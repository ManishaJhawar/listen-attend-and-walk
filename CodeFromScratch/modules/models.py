# -*- coding: utf-8 -*-
"""
the modules for Neural Walker model
we use :
1) bi-directional LSTM as encoder
2) multi-input neural aligner
3) LSTM as decoder
4) deep-output layer

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


class NeuralWalker(object):
	'''
    Here is the neural walker module
    As the dataset is small, we only implement non-batch version, to be simple
    '''

	def __init__(self, model_settings):
		#
		self.dim_model = model_settings['dim_model']  # 100
		self.dim_world = model_settings['dim_world']  # 78
		# it is the dim of raw world input
		# raw world input is NOT one-hot vector
		self.dim_lang = model_settings['dim_lang']  # 524
		self.dim_action = model_settings['dim_action']  # 4
		# theano.tensor.var.TensorVariable ,.tensor.var.TensorVariable
		# drop_out related stuff
		self.drop_out_rate = model_settings['drop_out_rate']  # 0.9
		assert (
			self.drop_out_rate <= numpy.float32(1.0)
		)
		self.rnd_gen = RandomStreams(seed=12345)
		self.drop_out_layer = self.rnd_gen.uniform(
				(self.dim_model,)) < self.drop_out_rate  # List of boolean variable of shape [100]
		# print "drop_out_layer=",self.drop_out_layer.eval()  # [100]

		"""
        drop_out_layer= [ True  True False  True  True  True  True  True  True  True  True  True
                        True  True  True False  True  True  True False  True  True  True  True
                        True  True  True  True  True  True  True False  True  True  True  True
                        True  True  True  True  True  True  True False  True False  True False
                        True  True  True  True  True  True  True  True  True False  True  True
                        True  True  True  True  True  True  True  True  True  True  True  True
                        True  True  True  True  True  True  True False  True  True  True  True
                        True  True  True  True  True  True  True False  True  True  True  True
                        False  True  True  True]
        """
		self.drop_out_layer_gen = theano.function(
				[], self.drop_out_layer
		)
		#
		#
		print "dim of model, world, lang and action is : ", self.dim_model, self.dim_world, self.dim_lang, self.dim_action
		#
		""" identity matrix of shape [524*524] """
		self.Emb_lang_sparse = theano.shared(
				numpy.identity(self.dim_lang, dtype=dtype),
				name='Emb_lang_sparse'
		)
		# print "self.Emb_lang_sparse=",self.Emb_lang_sparse.shape.eval()
		# this is the I-matrix that stands for idx of tokens
		#
		""" Matrix of shape [524*100] """
		self.Emb_enc_forward = theano.shared(
				utils.sample_weights(self.dim_lang, self.dim_model),
				name='Emb_enc_forward'
		)
		# print "self.Emb_enc_forward=",self.Emb_enc_forward.eval()," ", self.Emb_enc_forward.shape.eval()

		""" Matrix of shape [200*400] """
		self.W_enc_forward = theano.shared(
				utils.sample_weights(
						2 * self.dim_model, 4 * self.dim_model
				), name='W_enc_forward'
		)
		# print "self.W_enc_forward=",self.W_enc_forward.eval()," ", self.W_enc_forward.shape.eval()

		""" Matrix of shape [400] """
		self.b_enc_forward = theano.shared(
				numpy.zeros((4 * self.dim_model,), dtype=dtype),
				name='b_enc_forward'
		)
		# print "self.b_enc_forward=",self.b_enc_forward.eval()," ", self.b_enc_forward.shape.eval()
		#
		""" Matrix of shape [524*100] """
		self.Emb_enc_backward = theano.shared(
				utils.sample_weights(self.dim_lang, self.dim_model),
				name='Emb_enc_backward'
		)

		""" Matrix of shape [200*400] """
		self.W_enc_backward = theano.shared(
				utils.sample_weights(
						2 * self.dim_model, 4 * self.dim_model
				), name='W_enc_backward'
		)

		""" Matrix of shape [400] """
		self.b_enc_backward = theano.shared(
				numpy.zeros((4 * self.dim_model,), dtype=dtype),
				name='b_enc_backward'
		)
		#
		""" Matrix of shape [724*100] """
		self.W_att_scope = theano.shared(
				utils.sample_weights(
						self.dim_lang + 2 * self.dim_model, self.dim_model
				), name='W_att_scope'
		)

		""" Matrix of shape [100*100] """
		self.W_att_target = theano.shared(
				utils.sample_weights(
						self.dim_model, self.dim_model
				), name='W_att_target'
		)
		# print "self.W_att_target=",self.W_att_target.eval()," ", self.W_att_target.shape.eval()

		""" Matrix of shape [100] """
		self.b_att = theano.shared(
				numpy.zeros((self.dim_model,), dtype=dtype),
				name='b_att'
		)
		#
		""" Matrix of shape [78*100] """
		self.Emb_dec = theano.shared(
				utils.sample_weights(self.dim_world, self.dim_model),
				name='Emb_dec'
		)

		""" Matrix of shape [924*400] """
		self.W_dec = theano.shared(
				utils.sample_weights(
						self.dim_lang + 4 * self.dim_model, 4 * self.dim_model
				), name='W_dec'
		)
		# print "self.W_dec=",self.W_dec.eval()," ", self.W_dec.shape.eval()

		""" Matrix of shape [400] """
		self.b_dec = theano.shared(
				numpy.zeros((4 * self.dim_model,), dtype=dtype),
				name='b_dec'
		)
		#

		""" Matrix of shape [824*100] """
		self.W_out_hz = theano.shared(
				utils.sample_weights(
						self.dim_lang + 3 * self.dim_model, self.dim_model
				), name='W_out_hz'
		)

		""" Matrix of shape [100*4] """
		self.W_out = theano.shared(
				utils.sample_weights(
						self.dim_model, self.dim_action
				), name='W_out'
		)
		#

		""" Matrix of shape [100] """
		self.c0 = theano.shared(
				numpy.zeros((self.dim_model,), dtype=dtype),
				name='c0'
		)

		""" Matrix of shape [100] """
		self.h0 = theano.shared(
				numpy.zeros((self.dim_model,), dtype=dtype),
				name='h0'
		)
		#
		self.params = [
			self.Emb_enc_forward,
			self.W_enc_forward, self.b_enc_forward,
			self.Emb_enc_backward,
			self.W_enc_backward, self.b_enc_backward,
			#
			self.W_att_scope, self.W_att_target, self.b_att,
			self.Emb_dec,
			self.W_dec, self.b_dec,
			self.W_out_hz, self.W_out
		]
		#
		self.cost = None
		self.grad_params = None
		self.log_prob = None

	#

	def func_enc_forward(self, xt, htm1, ctm1):
		'''
        we separate the functions for 2 encoders
        to save the cost of weights passing
        even though the code is roughly same
        '''
		# xt -- embedded word
		# (1,400)+((1,200)*(200,400)=(1,400))=(1,400)

		post_transform = self.b_enc_forward + theano.dot(
				tensor.concatenate(
						[xt, htm1], axis=0
				),
				self.W_enc_forward
		)
		gate_input = tensor.nnet.sigmoid(
				post_transform[:self.dim_model]
		)
		gate_forget = tensor.nnet.sigmoid(
				post_transform[self.dim_model:2 * self.dim_model]
		)
		gate_output = tensor.nnet.sigmoid(
				post_transform[2 * self.dim_model:3 * self.dim_model]
		)
		gate_pre_c = tensor.tanh(
				post_transform[3 * self.dim_model:]
		)
		ct = gate_forget * ctm1 + gate_input * gate_pre_c
		ht = gate_output * tensor.tanh(ct)
		return ht, ct

	def func_enc_backward(self, xt, htm1, ctm1):
		# xt -- embedded word
		post_transform = self.b_enc_backward + theano.dot(
				tensor.concatenate(
						[xt, htm1], axis=0
				),
				self.W_enc_backward
		)
		gate_input = tensor.nnet.sigmoid(
				post_transform[:self.dim_model]
		)
		gate_forget = tensor.nnet.sigmoid(
				post_transform[self.dim_model:2 * self.dim_model]
		)
		gate_output = tensor.nnet.sigmoid(
				post_transform[2 * self.dim_model:3 * self.dim_model]
		)
		gate_pre_c = tensor.tanh(
				post_transform[3 * self.dim_model:]
		)
		ct = gate_forget * ctm1 + gate_input * gate_pre_c
		ht = gate_output * tensor.tanh(ct)
		return ht, ct

	def softmax(self, x):
		# x is a vector
		exp_x = tensor.exp(x - tensor.max(x))
		return exp_x / tensor.sum(exp_x)

	def func_dec(self, xt, htm1, ctm1):
		# xt -- embedded world representations
		# computing alpha
		current_att_weight = self.softmax(  # (x,100)*(100,1) = (x,1)
				# computing beta
				theano.dot(
						tensor.tanh(
								theano.dot(
										htm1, self.W_att_target  # (x,100)*(100,100) = (x,100)
								) + self.scope_att_times_W  # (x,100)
						),
						self.b_att  # (100,1)
				)
		)
		# (1,x)*(x,724)=(1,724)
		zt = theano.dot(current_att_weight, self.scope_att)  # context vector from the multi-level aligner
		#
		post_transform = self.b_dec + theano.dot(
				tensor.concatenate(
						[xt, htm1, zt], axis=0  # according to paper xt - yt, htm1 - s(t-1), zt - zt
				),
				self.W_dec
		)
		gate_input = tensor.nnet.sigmoid(
				post_transform[:self.dim_model]
		)
		gate_forget = tensor.nnet.sigmoid(
				post_transform[self.dim_model:2 * self.dim_model]
		)
		gate_output = tensor.nnet.sigmoid(
				post_transform[2 * self.dim_model:3 * self.dim_model]
		)
		gate_pre_c = tensor.tanh(
				post_transform[3 * self.dim_model:]
		)
		ct = gate_forget * ctm1 + gate_input * gate_pre_c
		ht = gate_output * tensor.tanh(ct)  # in paper ht - st
		#
		# use drop_out
		ht_dropout = ht * self.drop_out_layer_gen()
		#
		return ht, ht_dropout, ct, zt

	def compute_loss(self, seq_lang, seq_world, seq_action):
		print "computing the loss function of Neural Walker ... "
		"""xt_lang_forward =<class 'theano.tensor.var.TensorVariable'>"""

		"""
		in x[[i,j,k],] i,j,k row of x will be extracted.
		 example:
		>>> x[[0,1,1],:]
		array([[1, 1, 1],
       		   [2, 2, 2],
               [2, 2, 2]])
		>>> x[[0,1,0,1],:]
		array([[1, 1, 1],
              [2, 2, 2],
              [1, 1, 1],
              [2, 2, 2]])
		"""

		xt_lang_forward = self.Emb_enc_forward[seq_lang, :]
		xt_lang_backward = self.Emb_enc_backward[seq_lang, :]

		# (y,78)*(78,100)=(y,100)
		xt_world = theano.dot(
				seq_world, self.Emb_dec
		)
		#
		[ht_enc_forward, ct_enc_forward], _ = theano.scan(
				fn=self.func_enc_forward,
				sequences=dict(input=xt_lang_forward, taps=[0]),
				outputs_info=[
					dict(initial=self.h0, taps=[-1]),
					dict(initial=self.c0, taps=[-1])
				],
				non_sequences=None
		)
		#
		[ht_enc_backward, ct_enc_backward], _ = theano.scan(
				fn=self.func_enc_backward,
				sequences=dict(input=xt_lang_backward, taps=[0]),
				outputs_info=[
					dict(initial=self.h0, taps=[-1]),
					dict(initial=self.c0, taps=[-1])
				],
				non_sequences=None,
				go_backwards=True
		)

		# concatenation of input vector, h-fwd and h-bwd
		"""
		>>> a=np.array([[1,1,1],[4,4,4]])
		>>> b=np.array([[2,2,2],[5,5,5]])
		>>> c=np.array([[3,3,3],[6,6,6]])
		>>> np.concatenate((a,b,c),axis=1)
		array([[1, 1, 1, 2, 2, 2, 3, 3, 3],
       			[4, 4, 4, 5, 5, 5, 6, 6, 6]])
		"""
		self.scope_att = tensor.concatenate(  # (x,724)
				[
					self.Emb_lang_sparse[seq_lang, :],  # (x,524)
					ht_enc_forward, ht_enc_backward[::-1, :]  # (x,100) & (x,100)
				],
				axis=1
		)
		self.scope_att_times_W = theano.dot(  # (x,724)*(724,100)=(x,100)
				self.scope_att, self.W_att_scope
		)
		#
		[ht_dec, ht_dropout_dec, ct_dec, zt_dec], _ = theano.scan(
				fn=self.func_dec,
				sequences=dict(input=xt_world, taps=[0]),
				outputs_info=[
					dict(initial=self.h0, taps=[-1]), None,
					dict(initial=self.c0, taps=[-1]), None
				],
				non_sequences=None
		)
		# in paper post_transform - qt
		post_transform = theano.dot(
				xt_world + theano.dot(
						tensor.concatenate(
								[ht_dropout_dec, zt_dec], axis=1
						),
						self.W_out_hz
				),
				self.W_out
		)
		# shape -- len_path * dim_action
		prob = tensor.nnet.softmax(post_transform)
		self.log_prob = tensor.log(prob + numpy.float32(1e-8))

		#
		loglikelihood_path = self.log_prob[
			tensor.arange(self.log_prob.shape[0]), seq_action
		]

		loglikelihood_action = tensor.mean(
				loglikelihood_path
		)
		#
		self.cost = -loglikelihood_action
		self.grad_params = tensor.grad(
				self.cost, self.params
		)
		#
		print "checking the type of variables ... "
		print "type of cost is ", self.cost.dtype  # float64
		for param, gparam in zip(self.params, self.grad_params):
			print "shape and type of param and grad_param for this variable are : ", (
				param.name, param.get_value().shape, param.dtype, gparam.dtype)
		#

	def get_model(self):
		print "getting model ... "
		model_dict = {}
		for param in self.params:
			model_dict[param.name] = numpy.copy(
					param.get_value()
			)
		model_dict['drop_out_rate'] = self.drop_out_rate
		return model_dict

	def save_model(self, save_file):
		print "saving model ... "
		model_dict = {}
		for param in self.params:
			model_dict[param.name] = numpy.copy(
					param.get_value()
			)
		model_dict['drop_out_rate'] = self.drop_out_rate
		with open(save_file, 'wb') as f:
			pickle.dump(model_dict, f)
