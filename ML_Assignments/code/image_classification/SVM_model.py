import math
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def svc_param_selection(X, y, nfolds):
	costs = [math.pow(10, i) for i in range(-13,14)]
	gammas = [math.pow(10, i) for i in range(-13,14)]
	param_grid = {'C': costs, 'gamma' : gammas}
	grid_search = GridSearchCV(svm.SVC(kernel='rbf',verbose=True), param_grid, cv=nfolds)
	grid_search.fit(X, y)
	grid_search.best_params_
	return grid_search.best_params_

def svm_classify(train_X,train_y,valid_X,valid_y,test_X,test_y):
	X = np.vstack([train_X,valid_X]) 
	y = np.hstack([train_y,valid_y])
	
	indices = np.arange(X.shape[0])
	np.random.shuffle(indices)
	X = X[indices]
	y = y[indices]
	
	print"[INFO] Searching for best_params"
	best_params = svc_param_selection(train_X,train_y,3)
	print best_params
	model = svm.SVC(kernel='rbf',C = best_params["C"],gamma = best_params["gamma"])
	# model = svm.SVC(kernel='rbf',C = 0.001,gamma = 1e-10)
	print "[INFO] Training started"
	model.fit(X,y)
	print "[INFO] Training Done!!"
	
	### Testing
	print "[INFO] Testing started"
	predictions = model.predict(test_X)	
	print predictions
	print "[INFO] Testing done!"
	
	return predictions

# model = svm.SVC(kernel='rbf',C = 1,gamma = 1e-12)
