import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	sum=0
	x=0
	for i in range(len(y_true)):
		sum+=(np.dot(w,X[i])-y_true[i])**2
	for j in range(len(w)):
		x+=(w[j])**2
	return np.round(sum/len(y_true)+alpha*x,3)
	pass
