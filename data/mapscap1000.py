devset[0] is a dictionary having 3 key, value pairs

Key 1 = 'nodes' <type 'str'>
Value 1 = Is a list of 
{
	'neighbors': 
	{
		90: {'node': {'y': '5', 'x': '1', 'item': 'hatrack'}, 'edge': {'wall': 'fish', 'floor': 'grass'}}, 
		180: {'node': {'y': '6', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'blue'}}
	}, 
	'objvec': array([0, 0, 0, 0, 0, 0]), 
	'capfeat': {
					0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  0.,  0.,  0.,  1.], dtype=float32), 
					90: array([ 0.,  3.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  1.,  0., 0.,  0.,  0.,  0.,  0.], dtype=float32),
					180: array([ 5.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  7.,  1.,  0., 1.,  1.,  1.,  0.,  0.], dtype=float32), 
					270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  0.,  0.,  0.,  1.], dtype=float32)
				}, 
	'item': '', 
	'nbfeats': {
					0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
					90: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 
					180: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 
					270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
				}, 
	'y': 5, 
	'x': 0
}


Key 2 = 'edges' <type 'str'>
Value 2 = Is a list of 
{
    'wall': 'fish', 
    'n1': '0,5', 
    'n2': '0,6', 
    'floor': 'blue'
}


Key 3 = 'name' <type 'str'>

Value 3 = 'map-grid.xml' <type 'str'>


NOTE: devset[1] --> map-jelly
      devset[2] --> map-l









