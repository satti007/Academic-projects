import scipy.io
import numpy as np
from sklearn.model_selection import train_test_split

'''def Sampling(train_X, train_y):
	from imblearn.over_sampling import SMOTE
	sm = SMOTE(random_state=12, ratio = 1.0)
	train_X,train_y = sm.fit_sample(train_X, train_y)
'''
def load_data(path,labels,doSampling=False):
	mat = scipy.io.loadmat(path) 
	
	train_X = np.zeros((100,48))
	train_y = np.ones(100, dtype=int)
	valid_X = np.zeros((100,48))
	valid_y = np.ones(100,dtype=int)
	test_X  = np.zeros((100,48))
	test_y  = np.ones(100,dtype=int)
	
	for l in labels:
		data_X = mat['CompleteData'][l][0]
		data_y = l*np.ones(data_X.shape[0],dtype = int)
		X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.3, random_state=42)
		train_X = np.vstack([train_X,X_train])
		train_y = np.hstack([train_y,y_train])
		X_valid, X_test, y_valid, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
		valid_X = np.vstack([valid_X,X_valid])
		valid_y = np.hstack([valid_y,y_valid])
		test_X  = np.vstack([test_X,X_test])
		test_y  = np.hstack([test_y,y_test])
	
	train_X = train_X[100:]
	train_y = train_y[100:]
	valid_X = valid_X[100:]
	valid_y = valid_y[100:]
	test_X  = test_X[100:]
	test_y  = test_y[100:]
	
	if doSampling:
		train_X,train_y = Sampling(train_X, train_y)
	
	return 	train_X,train_y,valid_X,valid_y,test_X ,test_y  

data_X = np.zeros((100,48))
data_y = np.ones(100, dtype=int)