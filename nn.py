import numpy as np

def Sigmoid(expr):
	return 1 / (1 + np.exp(-expr))

def Relu(expr):
	return np.max(0,expr)