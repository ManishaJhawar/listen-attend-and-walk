# -*- coding: utf-8 -*-
"""
beam search modules for Neural Walker

"""

import pickle
import time
import numpy
import theano
from theano import sandbox
import theano.tensor as tensor
import os
import scipy.io
from collections import defaultdict
from theano.tensor.shared_randomstreams import RandomStreams
import utils

dtype = theano.config.floatX


#

# TODO: beam search for neural walker
class BeamSearchNeuralWalker(object):
	'''
    This is a beam search code for Neural Walker
    '''

	def __init__(self, settings):
		# print "initializing the beam searcher ... "
		assert (settings['size_beam'] >= 1)
		self.size_beam = settings['size_beam']
		#
		assert (
			settings['path_model'] == None or settings['trained_model'] == None
		)
		#
		if settings['path_model'] != None:
			with open(settings['path_model'], 'rb') as f:
				self.model = pickle.load(f)
		else:
			assert (settings['trained_model'] != None)
			self.model = settings['trained_model']
		#
		# convert float64 to float32
		for param_name in self.model:
			self.model[param_name] = numpy.float32(self.model[param_name])
		#
		self.dim_model = self.model['Emb_enc_forward'].shape[1]  # Matrix of shape [524*100] => self.dim_model = 100
		#
		# re-set the weights due to drop_out_rate
		self.drop_out_rate = self.model['drop_out_rate']
		assert (
			self.drop_out_rate <= numpy.float32(1.0)
		)
		self.model['W_out_hz'][:self.dim_model, :] = numpy.copy(
				self.model['W_out_hz'][:self.dim_model, :] * self.drop_out_rate
		)
		print "type(model)", type(self.model)
		print "self.model['W_out_hz'][:self.dim_model, :]=", self.model['W_out_hz'][:self.dim_model, :].shape, "self.model=", type(self.model['W_out_hz'])
		#
		#
		self.ht_encode = numpy.zeros(
				(self.dim_model,), dtype=dtype
		)
		self.ct_encode = numpy.zeros(
				(self.dim_model,), dtype=dtype
		)
		#
		self.scope_att = None
		self.scope_att_times_W = None
		#
		self.beam_list = []
		self.finish_list = []
		# self.normalize_mode = settings['normalize_mode']
		# whether to normalize the cost over length of sequence
		#
		# self.lang2idx = settings['lang2idx']
		self.dim_lang = settings['dim_lang']
		self.map = settings['map']
		self.Emb_lang_sparse = numpy.identity(
				self.dim_lang, dtype=dtype
		)
		#

	def refresh_state(self):
		# print "refreshing the states of beam search ... "
		self.ht_encode = numpy.zeros(
				(self.dim_model,), dtype=dtype
		)
		self.ct_encode = numpy.zeros(
				(self.dim_model,), dtype=dtype
		)
		#
		self.scope_att = None
		self.scope_att_times_W = None
		#
		self.beam_list = []
		self.finish_list = []

	#
	def sigmoid(self, x):
		return 1 / (1 + numpy.exp(-x))

	#
	def set_encoder_forward(self):
		""" seq_lang_numpy contains word indices.
		So, only those indices will be extracted from Emb_enc_forward """
		xt_lang_forward = self.model['Emb_enc_forward'][self.seq_lang_numpy, :]
		shape_encode = xt_lang_forward.shape  # Matrix of shape (x,100) where, x (# words in a sentence) value varies for different instructions
		self.ht_enc_forward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		self.ct_enc_forward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		len_lang = shape_encode[0]
		for time_stamp in range(-1, len_lang - 1, 1):

			""" LSTM cell update steps """
			""" x=bias+(weights*[prev. hidden input, current input] """
			# post_transform.shape = (400,)
			post_transform = self.model['b_enc_forward'] + numpy.dot(
					numpy.concatenate(
							(
								xt_lang_forward[time_stamp + 1, :],
								self.ht_enc_forward[time_stamp, :]
							),
							axis=0
					),
					self.model['W_enc_forward']
			)

			""" input gate layer, it = sigmoid(x[:100]) """
			# gate_input_numpy.shape = (100,)
			gate_input_numpy = self.sigmoid(
					post_transform[:self.dim_model]
			)

			""" forget gate layer, ft = sigmoid(x[100:200]) """
			# gate_forget_numpy.shape = (100,)
			gate_forget_numpy = self.sigmoid(
					post_transform[self.dim_model:2 * self.dim_model]
			)

			""" output gate layer, ot = sigmoid(x[200:300]) """
			# gate_output_numpy.shape = (100,)
			gate_output_numpy = self.sigmoid(
					post_transform[2 * self.dim_model:3 * self.dim_model]
			)

			""" candidate values, ct = tanh(x[300:400]) """
			# gate_pre_c_numpy.shape = (100,)
			gate_pre_c_numpy = numpy.tanh(
					post_transform[3 * self.dim_model:]
			)

			""" Updating the cell state Ct wrt LSTM network """
			self.ct_enc_forward[time_stamp + 1, :] = gate_forget_numpy * self.ct_enc_forward[time_stamp, :] + gate_input_numpy * gate_pre_c_numpy

			""" Calculating the final output of the LSTM cell """
			self.ht_enc_forward[time_stamp + 1, :] = gate_output_numpy * numpy.tanh(
					self.ct_enc_forward[time_stamp + 1, :])
			#
			#

	#
	##
	def set_encoder_backward(self):
		xt_lang_backward = self.model['Emb_enc_backward'][self.seq_lang_numpy, :][::-1, :]
		shape_encode = xt_lang_backward.shape
		self.ht_enc_backward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		self.ct_enc_backward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		len_lang = shape_encode[0]
		for time_stamp in range(-1, len_lang - 1, 1):
			post_transform = self.model['b_enc_backward'] + numpy.dot(
					numpy.concatenate(
							(
								xt_lang_backward[time_stamp + 1, :],
								self.ht_enc_backward[time_stamp, :]
							),
							axis=0
					),
					self.model['W_enc_backward']
			)
			#
			gate_input_numpy = self.sigmoid(
					post_transform[:self.dim_model]
			)
			gate_forget_numpy = self.sigmoid(
					post_transform[self.dim_model:2 * self.dim_model]
			)
			gate_output_numpy = self.sigmoid(
					post_transform[2 * self.dim_model:3 * self.dim_model]
			)
			gate_pre_c_numpy = numpy.tanh(
					post_transform[3 * self.dim_model:]
			)
			self.ct_enc_backward[time_stamp + 1, :] = gate_forget_numpy * self.ct_enc_backward[time_stamp,
																		  :] + gate_input_numpy * gate_pre_c_numpy
			self.ht_enc_backward[time_stamp + 1, :] = gate_output_numpy * numpy.tanh(
					self.ct_enc_backward[time_stamp + 1, :])
			#
			#

	#
	#

	def set_encoder(
			self, seq_lang_numpy, seq_world_numpy
	):
		#
		self.seq_lang_numpy = seq_lang_numpy
		self.seq_world_numpy = seq_world_numpy
		#
		self.set_encoder_forward()
		self.set_encoder_backward()

		# self.scope_att.shape = (x,724) where, x value varies for different instructions
		self.scope_att = numpy.concatenate(
				(
					self.Emb_lang_sparse[self.seq_lang_numpy, :],
					self.ht_enc_forward,
					self.ht_enc_backward[::-1, :]
				),
				axis=1
		)
		# print "self.scope_att.shape=",self.scope_att.shape

		# self.scope_att_times_W.shape = (x,100) where, x value varies for different instructions
		self.scope_att_times_W = numpy.dot(
				self.scope_att, self.model['W_att_scope']  # (x,724)*(724,100)=(x,100)
		)
		# self.ht_encode = ht_source[:, 0]
		#

	def init_beam(self, pos_start, pos_end):
		# print "initialize beam ... "
		item = {
			'htm1': numpy.copy(self.ht_encode),  # (100,)
			'ctm1': numpy.copy(self.ct_encode),  # (100,)
			'feat_current_position': numpy.copy(  # (1,78)
					self.seq_world_numpy[0, :]
			),
			#
			'pos_current': pos_start,
			'pos_destination': pos_end,
			'list_pos': [numpy.copy(pos_start)],
			#
			'list_idx_action': [],
			'continue': True,
			#
			'cost': 0.00
		}
		self.beam_list.append(item)

	def softmax(self, x):
		# x is a vector
		exp_x = numpy.exp(x - numpy.amax(x))
		return exp_x / numpy.sum(exp_x)

	def decode_step(
			self, feat_current_position,
			htm1_action, ctm1_action
	):
		# xt_action.shape = (1,100)
		xt_action = numpy.dot(
				feat_current_position,  # (1,78)
				self.model['Emb_dec']  # (78,100) -- utils.sample_weights
		)
		# neural attention operations first -- weight_current_step.shape = (x,1)
		# Follow decoder formula from the paper
		# weight_current_step = Pa,t = Probability

		"""
		example:
		>>> a=np.array([1,2,3])
		>>> b=np.array([[2,2,2],[3,3,3]])
		>>> a+b
		array([[3, 4, 5],
       			[4, 5, 6]])
		"""

		# alpha calculation
		weight_current_step = self.softmax(
				# beta calculation
				numpy.dot(
						numpy.tanh(
								numpy.dot(
										htm1_action, self.model['W_att_target']  # (1,100)*(100,100)=(1,100)
								) + self.scope_att_times_W  # (x,100) => each element in (x,100) will be added with the element of (1,100) (refer example)
						),
						self.model['b_att']  # (100,1) =>(x,100)*(100,1)=(x,1)
				)
		)
		# self.scope_att is the combo of h-fwd, h-bwd and i/p instructions
		# (1,x)*(x,724)=(1,724)
		zt_action = numpy.dot(
				weight_current_step,
				self.scope_att
		)

		# (1,400) + [(1,924)*(924,400)=(1,400)] = (1,400)
		post_transform = self.model['b_dec'] + numpy.dot(
				# (xt_action--world_state)+(htm1_action--prev.hidden state of lstm)+(zt_action--context vector)
				numpy.concatenate(
						(
							xt_action, htm1_action, zt_action  # (1,100)+(1,100)+(1,724) = (1,924)
						),
						axis=0
				),
				self.model['W_dec']  # (924,400)
		)
		#
		gate_input_numpy = self.sigmoid(
				post_transform[:self.dim_model]
		)
		gate_forget_numpy = self.sigmoid(
				post_transform[self.dim_model:2 * self.dim_model]
		)
		gate_output_numpy = self.sigmoid(
				post_transform[2 * self.dim_model:3 * self.dim_model]
		)
		gate_pre_c_numpy = numpy.tanh(
				post_transform[3 * self.dim_model:]
		)
		ct_action = gate_forget_numpy * ctm1_action + gate_input_numpy * gate_pre_c_numpy
		ht_action = gate_output_numpy * numpy.tanh(ct_action)
		# ht_action -- lstm's current state, zt_action -- context vector

		# (1,100)*(100,4)=(1,4)
		post_transform_prob = numpy.dot(
				#  (1,100)+(1,100)=(1,100)
				xt_action + numpy.dot(
						#  (1,824)*(824,100) = (1,100)
						numpy.concatenate(
								(ht_action, zt_action), axis=0  # (1,100) concat (1,724) = (1,824)
						),
						self.model['W_out_hz']  # (824,100)
 				),
				self.model['W_out']
		)
		# probability calculation
		exp_post_trans = numpy.exp(
				post_transform_prob - numpy.amax(post_transform_prob)
		)
		probt = exp_post_trans / numpy.sum(exp_post_trans)  # (4,)
		log_probt = numpy.log(probt + numpy.float32(1e-8))  # (4,)
		return xt_action, ht_action, ct_action, probt, log_probt

	def validate_step(self, idx_action, feat_current_position):
		assert (
			idx_action == 3 or idx_action == 2 or idx_action == 1 or idx_action == 0
		)
		if idx_action == 0:  # checking for the forward orientation
			# feat_current_position[23] indicates if the way is walkable or not for fwd vector
			if feat_current_position[23] > 0.5:
				# 6 + 18 = 24 --> 23
				return False  # indicates that the path is not walkable
			else:
				return True  # indicates that the path is walkable
		else:
			return True

	#
	def get_left_and_right(self, direc_current):
		# direc_current can be 0 , 90, 180, 270
		# it is the current facing direction
		assert (direc_current == 0 or direc_current == 90 or direc_current == 180 or direc_current == 270)
		left = direc_current - 90
		if left == -90:
			left = 270
		right = direc_current + 90
		if right == 360:
			right = 0
		behind = direc_current + 180
		if behind == 360:
			behind = 0
		elif behind == 450:
			behind = 90
		return left, right, behind

	#
	def one_step_forward(self, pos_current):
		direc_current = pos_current[2]
		pos_next = numpy.copy(pos_current)
		assert (
			direc_current == 0 or direc_current == 90 or direc_current == 180 or direc_current == 270
		)
		# grid is in 3rd quadrant (non-negative y value)
		if direc_current == 0:
			pos_next[1] -= 1  # moving 1 step fwd in North direction i.e decrementing y by 1
		elif direc_current == 90:
			pos_next[0] += 1  # moving 1 step fwd in East direction i.e incrementing x by 1
		elif direc_current == 180:
			pos_next[1] += 1  # moving 1 step fwd in South direction i.e incrementing y by 1
		else:
			pos_next[0] -= 1  # moving 1 step fwd in West direction i.e decrementing x by 1
		return pos_next

	#
	#
	#
	def take_one_step(self, pos_current, idx_action):
		#
		left_current, right_current, _ = self.get_left_and_right(
				pos_current[2]
		)
		pos_next = numpy.copy(pos_current)
		assert (idx_action == 0 or idx_action == 1 or idx_action == 2 or idx_action == 3)
		if idx_action == 1:
			# turn left
			pos_next[2] = left_current  # left orientation
		elif idx_action == 2:
			pos_next[2] = right_current  # right orientation
		elif idx_action == 3:  # stop
			pass
		else:
			pos_next = self.one_step_forward(pos_current)
		return pos_next

	#
	def get_feat_current_position(self, pos_current):
		#
		nodes = self.map['nodes']
		x_current, y_current, direc_current = pos_current[0], pos_current[1], pos_current[2]
		#
		count_pos_found = 0
		#
		for idx_node, node in enumerate(nodes):
			if node['x'] == x_current and node['y'] == y_current:
				# find this position in the map
				# so we can get its feature
				count_pos_found += 1
				#
				left_current, right_current, behind_current = self.get_left_and_right(direc_current)
				#
				feat_node = numpy.cast[dtype](
						node['objvec']
				)
				feat_forward = numpy.cast[dtype](
						node['capfeat'][direc_current]
				)
				feat_left = numpy.cast[dtype](
						node['capfeat'][left_current]
				)
				feat_right = numpy.cast[dtype](
						node['capfeat'][right_current]
				)
				feat_behind = numpy.cast[dtype](
						node['capfeat'][behind_current]
				)
				#
				feat_current_position = numpy.copy(
						numpy.concatenate(
								(feat_node, feat_forward, feat_left, feat_right, feat_behind),
								axis=0
						)
				)
				#
		assert (count_pos_found > 0)
		return feat_current_position
		# since the action is validated before moving
		# this position must be in this map
		#

	def search_func(self):
		# print "search for target ... "
		counter, max_counter = 0, 100
		while ((len(self.finish_list) < self.size_beam) and (counter < max_counter)):
			new_list = []
			for item in self.beam_list:
				# xt_item -- current world state, ht_item -- lstm state, ct_item -- context of the instruction
				# probt_item, log_prot_item -- conditional prob distribution over the next action
				xt_item, ht_item, ct_item, probt_item, log_probt_item = self.decode_step(
						item['feat_current_position'],
						item['htm1'], item['ctm1']
				)
				top_k_list = range(probt_item.shape[0])  # (4,)
				for top_idx_action in top_k_list:
					# item['feat_current_position'] is the world state of 1st position of the action set
					if self.validate_step(top_idx_action, item['feat_current_position']):
						# print "item['list_idx_action']=",item['list_idx_action']
						new_item = {
							'htm1': numpy.copy(ht_item),
							'ctm1': numpy.copy(ct_item),
							'list_idx_action': [
								idx for idx in item['list_idx_action']
								],
							'list_pos': [
								numpy.copy(pos) for pos in item['list_pos']
								]
						}
						# print "new_item['list_idx_action']=",new_item['list_idx_action']
						new_item['list_idx_action'].append(
								top_idx_action
						)
						# position value gets updated with new coordinates/orientation
						new_item['pos_current'] = numpy.copy(
								self.take_one_step(
										item['pos_current'], top_idx_action
								)
						)
						#
						new_item['pos_destination'] = numpy.copy(
								item['pos_destination']
						)
						# the world state of new position
						new_item['feat_current_position'] = numpy.copy(
								self.get_feat_current_position(
										new_item['pos_current']
								)
						)
						#
						new_item['list_pos'].append(
								numpy.copy(new_item['pos_current'])
						)
						#
						if top_idx_action == 3:
							# 3 -- stop
							new_item['continue'] = False
						else:
							new_item['continue'] = True
						#
						new_item['cost'] = item['cost'] + (-1.0) * log_probt_item[top_idx_action]
						#
						new_list.append(new_item)
			#
			new_list = sorted(
					new_list, key=lambda x: x['cost']
			)
			if len(new_list) > self.size_beam:
				new_list = new_list[:self.size_beam]  # performing the highest probability action only (greedy search)
			#
			self.beam_list = []
			while len(new_list) > 0:
				pop_item = new_list.pop(0)
				if pop_item['continue']:
					self.beam_list.append(pop_item)
				else:
					self.finish_list.append(pop_item)
			counter += 1
			#
		#
		if len(self.finish_list) > 0:
			self.finish_list = sorted(
					self.finish_list, key=lambda x: x['cost']
			)

			while len(self.finish_list) > self.size_beam:
				# print "Becoming zero..."
				self.finish_list.pop()

		# print "Length of finish list = ", len(self.finish_list)
		while len(self.finish_list) < self.size_beam:
			# print "len(self.finish_list)=",len(self.finish_list),"  self.size_beam=",self.size_beam
			# print "Entered!"
			self.finish_list.append(self.beam_list.pop(0))

	#
	#
	def count_path(self):
		print "# of finished responses is ", len(self.finish_list)

	def get_path(self):
		return self.finish_list[0]['list_pos']

	def check_pos_end(self):
		top_path = self.finish_list[0]
		diff_pos = numpy.sum(
				numpy.abs(
						top_path['pos_current'] - top_path['pos_destination']
				)
		)
		if diff_pos < 0.5:
			return True
		else:
			return False


