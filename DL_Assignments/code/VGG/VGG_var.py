from VGG_data_prep import load_data

print '[INFO] Loading the data...'
path = '/home/satti/Documents/Projects/Acads/DL_Assignments/data/cifar-10-batches-py/'
train_X, train_y,valid_X,  valid_y, test_X , test_y = load_data(path) 
print '[INFO] Training data: ',train_X.shape
print '[INFO] Loading the data done!'

