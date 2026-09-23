import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	X=np.array(X)
	y=np.array(y)
	if seed is not 	None:
		np.random.seed(seed)
	s=np.random.permutation(len(X))
	return X[s] ,y[s]
	pass