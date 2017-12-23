import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

def randomForest(train_data,valid_data):
	features = train_data.shape[1] - 1
	T_X,T_y = train_data.iloc[:,0:features],train_data["labels"]
	V_X,V_y = valid_data.iloc[:,0:features],valid_data["labels"]
	split_feat = ["sqrt","log2",None]
	models = []
	valid_acc = []
	file = open("valid_acc.log","a")
	
	for i in range(1,11):
		trees = 100*i
		for feat in split_feat:
			print "n_estimators: {}, max_features: {}".format(trees,feat)
			model = RandomForestClassifier(n_estimators=trees,max_features=feat,random_state=0)
			model.fit(T_X,T_y)
			acc = model.score(V_X,V_y)
			valid_acc.append(acc)
			models.append(model)
			print "n_estimators: {}, max_features: {}, acc: {}\n".format(trees,feat,acc)
			file.write("n_estimators: {}, max_features: {}, acc: {}\n".format(trees,feat,acc))
	
	file.close()
	return models, valid_acc.index(max(valid_acc))

### Training
## Random Forest
train_data = pd.read_csv("../data/ML_DATASET/train_data.csv")
valid_data = pd.read_csv("../data/ML_DATASET/valid_data.csv")
test_data = pd.read_csv("../data/ML_DATASET/test_data.csv")

models,index = randomForest(train_data,valid_data)
### Testing
model = models[index]  ## Select the x after checking the valid_acc.log
model.fit(T_X,T_y)
prediction = model.predict(test_data.iloc[:,0:features])
S = pd.Series(prediction)
S.value_counts()
acc = accuracy_score(test_data["labels"],S)
print S
print "Accuracy: ",acc