# '''
# TODO: beam search for neural walker, ensemble of models
class BeamSearchNeuralWalkerEnsemble(object):
	'''
    # This is a beam search code for Neural Walker
    '''

	def __init__(self, settings):
		# print "initializing the beam searcher ... "
		assert (settings['size_beam'] >= 1)
		self.size_beam = settings['size_beam']
		#
		assert (
			settings['set_path_model'] != None
		)
		#
		self.list_models = []
		for path_model in settings['set_path_model']:
			with open(path_model, 'rb') as f:
				self.list_models.append(
						pickle.load(f)
				)
		#
		for model in self.list_models:
			for param_name in model:
				model[param_name] = numpy.float32(
						model[param_name]
				)
			model['dim_model'] = model['Emb_enc_forward'].shape[1]
			assert (
				model['drop_out_rate'] <= numpy.float32(1.0)
			)
			model['W_out_hz'][:model['dim_model'], :] = numpy.copy(
					model['W_out_hz'][:model['dim_model'], :] * model['drop_out_rate']
			)
			#
			model['ht_encode'] = numpy.zeros(
					(model['dim_model'],), dtype=dtype
			)
			model['ct_encode'] = numpy.zeros(
					(model['dim_model'],), dtype=dtype
			)
			#
			model['scope_att'] = None
			model['scope_att_times_W'] = None
			#
		#
		self.beam_list = []
		self.finish_list = []
		# self.normalize_mode = settings['normalize_mode']
		# whether to normalize the cost over length of sequence
		#
		self.dim_lang = settings['dim_lang']
		self.map = settings['map']
		self.Emb_lang_sparse = numpy.identity(
				self.dim_lang, dtype=dtype
		)
		#

	def refresh_state(self):
		# print "refreshing the states of beam search ... "
		for model in self.list_models:
			model['ht_encode'] = numpy.zeros(
					(model['dim_model'],), dtype=dtype
			)
			model['ct_encode'] = numpy.zeros(
					(model['dim_model'],), dtype=dtype
			)
			model['scope_att'] = None
			model['scope_att_times_W'] = None
		#
		self.beam_list = []
		self.finish_list = []

	#
	def sigmoid(self, x):
		return 1 / (1 + numpy.exp(-x))

	#
	def set_encoder_forward(self, idx_model):
		dim_model = self.list_models[idx_model]['dim_model']
		xt_lang_forward = self.list_models[idx_model]['Emb_enc_forward'][
						  self.seq_lang_numpy, :
						  ]
		shape_encode = xt_lang_forward.shape
		self.ht_enc_forward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		self.ct_enc_forward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		len_lang = shape_encode[0]
		for time_stamp in range(-1, len_lang - 1, 1):
			post_transform = self.list_models[idx_model]['b_enc_forward'] + numpy.dot(
					numpy.concatenate(
							(
								xt_lang_forward[time_stamp + 1, :],
								self.ht_enc_forward[time_stamp, :]
							),
							axis=0
					),
					self.list_models[idx_model]['W_enc_forward']
			)
			#
			gate_input_numpy = self.sigmoid(
					post_transform[:dim_model]
			)
			gate_forget_numpy = self.sigmoid(
					post_transform[dim_model:2 * dim_model]
			)
			gate_output_numpy = self.sigmoid(
					post_transform[2 * dim_model:3 * dim_model]
			)
			gate_pre_c_numpy = numpy.tanh(
					post_transform[3 * dim_model:]
			)
			self.ct_enc_forward[time_stamp + 1, :] = gate_forget_numpy * self.ct_enc_forward[time_stamp,
																		 :] + gate_input_numpy * gate_pre_c_numpy
			self.ht_enc_forward[time_stamp + 1, :] = gate_output_numpy * numpy.tanh(
					self.ct_enc_forward[time_stamp + 1, :])
			#
			#

	#
	##
	def set_encoder_backward(self, idx_model):
		dim_model = self.list_models[idx_model]['dim_model']
		xt_lang_backward = self.list_models[idx_model]['Emb_enc_backward'][
						   self.seq_lang_numpy, :
						   ][::-1, :]
		shape_encode = xt_lang_backward.shape
		self.ht_enc_backward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		self.ct_enc_backward = numpy.zeros(
				shape_encode, dtype=dtype
		)
		len_lang = shape_encode[0]
		for time_stamp in range(-1, len_lang - 1, 1):
			post_transform = self.list_models[idx_model]['b_enc_backward'] + numpy.dot(
					numpy.concatenate(
							(
								xt_lang_backward[time_stamp + 1, :],
								self.ht_enc_backward[time_stamp, :]
							),
							axis=0
					),
					self.list_models[idx_model]['W_enc_backward']
			)
			#
			gate_input_numpy = self.sigmoid(
					post_transform[:dim_model]
			)
			gate_forget_numpy = self.sigmoid(
					post_transform[dim_model:2 * dim_model]
			)
			gate_output_numpy = self.sigmoid(
					post_transform[2 * dim_model:3 * dim_model]
			)
			gate_pre_c_numpy = numpy.tanh(
					post_transform[3 * dim_model:]
			)
			self.ct_enc_backward[time_stamp + 1, :] = gate_forget_numpy * self.ct_enc_backward[time_stamp,
																		  :] + gate_input_numpy * gate_pre_c_numpy
			self.ht_enc_backward[time_stamp + 1, :] = gate_output_numpy * numpy.tanh(
					self.ct_enc_backward[time_stamp + 1, :])
			#
			#

	#
	#

	def set_encoder(
			self, seq_lang_numpy, seq_world_numpy
	):
		#
		self.seq_lang_numpy = seq_lang_numpy
		self.seq_world_numpy = seq_world_numpy
		#
		for idx_model, model in enumerate(self.list_models):
			self.set_encoder_forward(idx_model)
			self.set_encoder_backward(idx_model)
			model['scope_att'] = numpy.copy(
					numpy.concatenate(
							(
								self.Emb_lang_sparse[self.seq_lang_numpy, :],
								self.ht_enc_forward,
								self.ht_enc_backward[::-1, :]
							), axis=1
					)
			)
			model['scope_att_times_W'] = numpy.dot(
					model['scope_att'], model['W_att_scope']
			)
			#
			# self.ht_encode = ht_source[:, 0]
			#

	def init_beam(self, pos_start, pos_end):
		# print "initialize beam ... "
		item = {
			# 'htm1': numpy.copy(self.ht_encode),
			# 'ctm1': numpy.copy(self.ct_encode),
			'list_htm1': [],
			'list_ctm1': [],
			'feat_current_position': numpy.copy(
					self.seq_world_numpy[0, :]
			),
			#
			'pos_current': pos_start,
			'pos_destination': pos_end,
			'list_pos': [numpy.copy(pos_start)],
			#
			'list_idx_action': [],
			'continue': True,
			#
			'cost': 0.00
		}
		#
		for model in self.list_models:
			item['list_htm1'].append(
					numpy.copy(model['ht_encode'])
			)
			item['list_ctm1'].append(
					numpy.copy(model['ct_encode'])
			)
		#
		self.beam_list.append(item)

	def softmax(self, x):
		# x is a vector
		exp_x = numpy.exp(x - numpy.amax(x))
		return exp_x / numpy.sum(exp_x)

	def decode_step(
			self, feat_current_position,
			htm1_action, ctm1_action,
			idx_model
	):
		#
		dim_model = self.list_models[idx_model]['dim_model']
		#
		xt_action = numpy.dot(
				feat_current_position,
				self.list_models[idx_model]['Emb_dec']
		)
		# neural attention operations first
		weight_current_step = self.softmax(
				numpy.dot(
						numpy.tanh(
								numpy.dot(
										htm1_action, self.list_models[idx_model]['W_att_target']
								) + self.list_models[idx_model]['scope_att_times_W']
						),
						self.list_models[idx_model]['b_att']
				)
		)
		#
		zt_action = numpy.dot(
				weight_current_step,
				self.list_models[idx_model]['scope_att']
		)
		#
		post_transform = self.list_models[idx_model]['b_dec'] + numpy.dot(
				numpy.concatenate(
						(
							xt_action, htm1_action, zt_action
						),
						axis=0
				),
				self.list_models[idx_model]['W_dec']
		)
		#
		gate_input_numpy = self.sigmoid(
				post_transform[:dim_model]
		)
		gate_forget_numpy = self.sigmoid(
				post_transform[dim_model:2 * dim_model]
		)
		gate_output_numpy = self.sigmoid(
				post_transform[2 * dim_model:3 * dim_model]
		)
		gate_pre_c_numpy = numpy.tanh(
				post_transform[3 * dim_model:]
		)
		ct_action = gate_forget_numpy * ctm1_action + gate_input_numpy * gate_pre_c_numpy
		ht_action = gate_output_numpy * numpy.tanh(ct_action)
		#
		post_transform_prob = numpy.dot(
				xt_action + numpy.dot(
						numpy.concatenate(
								(ht_action, zt_action), axis=0
						),
						self.list_models[idx_model]['W_out_hz']
				),
				self.list_models[idx_model]['W_out']
		)
		#
		exp_post_trans = numpy.exp(
				post_transform_prob - numpy.amax(post_transform_prob)
		)
		probt = exp_post_trans / numpy.sum(exp_post_trans)
		log_probt = numpy.log(probt + numpy.float32(1e-8))
		return xt_action, ht_action, ct_action, probt, log_probt

	def validate_step(self, idx_action, feat_current_position):
		assert (
			idx_action == 3 or idx_action == 2 or idx_action == 1 or idx_action == 0
		)
		if idx_action == 0:
			if feat_current_position[23] > 0.5:
				# 6 + 18 = 24 --> 23
				return False
			else:
				return True
		else:
			return True

	#
	def get_left_and_right(self, direc_current):
		# direc_current can be 0 , 90, 180, 270
		# it is the current facing direction
		assert (direc_current == 0 or direc_current == 90 or direc_current == 180 or direc_current == 270)
		left = direc_current - 90
		if left == -90:
			left = 270
		right = direc_current + 90
		if right == 360:
			right = 0
		behind = direc_current + 180
		if behind == 360:
			behind = 0
		elif behind == 450:
			behind = 90
		return left, right, behind

	#
	def one_step_forward(self, pos_current):
		direc_current = pos_current[2]
		pos_next = numpy.copy(pos_current)
		assert (
			direc_current == 0 or direc_current == 90 or direc_current == 180 or direc_current == 270
		)
		if direc_current == 0:
			pos_next[1] -= 1
		elif direc_current == 90:
			pos_next[0] += 1
		elif direc_current == 180:
			pos_next[1] += 1
		else:
			pos_next[0] -= 1
		return pos_next

	#
	#
	#
	def take_one_step(self, pos_current, idx_action):
		#
		left_current, right_current, _ = self.get_left_and_right(
				pos_current[2]
		)
		pos_next = numpy.copy(pos_current)
		assert (idx_action == 0 or idx_action == 1 or idx_action == 2 or idx_action == 3)
		if idx_action == 1:
			# turn left
			pos_next[2] = left_current
		elif idx_action == 2:
			pos_next[2] = right_current
		elif idx_action == 3:
			pass
		else:
			pos_next = self.one_step_forward(pos_current)
		return pos_next

	#
	def get_feat_current_position(self, pos_current):
		#
		nodes = self.map['nodes']
		x_current, y_current, direc_current = pos_current[0], pos_current[1], pos_current[2]
		#
		count_pos_found = 0
		#
		for idx_node, node in enumerate(nodes):
			if node['x'] == x_current and node['y'] == y_current:
				# find this position in the map
				# so we can get its feature
				count_pos_found += 1
				#
				left_current, right_current, behind_current = self.get_left_and_right(direc_current)
				#
				feat_node = numpy.cast[dtype](
						node['objvec']
				)
				feat_forward = numpy.cast[dtype](
						node['capfeat'][direc_current]
				)
				feat_left = numpy.cast[dtype](
						node['capfeat'][left_current]
				)
				feat_right = numpy.cast[dtype](
						node['capfeat'][right_current]
				)
				feat_behind = numpy.cast[dtype](
						node['capfeat'][behind_current]
				)
				#
				feat_current_position = numpy.copy(
						numpy.concatenate(
								(feat_node, feat_forward, feat_left, feat_right, feat_behind),
								axis=0
						)
				)
				#
		assert (count_pos_found > 0)
		return feat_current_position
		# since the action is validated before moving
		# this position must be in this map
		#

	def search_func(self):
		# print "search for target ... "
		counter, max_counter = 0, 100
		while ((len(self.finish_list) < self.size_beam) and (counter < max_counter)):
			new_list = []
			for item in self.beam_list:
				#
				list_probt = []
				list_ht, list_ct = [], []
				#
				for idx_model, model in enumerate(self.list_models):
					xt_item_model, ht_item_model, ct_item_model, probt_item_model, log_probt_item_model = self.decode_step(
							item['feat_current_position'],
							item['list_htm1'][idx_model],
							item['list_ctm1'][idx_model],
							idx_model
					)
					list_probt.append(numpy.copy(probt_item_model))
					list_ht.append(numpy.copy(ht_item_model))
					list_ct.append(numpy.copy(ct_item_model))
				probt_item = numpy.mean(
						numpy.array(list_probt), axis=0
				)
				log_probt_item = numpy.log(
						probt_item + numpy.float32(1e-8)
				)
				top_k_list = range(probt_item.shape[0])
				for top_idx_action in top_k_list:
					if self.validate_step(top_idx_action, item['feat_current_position']):
						new_item = {
							'list_htm1': [
								numpy.copy(ht_item_model) for ht_item_model in list_ht
								],
							'list_ctm1': [
								numpy.copy(ct_item_model) for ct_item_model in list_ct
								],
							'list_idx_action': [
								idx for idx in item['list_idx_action']
								],
							'list_pos': [
								numpy.copy(pos) for pos in item['list_pos']
								]
						}
						new_item['list_idx_action'].append(
								top_idx_action
						)
						#
						new_item['pos_current'] = numpy.copy(
								self.take_one_step(
										item['pos_current'], top_idx_action
								)
						)
						#
						new_item['pos_destination'] = numpy.copy(
								item['pos_destination']
						)
						#
						new_item['feat_current_position'] = numpy.copy(
								self.get_feat_current_position(
										new_item['pos_current']
								)
						)
						#
						new_item['list_pos'].append(
								numpy.copy(new_item['pos_current'])
						)
						#
						if top_idx_action == 3:
							# 3 -- stop
							new_item['continue'] = False
						else:
							new_item['continue'] = True
						#
						new_item['cost'] = item['cost'] + (-1.0) * log_probt_item[top_idx_action]
						#
						new_list.append(new_item)
			#
			new_list = sorted(
					new_list, key=lambda x: x['cost']
			)
			if len(new_list) > self.size_beam:
				new_list = new_list[:self.size_beam]
			#
			self.beam_list = []
			while len(new_list) > 0:
				pop_item = new_list.pop(0)
				if pop_item['continue']:
					self.beam_list.append(pop_item)
				else:
					self.finish_list.append(pop_item)
			counter += 1
			#
		#
		if len(self.finish_list) > 0:
			self.finish_list = sorted(
					self.finish_list, key=lambda x: x['cost']
			)
			while len(self.finish_list) > self.size_beam:
				self.finish_list.pop()
		while len(self.finish_list) < self.size_beam:
			self.finish_list.append(self.beam_list.pop(0))

	#
	#
	def count_path(self):
		print "# of finished responses is ", len(self.finish_list)

	def get_path(self):
		return self.finish_list[0]['list_pos']

	def check_pos_end(self):
		top_path = self.finish_list[0]
		diff_pos = numpy.sum(
				numpy.abs(
						top_path['pos_current'] - top_path['pos_destination']
				)
		)
		if diff_pos < 0.5:
			return True
		else:
			return False

# '''
