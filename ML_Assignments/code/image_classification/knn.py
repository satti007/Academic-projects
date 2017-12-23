import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

def distance(v1, v2, metric):
	if metric == 'euclidean':
		return np.sqrt(np.sum((v1 - v2) ** 2,axis=1))    

def get_predictions(k_neighbours_mat):
	predictions = np.ones(k_neighbours_mat.shape[0],dtype=int)
	for i in range(k_neighbours_mat.shape[0]):
		class_votes =  np.bincount(k_neighbours_mat[i])
		max_votes_classes = np.where(class_votes == np.max(class_votes))[0] 
		class_index = np.argmin([k_neighbours_mat[i].tolist().index(j) for j in max_votes_classes])
		predictions[i] = max_votes_classes[class_index]
	return predictions

# 1 neighbour to 50 neighbours get best k 
# k_max should be based on training data size
def get_best_k(dist_mat_val,train_y,valid_y,k_max):
	neighbours_mat = train_y[np.argsort(dist_mat_val,axis=1)]
	accuracy = []
	for k in range(1,k_max+1):
		k_neighbours_mat = neighbours_mat[:,:k]
		predictions = get_predictions(k_neighbours_mat)
		accuracy.append(accuracy_score(valid_y,predictions))
	return np.argmax(accuracy)+1

def knn_classify(train_X,train_y,valid_X,valid_y,test_X ,test_y):
	dist_mat_val = np.vstack([distance(train_X, valid_X[i], 'euclidean') for i in range(0,valid_X.shape[0])])
	dist_mat_test = np.vstack([distance(train_X, test_X[i],  'euclidean') for i in range(0,test_X.shape[0])])
	
	# nn classification(only based on nearest neighbour)
	nn_predictions = train_y[np.argmin(dist_mat_test,axis=1)]
	
	# knn classification(based on k nearest neighbours)
	k = get_best_k(dist_mat_val,train_y,valid_y,50) 
	knn_predictions = get_predictions(train_y[np.argsort(dist_mat_test,axis=1)][:,:k])
	
	return nn_predictions,knn_predictions,k

'''
STILL TODO:
1. User Other Metric
2. Weighted knn
'''