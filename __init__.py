import numpy as np
import nn

float32 = np.float32
int32 = np.int32
float64 = np.float64
int64 = np.int64

class Operation(object):
	def __init__(self,inputs = []):
		self.input_nodes = inputs

		for node in self.input_nodes:
			_default_graph.Operation.append(node)


class add(Operation):
	def __init__(self,x,y):
		super().__init__([x,y])

	def compute(x,y):
		return x + y


class multiply():
	def __init__(self,x,y):
		super().__init__([x,y])
	def compute(x,y):
		return x * y


class matmul():
	def __init__(self,x,y):
		super().__init__([x,y])
	def compute(x,y):
		return x.dot(y)

class substract():
	def __init__(self,x,y):
		super().__init__([x,y])
	def compute(x,y):
		return x - y

def postorder_traversal(node):
	node_postorder = []
	def recurse(node):
		if isinstance(node,Operation):
		  for input_node in node.input_nodes:
		    recurse(input_node)
		node_postorder.append(node)

	recurse(operation)
	return node_postorder


class Session():
	def __init__(self,graph=None):
		if graph == None:
			pass
		else:
			self.graph = _default_graph

	def run():
		postorder_traversal  = postorder_traversal(operation)
		node_postorder = traverse_postorder(operation)
		for node in node_postorder:
			print(dir(node))
			if type(node) == Placeholder:
				node.output = node.dtype(feed_dict[node])
	        
			elif type(node) == Variable:
				node.output = node.value
			else:
				node.inputs = [input_node.output for input_node in node.input_nodes]
				node.output = node.compute(*node.inputs)
	       
			if type(node.output) == list:
				node.output = np.array(node.output)
		return operation.output

	def __enter__(self):
		return self

	def __exit__(self,type,a,b):
		pass


class Variable():
	def __init__(self,value,dtype=None):
		if dtype == None:
			dtype = do_tagging(value)
		else:
			value,base_class = do_tagging(value)
			if isinstance(dtype(),base_class):
				value = dtype(value)
			else:
				raise TypeError("Type mismathc")

		self.value = value
		_default_graph.Variable.append(self)
			
def do_tagging(value):
	if isinstance(value,int):
		return np.int32(value),np.signedinteger
	if isinstance(value,float):
		return np.float32(value),np.floating

class constant():
	def __init__(self,value,dtype=None):
		if dtype == None:
			dtype = do_tagging(value)
		else:
			value,base_class = do_tagging(value)
			if isinstance(dtype(),base_class):
				value = dtype(value)
		self.value  = value
		_default_graph.constant.append(self)

	def set_value():
		raise Exception("It is immutable")

	def get_value():
		return self.value

	value = property(get_value,set_value)


class Placholder():
	def __init__(self,dtype=None):
		self.dtype = dtype
		_default_graph.Placholder.append(self)

	def get_dtype():
		return self.dtype

class Graph():
	def __init__(self):
		self.Variable = []
		self.Placholder = []
		self.Operation = []

	def get_tensor_by_name(var_scope):
		pass

	def as_default(self):
		global _default_graph
		_default_graph = self

