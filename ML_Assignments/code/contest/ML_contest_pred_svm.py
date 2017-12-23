import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def svc_param_selection(X, y, nfolds):
	costs  = [0.01,0.1, 1, 10]
	gammas = [0.01, 0.1, 1]
	param_grid = {'C': costs, 'gamma' : gammas}
	grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=nfolds)
	grid_search.fit(X, y)
	grid_search.best_params_
	return grid_search.best_params_

### Training
## SVM

def trainSVM(train_data,valid_data,test_data):
	print"SVM started"
	train_data = train_data.append(valid_data, ignore_index=True) 
	train_data = train_data.sample(frac=1).reset_index(drop=True)
	print"Searching for best_params"
	features = train_data.shape[1] - 1
	X,y = train_data.iloc[:,0:features],train_data["labels"]
	best_params = svc_param_selection(X,y,3)
	print best_params
	model = svm.SVC(C = best_params["C"],gamma = best_params["gamma"])
	print "Training started"
	model.fit(X,y)
	print "Training Done!!"

	### Testing
	print "Testing started"
	prediction = model.predict(test_data.iloc[:,0:features])
	S = pd.Series(prediction)
	S.value_counts()
	acc = accuracy_score(test_data["labels"],S)
	print S
	print "Accuracy: ",acc

train_data = pd.read_csv("../data/ML_DATASET/train_data.csv")
valid_data = pd.read_csv("../data/ML_DATASET/valid_data.csv")
test_data = pd.read_csv("../data/ML_DATASET/test_data.csv")

trainSVM(train_data,valid_data,test_data)



features = train_data.shape[1] - 1
train_data = train_data.append(valid_data, ignore_index=True) 
train_data = train_data.sample(frac=1).reset_index(drop=True)
X,y = train_data.iloc[:,0:features],train_data["labels"]
model = svm.SVC()
print "Training started"
model.fit(X,y)
print "Training Done!!"
### Testing
print "Testing started"
prediction = model.predict(test_data.iloc[:,0:features])
S = pd.Series(prediction)
print S.value_counts()
acc = accuracy_score(test_data["labels"],S)
print "Accuracy: ",acc
