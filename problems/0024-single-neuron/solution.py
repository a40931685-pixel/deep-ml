import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	features=np.array(features)
	weights=np.array(weights)
	labels=np.array(labels)
	z=np.dot(features,weights)+bias
	pred=1/(1+np.exp(-z))
	errors=(pred-labels)**2
	mse=np.mean(errors)
	mse=np.round(float(mse),4)
	pred=[np.round(float(p),4)for p in pred]
	return pred, mse