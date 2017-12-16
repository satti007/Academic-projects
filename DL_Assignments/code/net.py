import random
import numpy as np

def build_model(sizes):
	weights = [np.random.randn(sizes[index],sizes[index+1]) * np.sqrt(1.0/sizes[index]) for index, size in enumerate(sizes) if index != len(sizes)-1]
	biases  = [np.zeros(sizes[index]) for index, size in enumerate(sizes) if index != 0]
	
	return weights,biases

def sigmoid(x):
	return 1 / (1 + np.exp(-x)) 

def sigmoid_diff(x):
	sig_x = sigmoid(x)	
	return np.multiply(sig_x,np.subtract(1.0, sig_x))

def Tanh(x):
	return np.tanh(x)

def Tanh_diff(x):
	tanh_x = Tanh(x)
	return np.subtract(1.0,np.square(tanh_x))

def forward_pass(data_X,batch_size,weights,biases,activ_fun):
	layer_inputs  = []
	local_grads_biases  = []
	local_grads_weights = []
	layer_inputs.append(data_X)
	for index,layer_weights in enumerate(weights):
		output = np.dot(layer_inputs[index],layer_weights) +  np.repeat(biases[index],batch_size).reshape(batch_size,biases[index].shape[0])
		if activ_fun == 'sigmoid':
			output = sigmoid(output)
			local_grads_biases.append(sigmoid_diff(output))
			local_grads_weights.append(np.multiply(layer_inputs[index],sigmoid_diff(output)))
		else:
			output = Tanh(output)
			local_grads_biases.append(Tanh_diff(output))
			local_grads_weights.append(np.multiply(layer_inputs[index],Tanh_diff(output)))
		layer_inputs.append(output)
	
	return layer_inputs[-1],local_grads_weights,local_grads_biases





def build_model(sizes):
	weights = [np.ones((sizes[index],sizes[index+1])) for index, size in enumerate(sizes) if index != len(sizes)-1]
	biases  = [np.ones(sizes[index]) for index, size in enumerate(sizes) if index != 0]
	
	return weights,biases




# def loss():

# def back_prop():

# def weights_update():





