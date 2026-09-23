import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean=np.mean(data,axis=0)
	s=np.std(data, axis=0)
	d1=(data-mean)/s
	d1=np.round(d1,4)
	M=np.max(data,axis=0)
	minn=np.min(data,axis=0)
	d2=(data-minn)/(M-minn)
	d2=np.round(d2,4)
	return d1, d2