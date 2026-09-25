import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	
	for i in range(0,len(X),batch_size):
		end_index=min(len(X),i+batch_size)

		if y is None:
			yield (X[i:end_index].tolist())
		else:
			yield [X[i:end_index].tolist() , y[i:end_index].tolist()]
	
	pass