import numpy as np
import tensorflow as tf
from knn import * 
from data_prep import *
from sklearn.metrics import confusion_matrix,accuracy_score

print '[INFO] Loading the data...'
path = '/home/satti/Documents/Projects/Acads/ML_Assignments/data/PR_DATASET/Image/Image.mat'
labels = [8,2,5,16,6] # load data of these lables for the classification
train_X,train_y,valid_X,valid_y,test_X ,test_y = load_data(path,labels)
print '[INFO] Training data:   ', train_X.shape
print '[INFO] Validation data: ', valid_X.shape
print '[INFO] Testing data:    ', test_X.shape
print '[INFO] Loading the data done!'


# Model_1 -- knn
nn_predictions,knn_predictions,k = knn_classify(train_X,train_y,valid_X,valid_y,test_X ,test_y)
print '[INFO] Accuracy for nn model(only based on nearest neighbour): {:.2f}%'.format(100*accuracy_score(test_y,nn_predictions))
print '[INFO] Accuracy for knn model(based on {} nearest neighbours): {:.2f}%'.format(k,100*accuracy_score(test_y,knn_predictions))







# from sklearn.neural_network import MLPClassifier

# indices = np.arange(train_X.shape[0])
# np.random.shuffle(indices)
# train_X = train_X[indices]
# train_y = train_y[indices]

# sizes = [100,100]
# net = MLPClassifier(hidden_layer_sizes=tuple(sizes), activation='tanh', solver='adam', alpha=0.1, batch_size=64, 
# 					shuffle=True, learning_rate_init=0.001, max_iter=500,random_state=42, verbose=True) 
# net.fit(train_X,train_y)
# pred = net.predict(valid_X)
# acc = accuracy_score(valid_y,pred)
# acc
# pred = net.predict(train_X)
# acc = accuracy_score(train_y,pred)
# acc

# print(confusion_matrix(test_y,pred))
# print(classification_report(test_y,pred))

# count = np.bincount(pred)
# values = np.nonzero(count)[0]
# zip(values,count[values]) 


# pred = net.predict(test_X)
# acc = accuracy_score(test_y,pred)
# acc
