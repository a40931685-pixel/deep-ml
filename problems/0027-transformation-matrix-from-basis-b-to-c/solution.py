import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:

	c=np.linalg.inv(C)
	P=np.dot(c,B)

	return P