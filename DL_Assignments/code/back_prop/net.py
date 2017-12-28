import numpy as np
np.random.seed(1234)

# Xavier weight intilization
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
	local_grads   = []
	layer_inputs.append(data_X)
	for index,layer_weights in enumerate(weights):
		output = np.dot(layer_inputs[index],layer_weights) +  np.repeat(biases[index],batch_size).reshape(batch_size,biases[index].shape[0])
		if activ_fun == 'sigmoid':
			output = sigmoid(output)
			local_grads.append(sigmoid_diff(output))
		else:
			output = Tanh(output)
			local_grads.append(Tanh_diff(output))
		layer_inputs.append(output)
		
	return layer_inputs,local_grads


def get_loss(loss,outputs,data_y,batch_size):
	if loss == 'sq':
		error = np.sum(np.square(data_y - outputs))/float(batch_size)
		output_grad = outputs - data_y
	
	return error, output_grad


def back_prop(output_grad,local_grads,weights):
	gradients = []
	weights.reverse()
	local_grads.reverse()
	gradients.append(np.multiply(output_grad,local_grads[0]))
	for index,W in enumerate(weights):
		if index != len(weights)-1:
			temp = np.dot(gradients[index],W.T)
			gradients.append(np.multiply(temp,local_grads[index+1]))
	weights.reverse()
	local_grads.reverse()
	gradients.reverse()
	
	return gradients

def weights_update(weights,biases,layer_outputs,gradients,lr,opt,sizes,batch_size):
	index = 0
	for grads,W,B,inputs in zip(gradients,weights,biases,layer_outputs):
		inputs_mat = np.vstack([np.tile(inputs[row],sizes[index+1]).reshape(sizes[index+1],sizes[index]).T for row in range(batch_size)])
		grads_mat  = np.vstack([np.tile(grads[row],sizes[index]).reshape(sizes[index],sizes[index+1]) for row in range(batch_size)])
		batch_mat  = np.multiply(inputs_mat,grads_mat)
		delta_weights  = sum([batch_mat[sizes[index]*j:sizes[index]*(j+1)] for j in range(batch_size)])  
		delta_biases   = np.sum(grads,axis=0)
		W = np.subtract(W,lr*delta_weights)
		B = np.subtract(B,lr*delta_biases) 
		weights[index] = W
		biases[index] = B
		index = index + 1
		
	return weights,biases

