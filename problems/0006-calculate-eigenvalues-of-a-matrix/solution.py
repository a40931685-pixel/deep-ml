import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	matrix=np.array(matrix)
	x=matrix[0][0]+matrix[1][1]
	y=(matrix[0][0] * matrix[1][1])-matrix[0][1]*matrix[1][0]
	e=[]
	h=(x-np.emath.sqrt((x**2)-4*y))/2
	k=(x+np.emath.sqrt((x**2)-4*y))/2
	h=float(h)
	k=float(k)
	e=sorted([h,k],reverse=True)

	return e