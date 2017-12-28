from knn import * 
from data_prep import *
from sklearn.metrics import confusion_matrix,accuracy_score

print '[INFO] Loading the data...'
path = '/home/satti/Documents/Projects/Acads/ML_Assignments/data/PR_DATASET/Image/Image.mat'
labels = [8,2,5,16,6] # load data of these lables for the classification
train_X,train_y,valid_X,valid_y,test_X ,test_y = load_data(path,labels,doSampling=False)
print '[INFO] Training data:   ', train_X.shape
print '[INFO] Validation data: ', valid_X.shape
print '[INFO] Testing data:    ', test_X.shape
print '[INFO] Loading the data done!'

# Model_1 -- knn
print '[INFO] Model_1: knn...'
nn_predictions,knn_predictions,k = knn_classify(train_X,train_y,valid_X,valid_y,test_X ,test_y)
print '[INFO] Accuracy for nn model(only based on nearest neighbour): {:.2f}%'.format(100*accuracy_score(test_y,nn_predictions))
print '[INFO] Accuracy for knn model(based on {} nearest neighbours): {:.2f}%'.format(k,100*accuracy_score(test_y,knn_predictions))
print '[INFO] knn model done!'


# Model_2 -- SVMs
train_X,train_y,valid_X,valid_y,test_X ,test_y = load_data(path,labels,doSampling=True)
print '[INFO] Model_2: SVM-Gaussaion Kernel...'
predictions = svm_classify(train_X,train_y,valid_X,valid_y,test_X,test_y)
print '[INFO] SVM-Gaussaion Kernel done!'



# # Model_2 -- neural network
# # train_X,train_y,valid_X,valid_y,test_X ,test_y = load_data(path,labels,doSampling=True)
# print '[INFO] Model_2: neural network...'
# predictions = net_classify(train_X,train_y,valid_X,valid_y,test_X,test_y)
# print '[INFO] neural network done!'

labels=[9,10,17,5,13]
