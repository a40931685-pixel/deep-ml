import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	a=np.array(A)
	t=np.array(T)
	s=np.array(S)

	if np.linalg.det(s) ==0:
		return -1
	
	transformed_matrix=np.dot(np.dot(np.linalg.inv(t),a),s).tolist()
	return transformed_matrix