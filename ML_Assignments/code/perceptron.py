import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def perceptron(beta,beta_,gamma,postivie_data,negative_data):
	error = 10^5
	while error > gamma:
		postivie_error = np.zeros(dtype=int,[len(postivie_data)])
		for point in postivie_data:










data_1 = pd.read_csv("../data/PR_DATASET/2d_Dataset/linearly_Separable_Data/class1_train.txt",header=None,sep=" ")
data_2 = pd.read_csv("../data/PR_DATASET/2d_Dataset/linearly_Separable_Data/class2_train.txt",header=None,sep=" ")

plt.plot(data_1[0],data_1[1], 'ro')
plt.plot(data_2[0],data_2[1], 'b*')
plt.show()
