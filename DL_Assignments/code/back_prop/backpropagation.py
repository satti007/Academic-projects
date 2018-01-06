import gzip
import pickle
import random
import argparse
import numpy as np
from net import *
from sklearn.metrics import accuracy_score

# A function for anneal(T/F) argument
def str2bool(v):
	if v.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif v.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')

# Arguments Parser
def get_arguments():
	ap = argparse.ArgumentParser()
	ap.add_argument('--lr', type=float, default=0.01)
	ap.add_argument('--momentum', type=float, default=0.9)
	ap.add_argument('--num_hidden', type=int,default=2)
	ap.add_argument('--sizes', type=str,default='100,100')
	ap.add_argument('--batch_size', type=int, default=1)
	ap.add_argument('--anneal', type=str2bool, default=False)
	ap.add_argument('--loss', type=str, default='ce' , choices =['sq','ce'])
	ap.add_argument('--activation', type=str, default='tanh',choices=['tanh','sigmoid'])
	ap.add_argument('--opt',  type=str, default='adam', choices=['gd', 'momentum', 'nag', 'adam'])
	ap.add_argument('--save_dir', type=str)
	ap.add_argument('--expt_dir', type=str)
	ap.add_argument('--mnist', type=str)

	print '[INFO] Parsing the Arguments...'
	args = vars(ap.parse_args())

	num_hidden = args['num_hidden']
	sizes  = map(int,args['sizes'].split(','))

	if len(sizes) != num_hidden :
		ap.error('len(sizes) is not equal to num of hidden layers')
	if args['batch_size']%5 == 0 or args['batch_size'] == 1 :
		batch_size  = args['batch_size']
	else:
		ap.error('valid values are 1 and multiples of 5')

	lr = args['lr']
	momentum = args['momentum']
	opt = args['opt']
	loss  = args['loss']
	anneal  = args['anneal']
	activation = args['activation']
	save_dir  = args['save_dir']
	expt_dir  = args['expt_dir']
	mnist  = args['mnist']
	print '[INFO] Arguments Parsing Done!'
	print '[INFO] Arguments details: '
	print 'lr,momentum,num_hidden,sizes: ',lr,momentum,num_hidden,sizes
	print 'batch_size,opt,loss,anneal,activation: ',batch_size,opt,loss,anneal,activation
	print 'mnist: ',mnist
	print 'save_dir: ',save_dir
	print 'expt_dir: ',expt_dir

	return lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,mnist

# Reading data
def load_data(mnist):
	print '[INFO] Loaidng the data...'
	with gzip.open(mnist, 'rb') as f:
		train_data, valid_data, test_data = pickle.load(f)
	
	train_x, train_y = train_data
	valid_x, valid_y = valid_data
	test_x, test_y = test_data
	print '[INFO] Training_data details: ',train_x.shape, train_y.shape
	print '[INFO] Validation_data details: ',valid_x.shape, valid_y.shape 
	print '[INFO] Testing_data details: ',test_x.shape, test_y.shape
	print '[INFO] Reading the data Done!'
	
	return train_x, train_y,valid_x, valid_y,test_x, test_y

# Neural net building and weight intilization 
def get_model(sizes,train_x,train_y):
	in_dim = train_x.shape[1]
	out_dim = np.unique(train_y).shape[0]
	print '[INFO] Length of input vector: ', in_dim
	print '[INFO] Length of output vector: ', out_dim
	print '[INFO] Model and weights intilization...'
	sizes.insert(0,in_dim)
	sizes.append(out_dim)
	weights,biases = build_model(sizes)
	print '[INFO] Weights details:'
	for i,j in zip(weights,biases):
		print i.shape,j.shape
	print '[INFO] Weights intilization Done!'
	
	return weights,biases

# get the batch data
def get_batch_data(batch_size):
	indicies = random.sample(range(0,train_x.shape[0]), batch_size) 
	# indicies = [0,1,2,3,4,5,6,7]
	data_X = train_x[indicies]
	data_y = np.zeros((batch_size, 10))
	data_y[np.arange(batch_size), train_y[indicies]] = 1
	
	return data_X,data_y

def get_accuracy(outputs,true_labels,train):
	predictions = np.argmax(outputs,axis=1)
	if train:
		true_labels = np.argmax(true_labels,axis=1)
	# print outputs
	# print true_labels
	return  accuracy_score(true_labels,predictions)


def load_weights(save_dir,state):
	biases  = list(np.load(save_dir+'/biases_{}.npy'.format(state)))
	weights = list(np.load(save_dir+'/weights_{}.npy'.format(state)))
	
	return weights,biases

def save_weights(save_dir,weights,biases,epochs):
	print '[INFO] Model weights saved at {} epochs'.format(epochs)
	np.save(save_dir+'/biases_{}.npy'.format(epochs), biases)
	np.save(save_dir+'/weights_{}.npy'.format(epochs), weights)

