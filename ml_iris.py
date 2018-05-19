#!/usr/bin/env python3
#import dataset
from sklearn.datasets import load_iris
#import tree for decision tree algo
from sklearn import tree
import numpy as np

#loading dataset
iris=load_iris()

#loading feature names
fl_features=iris.feature_names
#print(fl_features)

#loading target name(flower names)
fl_names=iris.target_names
#print(fl_names)

#loading targets (for each data input)
fl_data_names=iris.target
#print(fl_data_names)

#loading data
fl_data=iris.data

#splitting targets to creat train and test list
#for setosa
setosa=fl_data_names[0:50]
#setosa training data
setosa_train=setosa[0:49]
#setosa test data
setosa_test=setosa[-1]

#for versicolor
versi=fl_data_names[50:100]
#versi training data
versi_train=versi[0:49]
#versi test data
versi_test=versi[-1]

#for virginica
vir=fl_data_names[100:150]
#vir training data
vir_train=vir[0:49]
#setosa test data
vir_test=vir[-1]

#creating list of targets to train
train_target=np.concatenate((setosa_train,versi_train,vir_train))

# print(train_target.shape,train_target.size)

#splitting data
#for setosa
setosa_data=fl_data[0:50]
#setosa training data
setosa_train_data=setosa_data[0:49]
#setosa test data
setosa_test_data=setosa_data[-1]

#for versicolor
versi_data=fl_data[50:100]
#versi training data
versi_train_data=versi_data[0:49]
#versi test data
versi_test_data=versi_data[-1]

#for virginica
vir_data=fl_data[100:150]
#vir training data
vir_train_data=vir_data[0:49]
#setosa test data
vir_test_data=vir_data[-1]

train_data=np.concatenate((setosa_train_data,versi_train_data,vir_train_data))

# print(train_data.shape,train_data.size)


#now training using algo

#loading decision tree algo
algo=tree.DecisionTreeClassifier()

#training with data
algo.fit(train_data,train_target)		#as numpy array
#algo.fit([*train_data],[*train_target])#as list

#testing
result1=algo.predict([setosa_test_data])	# test data format should be same as input data format
print(result1)
# result2=algo.predict([versi_test_data])
# print(result2)
# result3=algo.predict([vir_test_data])
# print(result3)