[{'neighbors': {90: {'node': {'y': '5', 'x': '1', 'item': 'hatrack'}, 'edge': {'wall': 'fish', 'floor': 'grass'}}, 180: {'node': {'y': '6', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'blue'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  3.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 5.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  7.,  1.,  0.,
        1.,  1.,  1.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 5, 'x': 0}, {'neighbors': {0: {'node': {'y': '5', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'blue'}}, 90: {'node': {'y': '6', 'x': '1', 'item': 'easel'}, 'edge': {'wall': 'fish', 'floor': 'flower'}}, 180: {'node': {'y': '7', 'x': '0', 'item': 'chair'}, 'edge': {'wall': 'fish', 'floor': 'blue'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0., 0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  3.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  1.,  0.,  1.,  0.], dtype=float32), 180: array([ 5.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  6.,  1.,  0., 1.,  1.,  1.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 180: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 6, 'x': 0}, {'neighbors': {0: {'node': {'y': '6', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'blue'}}, 90: {'node': {'y': '7', 'x': '1', 'item': 'lamp'}, 'edge': {'wall': 'fish', 'floor': 'wood'}}, 180: {'node': {'y': '8', 'x': '0', 'item': 'barstool'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}}, 'objvec': array([0, 0, 1, 0, 0, 0]), 'capfeat': {0: array([ 0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  1.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 5.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  5.,  1.,  0.,
        0.,  1.,  1.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': 'chair', 'nbfeats': {0: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 7, 'x': 0}, {'neighbors': {0: {'node': {'y': '7', 'x': '0', 'item': 'chair'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}, 90: {'node': {'y': '8', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'gravel'}}, 180: {'node': {'y': '9', 'x': '0', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}}, 'objvec': array([0, 0, 0, 0, 1, 0]), 'capfeat': {0: array([ 1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,
        1.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 1.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  4.,  0.,  0.,  0.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 180: array([ 4.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  4.,  1.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': 'barstool', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]), 90: array([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 8, 'x': 0}, {'neighbors': {0: {'node': {'y': '8', 'x': '0', 'item': 'barstool'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}, 90: {'node': {'y': '9', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 180: {'node': {'y': '10', 'x': '0', 'item': 'sofa'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 2.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  4.,  0.,  0.,
        1.,  0.,  1.,  0.,  0.], dtype=float32), 90: array([ 1.,  0.,  1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  1.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]), 90: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 9, 'x': 0}, {'neighbors': {0: {'node': {'y': '9', 'x': '0', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}, 90: {'node': {'y': '10', 'x': '1', 'item': 'chair'}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 180: {'node': {'y': '11', 'x': '0', 'item': 'hatrack'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}}, 'objvec': array([0, 0, 0, 1, 0, 0]), 'capfeat': {0: array([ 3.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  5.,  0.,  0.,
        1.,  0.,  1.,  0.,  0.], dtype=float32), 90: array([ 2.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        1.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  2.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': 'sofa', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 90: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 10, 'x': 0}, {'neighbors': {0: {'node': {'y': '10', 'x': '0', 'item': 'sofa'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}, 90: {'node': {'y': '11', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 180: {'node': {'y': '12', 'x': '0', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}}, 'objvec': array([1, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 4.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  6.,  0.,  0.,
        1.,  1.,  1.,  0.,  0.], dtype=float32), 90: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': 'hatrack', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]), 90: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 11, 'x': 0}, {'neighbors': {0: {'node': {'y': '11', 'x': '0', 'item': 'hatrack'}, 'edge': {'wall': 'butterfly', 'floor': 'blue'}}, 90: {'node': {'y': '12', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 5.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  7.,  1.,  0.,
        1.,  1.,  1.,  0.,  0.], dtype=float32), 90: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 90: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 12, 'x': 0}, {'neighbors': {90: {'node': {'y': '5', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'grass'}}, 180: {'node': {'y': '6', 'x': '1', 'item': 'easel'}, 'edge': {'wall': 'fish', 'floor': 'brick'}}, 270: {'node': {'y': '5', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'grass'}}}, 'objvec': array([1, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  2.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 2.,  2.,  1.,  0.,  0.,  0.,  0.,  5.,  0.,  0.,  0.,  0.,  1.,
        1.,  0.,  0.,  1.,  0.], dtype=float32), 270: array([ 0.,  1.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': 'hatrack', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 270: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 5, 'x': 1}, {'neighbors': {0: {'node': {'y': '5', 'x': '1', 'item': 'hatrack'}, 'edge': {'wall': 'fish', 'floor': 'brick'}}, 90: {'node': {'y': '6', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'flower'}}, 180: {'node': {'y': '7', 'x': '1', 'item': 'lamp'}, 'edge': {'wall': 'fish', 'floor': 'brick'}}, 270: {'node': {'y': '6', 'x': '0', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'flower'}}}, 'objvec': array([0, 0, 0, 0, 0, 1]), 'capfeat': {0: array([ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  2.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 180: array([ 2.,  1.,  1.,  0.,  0.,  0.,  0.,  4.,  0.,  0.,  0.,  0.,  1.,
        1.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': 'easel', 'nbfeats': {0: array([0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]), 270: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 6, 'x': 1}, {'neighbors': {0: {'node': {'y': '6', 'x': '1', 'item': 'easel'}, 'edge': {'wall': 'fish', 'floor': 'brick'}}, 90: {'node': {'y': '7', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'wood'}}, 180: {'node': {'y': '8', 'x': '1', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'brick'}}, 270: {'node': {'y': '7', 'x': '0', 'item': 'chair'}, 'edge': {'wall': 'fish', 'floor': 'wood'}}}, 'objvec': array([0, 1, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  2.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  1.,  0., 0.,  0.,  0.,  1.,  0.], dtype=float32), 90: array([ 0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0., 0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 2.,  0.,  1.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  0., 1.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0., 1.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': 'lamp', 'nbfeats': {0: array([0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 90: array([0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])}, 'y': 7, 'x': 1}, {'neighbors': {0: {'node': {'y': '7', 'x': '1', 'item': 'lamp'}, 'edge': {'wall': 'tower', 'floor': 'brick'}}, 90: {'node': {'y': '8', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}, 180: {'node': {'y': '9', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'brick'}}, 270: {'node': {'y': '8', 'x': '0', 'item': 'barstool'}, 'edge': {'wall': 'butterfly', 'floor': 'gravel'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  2.,  1.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  1.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 90: array([ 0.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 180: array([ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,
        1.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,
        0.,  0.,  1.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]), 90: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0])}, 'y': 8, 'x': 1}, {'neighbors': {0: {'node': {'y': '8', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'brick'}}, 90: {'node': {'y': '9', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 180: {'node': {'y': '10', 'x': '1', 'item': 'chair'}, 'edge': {'wall': 'butterfly', 'floor': 'brick'}}, 270: {'node': {'y': '9', 'x': '0', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 1.,  2.,  1.,  0.,  0.,  0.,  0.,  4.,  0.,  0.,  0.,  1.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 90: array([ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,
        1.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]), 270: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 9, 'x': 1}, {'neighbors': {0: {'node': {'y': '9', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'brick'}}, 90: {'node': {'y': '10', 'x': '2', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 270: {'node': {'y': '10', 'x': '0', 'item': 'sofa'}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 1, 0, 0, 0]), 'capfeat': {0: array([ 2.,  2.,  1.,  0.,  0.,  0.,  0.,  5.,  0.,  0.,  0.,  1.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 90: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32)}, 'item': 'chair', 'nbfeats': {0: array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])}, 'y': 10, 'x': 1}, {'neighbors': {180: {'node': {'y': '12', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 270: {'node': {'y': '11', 'x': '0', 'item': 'hatrack'}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])}, 'y': 11, 'x': 1}, {'neighbors': {0: {'node': {'y': '11', 'x': '1', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}, 270: {'node': {'y': '12', 'x': '0', 'item': ''}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 12, 'x': 1}, {'neighbors': {90: {'node': {'y': '5', 'x': '3', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'grass'}}, 180: {'node': {'y': '6', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'concrete'}}, 270: {'node': {'y': '5', 'x': '1', 'item': 'hatrack'}, 'edge': {'wall': 'fish', 'floor': 'grass'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  1.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  2.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  2.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])}, 'y': 5, 'x': 2}, {'neighbors': {0: {'node': {'y': '5', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'concrete'}}, 90: {'node': {'y': '6', 'x': '3', 'item': 'sofa'}, 'edge': {'wall': 'fish', 'floor': 'flower'}}, 180: {'node': {'y': '7', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'concrete'}}, 270: {'node': {'y': '6', 'x': '1', 'item': 'easel'}, 'edge': {'wall': 'fish', 'floor': 'flower'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  1.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  2.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  1.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 180: array([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])}, 'y': 6, 'x': 2}, {'neighbors': {0: {'node': {'y': '6', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'concrete'}}, 90: {'node': {'y': '7', 'x': '3', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'wood'}}, 270: {'node': {'y': '7', 'x': '1', 'item': 'lamp'}, 'edge': {'wall': 'tower', 'floor': 'wood'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  2.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  1.,
        1.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])}, 'y': 7, 'x': 2}, {'neighbors': {90: {'node': {'y': '8', 'x': '3', 'item': 'easel'}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}, 180: {'node': {'y': '9', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 270: {'node': {'y': '8', 'x': '1', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  1.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 180: array([ 0.,  0.,  2.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,
        0.,  0.,  1.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]), 180: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 8, 'x': 2}, {'neighbors': {0: {'node': {'y': '8', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 180: {'node': {'y': '10', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 270: {'node': {'y': '9', 'x': '1', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 1.,  0.,  1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 9, 'x': 2}, {'neighbors': {0: {'node': {'y': '9', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 270: {'node': {'y': '10', 'x': '1', 'item': 'chair'}, 'edge': {'wall': 'butterfly', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  2.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 2.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        1.,  1.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])}, 'y': 10, 'x': 2}, {'neighbors': {180: {'node': {'y': '6', 'x': '3', 'item': 'sofa'}, 'edge': {'wall': 'fish', 'floor': 'yellow'}}, 270: {'node': {'y': '5', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'grass'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  2.,  1.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  1.,  0.], dtype=float32), 270: array([ 0.,  3.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 270: array([0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 5, 'x': 3}, {'neighbors': {0: {'node': {'y': '5', 'x': '3', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'yellow'}}, 180: {'node': {'y': '7', 'x': '3', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'yellow'}}, 270: {'node': {'y': '6', 'x': '2', 'item': ''}, 'edge': {'wall': 'fish', 'floor': 'flower'}}}, 'objvec': array([0, 0, 0, 1, 0, 0]), 'capfeat': {0: array([ 0.,  1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  1.,  1.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 270: array([ 0.,  3.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  1.,  0.], dtype=float32)}, 'item': 'sofa', 'nbfeats': {0: array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 6, 'x': 3}, {'neighbors': {0: {'node': {'y': '6', 'x': '3', 'item': 'sofa'}, 'edge': {'wall': 'fish', 'floor': 'yellow'}}, 180: {'node': {'y': '8', 'x': '3', 'item': 'easel'}, 'edge': {'wall': 'tower', 'floor': 'yellow'}}, 270: {'node': {'y': '7', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'wood'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  2.,  0.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  1.,  0.], dtype=float32), 270: array([ 0.,  1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  1.,
        1.,  0.,  0.,  0.,  0.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 270: array([0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])}, 'y': 7, 'x': 3}, {'neighbors': {0: {'node': {'y': '7', 'x': '3', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'yellow'}}, 90: {'node': {'y': '8', 'x': '4', 'item': 'lamp'}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}, 270: {'node': {'y': '8', 'x': '2', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}}, 'objvec': array([0, 0, 0, 0, 0, 1]), 'capfeat': {0: array([ 0.,  2.,  1.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 1.,  0.,  2.,  0.,  0.,  0.,  0.,  0.,  3.,  0.,  0.,  0.,  0.,
        0.,  0.,  1.,  0.,  0.], dtype=float32)}, 'item': 'easel', 'nbfeats': {0: array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 8, 'x': 3}, {'neighbors': {180: {'node': {'y': '8', 'x': '4', 'item': 'lamp'}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}}, 'objvec': array([0, 0, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 270: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32)}, 'item': '', 'nbfeats': {0: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]), 270: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}, 'y': 7, 'x': 4}, {'neighbors': {0: {'node': {'y': '7', 'x': '4', 'item': ''}, 'edge': {'wall': 'tower', 'floor': 'concrete'}}, 270: {'node': {'y': '8', 'x': '3', 'item': 'easel'}, 'edge': {'wall': 'tower', 'floor': 'gravel'}}}, 'objvec': array([0, 1, 0, 0, 0, 0]), 'capfeat': {0: array([ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.], dtype=float32), 90: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 180: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.], dtype=float32), 270: array([ 1.,  0.,  3.,  0.,  0.,  0.,  0.,  0.,  4.,  0.,  0.,  0.,  0.,
        0.,  0.,  1.,  1.,  0.], dtype=float32)}, 'item': 'lamp', 'nbfeats': {0: array([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 90: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 180: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 270: array([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1])}, 'y': 8, 'x': 4}]
        
        
        
        
        
        
        
[{'wall': 'fish', 'n1': '0,5', 'n2': '0,6', 'floor': 'blue'}, {'wall': 'fish', 'n1': '0,6', 'n2': '0,7', 'floor': 'blue'}, {'wall': 'butterfly', 'n1': '0,7', 'n2': '0,8', 'floor': 'blue'}, {'wall': 'butterfly', 'n1': '0,8', 'n2': '0,9', 'floor': 'blue'}, {'wall': 'butterfly', 'n1': '0,9', 'n2': '0,10', 'floor': 'blue'}, {'wall': 'butterfly', 'n1': '0,10', 'n2': '0,11', 'floor': 'blue'}, {'wall': 'butterfly', 'n1': '0,11', 'n2': '0,12', 'floor': 'blue'}, {'wall': 'fish', 'n1': '1,5', 'n2': '1,6', 'floor': 'brick'}, {'wall': 'fish', 'n1': '1,6', 'n2': '1,7', 'floor': 'brick'}, {'wall': 'tower', 'n1': '1,7', 'n2': '1,8', 'floor': 'brick'}, {'wall': 'butterfly', 'n1': '1,8', 'n2': '1,9', 'floor': 'brick'}, {'wall': 'butterfly', 'n1': '1,9', 'n2': '1,10', 'floor': 'brick'}, {'wall': 'butterfly', 'n1': '1,11', 'n2': '1,12', 'floor': 'concrete'}, {'wall': 'fish', 'n1': '2,5', 'n2': '2,6', 'floor': 'concrete'}, {'wall': 'fish', 'n1': '2,6', 'n2': '2,7', 'floor': 'concrete'}, {'wall': 'tower', 'n1': '2,8', 'n2': '2,9', 'floor': 'concrete'}, {'wall': 'tower', 'n1': '2,9', 'n2': '2,10', 'floor': 'concrete'}, {'wall': 'fish', 'n1': '3,5', 'n2': '3,6', 'floor': 'yellow'}, {'wall': 'fish', 'n1': '3,6', 'n2': '3,7', 'floor': 'yellow'}, {'wall': 'tower', 'n1': '3,7', 'n2': '3,8', 'floor': 'yellow'}, {'wall': 'tower', 'n1': '4,7', 'n2': '4,8', 'floor': 'concrete'}, {'wall': 'fish', 'n1': '0,5', 'n2': '1,5', 'floor': 'grass'}, {'wall': 'fish', 'n1': '1,5', 'n2': '2,5', 'floor': 'grass'}, {'wall': 'fish', 'n1': '2,5', 'n2': '3,5', 'floor': 'grass'}, {'wall': 'fish', 'n1': '0,6', 'n2': '1,6', 'floor': 'flower'}, {'wall': 'fish', 'n1': '1,6', 'n2': '2,6', 'floor': 'flower'}, {'wall': 'fish', 'n1': '2,6', 'n2': '3,6', 'floor': 'flower'}, {'wall': 'fish', 'n1': '0,7', 'n2': '1,7', 'floor': 'wood'}, {'wall': 'tower', 'n1': '1,7', 'n2': '2,7', 'floor': 'wood'}, {'wall': 'tower', 'n1': '2,7', 'n2': '3,7', 'floor': 'wood'}, {'wall': 'butterfly', 'n1': '0,8', 'n2': '1,8', 'floor': 'gravel'}, {'wall': 'tower', 'n1': '1,8', 'n2': '2,8', 'floor': 'gravel'}, {'wall': 'tower', 'n1': '2,8', 'n2': '3,8', 'floor': 'gravel'}, {'wall': 'tower', 'n1': '3,8', 'n2': '4,8', 'floor': 'gravel'}, {'wall': 'butterfly', 'n1': '0,9', 'n2': '1,9', 'floor': 'concrete'}, {'wall': 'tower', 'n1': '1,9', 'n2': '2,9', 'floor': 'concrete'}, {'wall': 'butterfly', 'n1': '0,10', 'n2': '1,10', 'floor': 'concrete'}, {'wall': 'butterfly', 'n1': '1,10', 'n2': '2,10', 'floor': 'concrete'}, {'wall': 'butterfly', 'n1': '0,11', 'n2': '1,11', 'floor': 'concrete'}, {'wall': 'butterfly', 'n1': '0,12', 'n2': '1,12', 'floor': 'concrete'}]