def do_predictions(data_X,data_y,weights,biases):
	outputs,temp   = forward_pass(data_X,data_X.shape[0],weights,biases,activation)
	accuracy = get_accuracy(outputs[-1],data_y,False)  
	
	return accuracy

def prev_list_zeros(sizes):
	return 2*[[np.zeros((sizes[index],sizes[index+1])) for index, size in enumerate(sizes) if index != len(sizes)-1],
										 [np.zeros(sizes[index]) for index, size in enumerate(sizes) if index != 0]]

def train(max_epochs,save_dir,weights,biases,opt,lr,anneal,sizes):
	epochs = 0
	if anneal:
		anneal_valid_accuracy = 0
	prev_list = prev_list_zeros(sizes)
	while(epochs < max_epochs):
		for step in range(0,train_x.shape[0]/batch_size): 		
			data_X, data_y = get_batch_data(batch_size)
			layer_outputs,local_grads = forward_pass(data_X,batch_size,weights,biases,activation)
			train_accuracy  = get_accuracy(layer_outputs[-1],data_y,True)
			error, output_grad = get_loss(loss,layer_outputs[-1],data_y,batch_size)
			if opt == 'nag':
				weights_m = [i+momentum*j for i,j in zip(weights,prev_list[0])]
				gradients = back_prop(output_grad,local_grads,weights_m)
			else:
				gradients = back_prop(output_grad,local_grads,weights)
			weights,biases,prev_list =  weights_update(weights,biases,layer_outputs,gradients,sizes,batch_size,opt,lr,prev_list,momentum)
			if step%100 == 0:
				print '[INFO] Epoch {}, Step {}, Loss: {}, train_accuracy: {}'.format(epochs,step,error,train_accuracy)
		valid_accuracy = do_predictions(valid_x,valid_y,weights,biases)
		print '[INFO] Validation_accuracy at {} epochs is {}'.format(epochs,valid_accuracy)
		if anneal:
			if valid_accuracy < anneal_valid_accuracy:
				lr = lr*0.5
				weights,biases = load_weights(save_dir,epochs-1)
				print '[INFO] learning_rate annealed to half, lr: {}'.format(lr)
				continue
			anneal_valid_accuracy = valid_accuracy
		save_weights(save_dir,weights,biases,epochs)
		epochs = epochs + 1
	print do_predictions(test_x,test_y,weights,biases)

lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,mnist = get_arguments()
train_x, train_y,valid_x, valid_y,test_x, test_y = load_data(mnist)
weights,biases = get_model(sizes,train_x,train_y)
max_epochs = 100
print '[INFO] Model training started...'
train(max_epochs,save_dir,weights,biases,opt,lr,anneal,sizes)
print '[INFO] Model training done!'

	
# Testing model by overfitting on small dataset
'''
def test_run(weights,biases,momentum,opt):
	batch_size = 8
	data_X, data_y = get_batch_data(batch_size)
	prev_list = prev_list_zeros(sizes)	
	iter = 0
	while(True):
		layer_outputs,local_grads = forward_pass(data_X,batch_size,weights,biases,activation)
		train_accuracy  = get_accuracy(layer_outputs[-1],data_y,True)
		error, output_grad = get_loss(loss,layer_outputs[-1],data_y,batch_size)
		print iter,error,train_accuracy
		if opt == 'nag':
			weights_1 = [i+momentum*j for i,j in zip(weights,prev_list[0])]
			gradients = back_prop(output_grad,local_grads,weights_1)
		else:
			gradients = back_prop(output_grad,local_grads,weights)
		weights,biases,prev_list =  weights_update(weights,biases,layer_outputs,gradients,sizes,batch_size,
													opt,lr,prev_list,momentum)

		# if opt == 'gd':
		# 	weights, biases =  weights_update_gd(weights,biases,layer_outputs,gradients,lr,opt,sizes,batch_size)
		# elif opt == 'momentum' or opt == 'nag':
		# 	weights,biases,prev_mu_weights,prev_mu_biases =  weights_update_mu(weights,biases,layer_outputs,gradients,lr,
		# 												opt,sizes,batch_size,momentum,prev_mu_weights,prev_mu_biases)
		# elif opt == 'adam':
		# 	weights,biases,prev_m_weights,prev_m_biases,prev_v_weights,prev_v_biases = weights_update_adam(weights,biases,layer_outputs,gradients,lr,
		# 																opt,sizes,batch_size,prev_m_weights,prev_m_biases,prev_v_weights,prev_v_biases,
		# 																momentum)
		iter = iter +1 

test_run(weights,biases,momentum,opt)
'''













