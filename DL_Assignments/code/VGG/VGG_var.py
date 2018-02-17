import os
import random
import numpy as np
import tensorflow as tf
from VGG_data_prep import load_data
from tensorflow.python.framework.graph_util import convert_variables_to_constants

np.random.seed(1234)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def conv2d(input_layer,filters,ksize,stride,padding,scope):
	with tf.variable_scope(scope) as scope:
		return tf.contrib.layers.convolution2d(inputs=input_layer,num_outputs=filters,
								 kernel_size=ksize,stride=stride,padding=padding,scope=scope)

def max_pool2d(input_layer,ksize,stride):
	return tf.contrib.layers.max_pool2d(inputs=input_layer,kernel_size=ksize,stride=stride,padding='VALID')

def FC(input_layer,neurons,scope):
	with tf.variable_scope(scope) as scope:
		return tf.contrib.layers.fully_connected(inputs=input_layer,num_outputs=neurons,scope=scope)

def softmax(input_layer,neurons,scope,is_training_mode):
	with tf.variable_scope(scope) as scope:
		return tf.contrib.layers.fully_connected(inputs=input_layer,num_outputs=neurons,activation_fn=None,
						normalizer_fn=tf.contrib.layers.batch_norm,normalizer_params={'is_training': is_training_mode},scope=scope)

def model(x,is_training_mode):
	with tf.contrib.slim.arg_scope([tf.contrib.slim.model_variable, tf.contrib.slim.variable]):
		
		# TODO: Convlayer: input = 32,32,3  output = 32,32,64
		layer_1 = conv2d(x,64,3,1,'SAME','conv1')
		
		# TODO: poollayer: input = 32,32,64  output = 16,16,64
		pool_1 = max_pool2d(layer_1,2,2)
		
		# TODO: Convlayer: input = 16,16,64 output = 16,16,128
		layer_2 = conv2d(pool_1,128,3,1,'SAME','conv2')        
		
		# TODO: poollayer: input = 16,16,128  output = 8,8,128
		pool_2 = max_pool2d(layer_2,2,2)
		
		# TODO: Convlayer: input = 8,8,128  output = 8,8,256
		layer_3 = conv2d(pool_2,256,3,1,'SAME','conv3')
		
		# TODO: Convlayer: input = 8,8,256  output = 8,8,256
		layer_4 = conv2d(layer_3,256,3,1,'SAME','conv4')
		
		# TODO: poollayer: input = 8,8,256  output = 4,4,256
		pool_3 = max_pool2d(layer_4,2,2)
		
		# TODO: poollayer: input = 4,4,256  output = 4096
		layer_f = tf.contrib.layers.flatten(pool_3)
		
		# TODO: FC layer: input = 4096 output = 1024
		layer_5 = FC(layer_f,1024,'fc5')
		
		# TODO: FC layer: input = 1024  output = 1024
		layer_6 = FC(layer_5,1024,'fc6')
		
		# TODO: FC layer: input = 1024  output = 10
		logits = softmax(layer_6,10,'fc7',is_training_mode)
		
		y = tf.nn.softmax(logits,name='output_node')
		
		return logits,y

def get_batch_data(batch_size,isTrain):
	if isTrain:
		data_X = train_X
		data_y = train_y
	else:
		data_X = valid_X
		data_y = valid_y
	batch_size = 8
	indicies = [0,1,2,3,4,5,6,7]
	# indicies = random.sample(range(0,data_X.shape[0]), batch_size) 
	xs = data_X[indicies]
	ys = np.zeros((batch_size, 10))
	ys[np.arange(batch_size), data_y[indicies]] = 1
	
	return xs,ys

def save_weights(iters):
	Wts = [p.eval(session=sess) for p in tf.trainable_variables()]
	np.savez("weights/VGG_weights_"+str(iters)+".npz", *Wts) 

def save_pb():
	minimal_graph = convert_variables_to_constants(sess, sess.graph_def,["output_node"])
	tf.train.write_graph(minimal_graph, '.','VGG_var.pb', as_text=False)

def load_weights(iters):
	f = np.load("weights/VGG_weights_"+str(iters)+".npz")
	initial_weights = [f[p] for p in sorted(f.files,key=lambda s: int(s[4:]))]
	assign_ops = [w.assign(v) for w, v in zip(tf.trainable_variables(), initial_weights)]
	sess.run(tf.global_variables_initializer())
	sess.run(assign_ops)

def accuracy(y,y_,iters):
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	print sess.run(correct_prediction)
	acc = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	print "step %d validation accuracy %g" % (iters,sess.run(acc))

x  = tf.placeholder(tf.float32, [None,32,32,3], name='input_node')
y_ = tf.placeholder("float",shape=[None,10])
is_training_mode = tf.placeholder(tf.bool,name='is_training_mode')
logits,y = model(x,is_training_mode)
cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_))
train_step = tf.train.AdamOptimizer(1e-3).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


def train(load=None,state=None):
	if(load):
		load_weights(state)
	try:
		iters = 0
		while True:
			iters += 1
			xs,ys = get_batch_data(batch_size,True)
			# print sess.run(logits,feed_dict={x:xs,is_training_mode:True})
			sess.run(train_step, feed_dict={x:xs,y_:ys,is_training_mode:True})
			if iters % 5 == 0:
				loss=sess.run(cross_entropy,feed_dict={x:xs,y_:ys,is_training_mode:True})
				print "step %d training loss %g" % (iters,loss)
				pred=sess.run(y,feed_dict={x:xs,is_training_mode:False})
			 	accuracy(pred.reshape(8,10),ys,iters)
			
			# if iters % 500 == 0:
			# 	xs,ys = get_batch_data(500,False)
			# 	pred=sess.run(y,feed_dict={x:xs})
			# 	accuracy(pred.reshape(500,2),ys,iters)
			# 	save_weights(iters)
			# 	save_pb()
	except KeyboardInterrupt: 
		# save_weights(iters)
		save_pb()

print '[INFO] Loading the data...'
path = '/home/satti/Documents/Projects/Acads/DL_Assignments/data/cifar-10-batches-py/'
train_X, train_y,valid_X,  valid_y, test_X , test_y = load_data(path) 
print '[INFO] Training data: ',train_X.shape
print '[INFO] Validation data: ',valid_X.shape
print '[INFO] Testing data: ',test_X.shape
print '[INFO] Loading the data done!'
batch_size = 8
train()


# for i in tf.trainable_variables():
# 	print i
