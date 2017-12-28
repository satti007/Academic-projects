import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

def net_classify(train_X,train_y,valid_X,valid_y,test_X ,test_y):
indices = np.arange(train_X.shape[0])
np.random.shuffle(indices)
train_X = train_X[indices]
train_y = train_y[indices]

sizes = [100,100]
net = MLPClassifier(hidden_layer_sizes=tuple(sizes), activation='tanh', solver='adam', alpha=0.1, batch_size=64, 
					shuffle=True, learning_rate_init=0.001, max_iter=1,random_state=42, verbose=True) 
net.fit(train_X,train_y)

pred = net.predict(test_X)
acc = accuracy_score(test_y,pred)
print(confusion_matrix(test_y,pred))

count = np.bincount(pred)
values = np.nonzero(count)[0]
zip(values,count[values]) 
