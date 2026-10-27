def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	if mode=="row":
		means=np.array(matrix).mean(axis=1)
	elif mode =="column":
		means=np.array(matrix).mean(axis=0)


	return means