# Different way of training(w.r.t iterations, train/test and other several options)
'''
def train(max_iters,weights_path,weights,biases,restore,state=None):
	iters = 1
	if restore:
		weights,biases = load_weights(weights_path,state)
	while(iters < max_iters+1):
		data_X, data_y = get_batch_data(batch_size)
		layer_outputs,local_grads = forward_pass(data_X,batch_size,weights,biases,activation)
		train_accuracy  = get_accuracy(layer_outputs[-1],data_y,True)
		if iters%50 == 0:
			save_weights(weights_path,weights,biases,iters)
			valid_accuracy = do_predictions(valid_x,valid_y,weights,biases)
		error, output_grad = get_loss(loss,layer_outputs[-1],data_y,batch_size)
		print error,train_accuracy
		gradients = back_prop(output_grad,local_grads,weights)
		weights, biases =  weights_update(weights,biases,layer_outputs,gradients,lr,opt,sizes,batch_size)
		iters = iters + 1
	print do_predictions(test_x,test_y,weights,biases)

lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,mnist = get_arguments()
train_x, train_y,valid_x, valid_y,test_x, test_y = load_data(mnist)
weights,biases = get_model(sizes,train_x,train_y)
mode = raw_input('Enter the mode(train/test):  ')
if mode == 'train':
	training = True
else:
	training = False
weights_path = save_dir
if training:
	max_iters = int(raw_input('Enter no.of.max_iters: '))
	restore = str2bool(raw_input('Restore model(T/F): '))
	if restore:
		state = int(raw_input('Enter the state of restoring: '))
		train(max_iters,weights_path,weights,biases,restore,state)
	else:
		train(max_iters,weights_path,weights,biases,restore)
else:
	state = int(raw_input('Enter the state of restoring: '))
	weights,biases = load_weights(weights_path,state)
	print do_predictions(test_x,test_y,weights,biases)
'''
'''
def train(max_epochs,save_dir,weights,biases,opt,lr,anneal,sizes):
	epochs = 1
	if anneal:
		anneal_valid_accuracy = 0
	if opt == 'momentum' or opt == 'nag': 
		prev_mu_weights = [np.zeros((sizes[index],sizes[index+1])) for index, size in enumerate(sizes) if index != len(sizes)-1]
		prev_mu_biases  = [np.zeros(sizes[index]) for index, size in enumerate(sizes) if index != 0]
	if opt == 'adam':
		prev_m_weights = [np.zeros((sizes[index],sizes[index+1])) for index, size in enumerate(sizes) if index != len(sizes)-1]
		prev_m_biases  = [np.zeros(sizes[index]) for index, size in enumerate(sizes) if index != 0]
		prev_v_weights = prev_m_weights
		prev_v_biases  = prev_m_biases
	while(epochs < max_epochs+1):
		for step in range(0,train_x.shape[0]/batch_size): 		
			data_X, data_y = get_batch_data(batch_size)
			layer_outputs,local_grads = forward_pass(data_X,batch_size,weights,biases,activation)
			train_accuracy  = get_accuracy(layer_outputs[-1],data_y,True)
			error, output_grad = get_loss(loss,layer_outputs[-1],data_y,batch_size)
			if opt == 'nag':
				weights_1 = [i+momentum*j for i,j in zip(weights,prev_mu_weights)]
				gradients = back_prop(output_grad,local_grads,weights_1)
			else:
				gradients = back_prop(output_grad,local_grads,weights)
			if opt == 'gd':
				weights, biases =  weights_update_gd(weights,biases,layer_outputs,gradients,lr,opt,sizes,batch_size)
			elif opt == 'momentum':
				weights,biases,prev_mu_weights,prev_mu_biases =  weights_update_mu(weights,biases,layer_outputs,gradients,lr,
															opt,sizes,batch_size,momentum,prev_mu_weights,prev_mu_biases)
			elif opt == 'adam':
				weights,biases,prev_m_weights,prev_m_biases,prev_v_weights,prev_v_biases = weights_update_adam(weights,biases,
																				layer_outputs,gradients,lr,opt,sizes,batch_size,
															prev_m_weights,prev_m_biases,prev_v_weights,prev_v_biases,momentum)
			if step%100 == 0:
				print '[INFO] Epoch {}, Step {}, Loss: {}, train_accuracy: {}'.format(epochs,step,error,train_accuracy)
		save_weights(save_dir,weights,biases,epochs)
		valid_accuracy = do_predictions(valid_x,valid_y,weights,biases)
		if anneal:
			if valid_accuracy < anneal_valid_accuracy:
				lr = lr*0.5
				print '[INFO] learning_rate annealed to half'
				continue
			anneal_valid_accuracy = valid_accuracy
		print '[INFO] Validation_accuracy at {} epochs is {}'.format(epochs,valid_accuracy)
		epochs = epochs + 1
	print do_predictions(test_x,test_y,weights,biases)
'''