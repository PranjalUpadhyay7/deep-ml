import numpy as np

def to_categorical(x, n_col=None):
	unique=list(set(x))
	redundant=0
	n=len(unique)
	if not n_col:
		n_col=n
	elif n_col-n>0:
		redundant=n_col-n
	ans=[]
	for data in x:
		value=[0]*n_col
		index=unique.index(data)
		value[index+redundant]=1
		ans.append(value)
	return ans

	# Your code here
	# pass