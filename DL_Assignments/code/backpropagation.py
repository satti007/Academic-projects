import gzip
import pickle
import argparse
import numpy as np
from net import *

# A function for anneal(T/F) argument
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Arguments Parser
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

print '[INFO] Arguments details: ',lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,mnist
if anneal:
	print 'anneal--true'

# Reading data
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

# Getting the dimensions of input and output
in_dim = train_x.shape[1]
out_dim = np.unique(train_y).shape[0]
print '[INFO] Length of input vector: ', in_dim
print '[INFO] Length of output vector: ', out_dim

# Neural net building and weight intilization 
print '[INFO] Model and weights intilization...'
sizes.insert(0,in_dim)
sizes.append(out_dim)
weights,biases = build_model(sizes)

print '[INFO] Weights details:'
for i,j in zip(weights,biases):
	print i.shape,j.shape
print '[INFO] Weights intilization Done!'

data_X = train_x[0:batch_size]
data_y = np.zeros((batch_size, 10))
data_y[np.arange(batch_size), train_y[0:batch_size]] = 1

outputs,local_grads_weights,local_grads_biases = forward_pass(data_X,batch_size,weights,biases,activation)
# print outputs
error, output_grad = get_loss(loss,outputs,data_y,batch_size)
print error, output_grad.shape

grads_weights,grads_biases = back_prop(output_grad,local_grads_weights,local_grads_biases,weights,sizes)


# weight_grads = evaluate_grad(loss W_in,W_hid,b_hid,W_out,b_out)