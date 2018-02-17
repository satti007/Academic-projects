import random
import argparse
import numpy as np
import pandas as pd
from net import *
import numpy as np
np.random.seed(1234)

param_file = open('log_params_exp.txt','a')

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
	ap.add_argument('--activation', type=str, default='tanh',choices=['tanh','sigmoid','relu'])
	ap.add_argument('--opt',  type=str, default='adam', choices=['gd', 'momentum', 'nag', 'adam'])
	ap.add_argument('--save_dir', type=str)
	ap.add_argument('--expt_dir', type=str)
	ap.add_argument('--train', type=str)
	ap.add_argument('--val', type=str)
	ap.add_argument('--test', type=str)
	
	print '[INFO] Parsing the Arguments...'
	param_file.write('[INFO] Parsing the Arguments...\n')
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
	train = args['train']
	valid = args['val']
	test  = args['test']
	print '[INFO] Arguments Parsing Done!'
	param_file.write('[INFO] Arguments Parsing Done!\n')
	print '[INFO] Arguments details: '
	param_file.write('[INFO] Arguments details: \n')
	print 'lr,momentum,num_hidden,sizes: ',lr,momentum,num_hidden,sizes
	param_file.write('lr,momentum,num_hidden,sizes: {} {} {} {} \n'.format(lr,momentum,num_hidden,sizes))
	print 'batch_size,opt,loss,anneal,activation: ',batch_size,opt,loss,anneal,activation
	param_file.write('batch_size,opt,loss,anneal,activation: {} {} {} {} {} \n'.format(batch_size,opt,loss,anneal,activation))
	print 'train: ',train
	param_file.write('train: {} \n'.format(train))
	print 'train: ',valid
	param_file.write('valid: {} \n'.format(valid))
	print 'test: ',test
	param_file.write('test: {} \n'.format(test))
	print 'save_dir: ',save_dir
	param_file.write('save_dir: {} \n'.format(save_dir))
	print 'expt_dir: ',expt_dir
	param_file.write('expt_dir: {} \n'.format(expt_dir))
	
	return lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,train,valid,test

# Reading data
def load_data(train,valid,test):
	print '[INFO] Loaidng the data...'
	param_file.write('[INFO] Loaidng the data...\n')
	train_data = pd.read_csv(train).as_matrix()
	valid_data = pd.read_csv(valid).as_matrix()
	test_data = pd.read_csv(test).as_matrix()			
	train_x, train_y = train_data[:,1:785], train_data[:,785]
	valid_x, valid_y = valid_data[:,1:785], valid_data[:,785]
	test_x = test_data[:,1:785]
	print '[INFO] Training_data details: ',train_x.shape, train_y.shape
	param_file.write('[INFO] Training_data details: {} {} \n '.format(train_x.shape, train_y.shape))
	print '[INFO] Validation_data details: ',valid_x.shape, valid_y.shape
	param_file.write('Validation_data details: {} {} \n'.format(valid_x.shape, valid_y.shape))
	print '[INFO] Testing_data details: ',test_x.shape
	param_file.write('Testing_data details: {} \n'.format(test_x.shape))
	print '[INFO] Reading the data Done!'
	param_file.write('[INFO] Reading the data Done!\n')
	
	return train_x/255.0, train_y,valid_x/255.0, valid_y,test_x/255.0

# Neural net building and weight intilization 
def get_model(sizes,train_x,train_y):
	in_dim = train_x.shape[1]
	out_dim = 10
	print '[INFO] Length of input vector: ', in_dim
	param_file.write('[INFO] Length of input vector: {}\n'.format(in_dim))
	print '[INFO] Length of output vector: ', out_dim
	param_file.write('[INFO] Length of output vector: {}\n '.format(out_dim))
	print '[INFO] Model and weights intilization...'
	param_file.write('[INFO] Model and weights intilization...\n')
	sizes.insert(0,in_dim)
	sizes.append(out_dim)
	weights,biases = build_model(sizes)
	print '[INFO] Weights details:'
	param_file.write('[INFO] Weights details:\n')
	for i,j in zip(weights,biases):
		print i.shape,j.shape
	print '[INFO] Weights intilization Done!'
	param_file.write('[INFO] Weights intilization Done!\n')
	
	return weights,biases

# get the batch data
def get_batch_data(batch_size):
	indicies = random.sample(range(0,train_x.shape[0]), batch_size) 
	data_X = train_x[indicies]
	data_y = np.zeros((batch_size, 10))
	data_y[np.arange(batch_size), train_y[indicies]] = 1
	
	return data_X,data_y

def get_accuracy(outputs,true_labels,train):
	predictions = np.argmax(outputs,axis=1)
	if train:
		true_labels = np.argmax(true_labels,axis=1)
	return np.count_nonzero(predictions == true_labels)/float(predictions.shape[0])

def load_weights(save_dir,state):
	biases  = list(np.load(save_dir+'/biases_{}.npy'.format(state)))
	weights = list(np.load(save_dir+'/weights_{}.npy'.format(state)))
	print '[INFO] Model restored at {} Epoch'.format(state)
	# param_file.write('[INFO] Model restored at {} Epoch\n'.format(state))
	
	return weights,biases

