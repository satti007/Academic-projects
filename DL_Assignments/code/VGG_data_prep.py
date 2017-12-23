import os
import cPickle
import numpy as np

# Reading data from the batch files
def unpickle(file):
	with open(file, 'rb') as fo:
		dict = cPickle.load(fo)
	return dict

def load_data(path):
	batch_files = []
	
	for file in os.listdir(path):
		if "_batch" in file  :
			batch_files.append(os.path.join(path, file))
	
	batch_files.sort()
	
	data_X = np.vstack([unpickle(file)['data'] for file in batch_files])	
	data_y = np.hstack([unpickle(file)['labels'] for file in batch_files])	
	
	# Splitting the data into train, valid, test
	train_X, valid_X, test_X = data_X[0:45000],data_X[45000:50000],data_X[50000:]
	train_y, valid_y, test_y = data_y[0:45000],data_y[45000:50000],data_y[50000:]
	
	# Reshaping into width*height*channels for convnets	
	train_X = train_X.reshape(45000,32,32,3)
	valid_X = valid_X.reshape(5000,32,32,3)
	test_X  = test_X.reshape(10000,32,32,3)

	im = (im-np.mean(im)) / np.std(im)
	
	return train_X, train_y,valid_X,  valid_y, test_X , test_y 

'''
count = np.bincount(train_y)
values = np.nonzero(count)[0]
zip(values,count[values]) 
'''

'''
indicies = np.argsort(train_y)
train_X = train_X[indicies]
train_y = train_y[indicies]
'''