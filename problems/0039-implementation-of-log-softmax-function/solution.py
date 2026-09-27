import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	x=np.array(scores)
	array=np.zeros(len(x))
	sum=0
	for i in range(len(x)):
		sum+=(np.exp(x[i]-np.max(x)))
	for i in range(len(x)):
		array[i]=x[i]-np.max(x)-np.log(sum)

	return array
	pass