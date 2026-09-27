import numpy as np

def make_diagonal(x):
	# Your code here
	
	y=np.zeros((len(x),len(x)))
	for i in range(len(x)):
		
		y[i][i]=x[i]
	return y

	pass

