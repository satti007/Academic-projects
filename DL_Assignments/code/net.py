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

def eval_local_grads(data,activ_diff,batch_size):
	grads = [np.dot(data[index].reshape(data[index].shape[0],1),activ_diff[index].reshape(1,activ_diff[index].shape[0])) for index in range(batch_size)]
	
	return grads

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
			local_grads_weights.append(eval_local_grads(layer_inputs[index],sigmoid_diff(output),batch_size))
		else:
			output = Tanh(output)
			local_grads_biases.append(Tanh_diff(output))
			local_grads_weights.append(eval_local_grads(layer_inputs[index],Tanh_diff(output),batch_size))
		layer_inputs.append(output)
		
	return layer_inputs[-1],local_grads_weights,local_grads_biases


def get_loss(loss,outputs,data_y,batch_size):
	if loss == 'sq':
		error = np.sum(np.square(data_y - outputs))/float(batch_size)
		output_grad = outputs - data_y
	
	return error, output_grad


def eval_grads(local_grads,output_grad,batch_size):
	A = np.vstack([i for i in local_grads])
	B = np.vstack([np.tile(output_grad[i], (local_grads[0].shape[0],1)) for i in range(0,output_grad.shape[0])])
	C = np.multiply(A,B)
	D = sum([C[local_grads[0].shape[0]*i:local_grads[0].shape[0]*(i+1)] for i in range(0,batch_size)])
	
	return D


def back_prop(output_grad,local_grads_weights,local_grads_biases,weights):
	grads_biases = []
	grads_weights = []
	weights.reverse()
	local_grads_biases.reverse()
	local_grads_weights.reverse()
	for i,j,k in zip(local_grads_weights,local_grads_biases,weights):
		grads_biases.append(np.sum(np.multiply(np.vstack([bias for bias in j]),output_grad),axis=0))
		grads_weights.append(eval_grads(i,output_grad,batch_size))



return grads_weights,grads_biases

# def weights_update():