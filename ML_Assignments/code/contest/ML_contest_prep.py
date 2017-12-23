import numpy as np
import pandas as pd

def PCA(data):
	sigma = np.cov(data,rowvar=False)
	U,D,V = np.linalg.svd(sigma,compute_uv=1)
	var_retained = np.cumsum(D)/np.sum(D)
	K = np.argwhere(var_retained > 0.99)
	Z = U[:, 0:K[0][0]+1]
	Red_data =  pd.DataFrame(data=np.matmul(data,Z))
	# Org_data = np.matmul(Red_data,Z.transpose())
	return Red_data

def dataDivision(Red_data):
	Red_data["labels"] = pd.read_csv("../data/ML_DATASET/labels",header=None)
	labels = Red_data['labels'].value_counts().index.tolist()
	train_data = pd.DataFrame()
	valid_data = pd.DataFrame()
	test_data = pd.DataFrame()
	for l in labels: # Division in each label
		l_data = Red_data.loc[Red_data['labels'] == l]
		data_1, data_2, data_3 = np.split(l_data.sample(frac=1), [int(.72*len(l_data)),int(.8*len(l_data))])
		train_data = train_data.append(data_1, ignore_index=True)
		valid_data = valid_data.append(data_2, ignore_index=True)
		test_data = test_data.append(data_3, ignore_index=True)
	
	train_data = train_data.sample(frac=1).reset_index(drop=True)
	valid_data = valid_data.sample(frac=1).reset_index(drop=True)
	test_data = test_data.sample(frac=1).reset_index(drop=True)
	
	return train_data,valid_data,test_data

### Reading data files
data = pd.read_csv("../data/ML_DATASET/data",header=None)
print "Shape of data:",data.shape

### Dimension Reduction
## Method 1 -- PCA 
print "Dimension Reduction - PCA"
Red_data = PCA(data)
print "Shape of Red_data:",Red_data.shape
Red_data.to_csv('../data/ML_DATASET/Red_data.csv', index=False)

### Data divison into train(80%) and test(20%) 
train_data,valid_data,test_data =  dataDivision(Red_data) 
print " Shape of train_data: {}\n Shape of valid_data: {}\n Shape of test_data: {}\n".format(train_data.shape,valid_data.shape,test_data.shape)
train_data.to_csv('../data/ML_DATASET/train_data.csv', index=False)
valid_data.to_csv('../data/ML_DATASET/valid_data.csv', index=False)
test_data.to_csv('../data/ML_DATASET/test_data.csv', index=False)