def save_weights(save_dir,weights,biases,epochs):
	print '[INFO] Model weights saved at {} epochs'.format(epochs)
	param_file.write('[INFO] Model weights saved at {} epochs\n'.format(epochs))
	np.save(save_dir+'/biases_{}.npy'.format(epochs), biases)
	np.save(save_dir+'/weights_{}.npy'.format(epochs), weights)

def do_predictions(data_X,data_y,weights,biases,train):
	Loss = 0.0
	accuracy = 0.0
	batches = data_X.shape[0]/10
	for i in range (batches):
		data_x, labels = data_X[10*i:10*(i+1),:],data_y[10*i:10*(i+1)]
		data_Y = np.zeros((10, 10)) 
		data_Y[np.arange(10), labels[0:10]] = 1
		outputs,temp   = forward_pass(data_x,10,weights,biases,activation,False,data_Y)
		error, temp = get_loss(loss,outputs[-1],data_Y,10,weights)
		Loss += error
		accuracy += get_accuracy(outputs[-1],labels,train)  
		
	return Loss/batches,accuracy/batches

def do_test(test_x,weights,biases):
	outputs,temp   = forward_pass(test_x,test_x.shape[0],weights,biases,activation,False)
	predictions = np.argmax(outputs[-1],axis=1)
	sub = pd.read_csv('../data/sample_sub.csv')
	sub['label'] = predictions
	sub.to_csv('../data/submission_check.csv',index = False)

def prev_list_zeros(sizes):
	return 2*[[np.zeros((sizes[index],sizes[index+1])) for index, size in enumerate(sizes) if index != len(sizes)-1],
										 [np.zeros(sizes[index]) for index, size in enumerate(sizes) if index != 0]]

def do_train(max_epochs,save_dir,weights,biases,opt,lr,anneal,sizes):
	epochs = 0
	updates = 0
	if anneal:
		anneal_valid_accuracy = 0
	anneal_times = 0
	anneal_list = prev_list_zeros(sizes) 
	prev_list = prev_list_zeros(sizes)
	while(epochs < max_epochs and anneal_times < 6):
		for step in range(0,train_x.shape[0]/batch_size): 		
			data_X, data_y = get_batch_data(batch_size)
			if opt == 'nag':
				weights = [i+momentum*j for i,j in zip(weights,prev_list[0])]
			layer_outputs,local_grads = forward_pass(data_X,batch_size,weights,biases,activation,True,data_y)
			error, output_grad = get_loss(loss,layer_outputs[-1],data_y,batch_size,weights)
			gradients = back_prop(output_grad,local_grads,weights)
			weights,biases,prev_list,anneal_list = weights_update(weights,biases,layer_outputs,gradients,sizes,batch_size,opt,lr,prev_list,anneal_list,momentum,epochs*step+1)
			if step%500 == 0:
				train_loss,train_accuracy = do_predictions(train_x,train_y,weights,biases,False)
				print 'Epoch {}, Step {}, Loss: {}, Error: {} lr:{}'.format(epochs,step,round(train_loss,5),round(train_accuracy*100,2),lr)
				train_file.write('Epoch {}, Step {}, Loss: {}, Error: {}, lr:{}\n'.format(epochs,step,round(train_loss,5),round((1-train_accuracy)*100,2),lr))
				valid_loss,valid_accuracy = do_predictions(valid_x,valid_y,weights,biases,False)
				print '[INFO] Epoch {}, Step {}, Loss: {}, Error: {}, lr:{}'.format(epochs,step,round(valid_loss,5),round(valid_accuracy*100,2),lr)
				val_file.write('Epoch {}, Step {}, Loss: {}, Error: {}, lr:{}\n'.format(epochs,step,round(valid_loss,5),round((1-valid_accuracy)*100,2),lr))
		if anneal:
			if valid_accuracy < anneal_valid_accuracy:
				lr = lr*0.8
				prev_list = anneal_list
				anneal_times = anneal_times + 1
				weights,biases = load_weights(save_dir,epochs-1)
				print '[INFO] learning_rate annealed to half, lr: {}'.format(lr)
				param_file.write('[INFO] learning_rate annealed to half, lr: {}\n'.format(lr))
				continue
			else:
				anneal_times = 0
				anneal_valid_accuracy = valid_accuracy
		save_weights(save_dir,weights,biases,epochs)
		epochs = epochs + 1
	
	return weights,biases,epochs
try:
	lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,train,valid,test = get_arguments()
	train_file = open(expt_dir+"/log_train.txt","w") 
	val_file   = open(expt_dir+"/log_val.txt","w") 
	train_x,train_y,valid_x,valid_y,test_x = load_data(train,valid,test)
	weights,biases = get_model(sizes,train_x,train_y)
	max_epochs = 20
	print '[INFO] Model training started...'
	param_file.write('[INFO] Model training started...\n')
	weights,biases,epochs =  do_train(max_epochs,save_dir,weights,biases,opt,lr,anneal,sizes)
	print '[INFO] Model training done!'
	param_file.write('[INFO] Model training done!\n')
	param_file.write('\n')
except KeyboardInterrupt: 
	train_file.close()
	val_file.close()
	param_file.close()