# -*- coding: utf-8 -*-
"""Pneumonia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chB5YUO5LZq8TCjqipsSXMNtIz9s2cFz
"""

from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
from numpy import asarray
import pandas as pd
from array import array
import glob
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib import image

from google.colab import drive
drive.mount('/content/drive')

numberoftrainingimagestocall=300

#!pip install tensorflow-gpu

"""**Get Training Normal Data**"""

import math
trainTestSplitRatio=.3
trainValidationSplitRatio=.2
NumberOfTestImagesToCall=100
xlength=150
ylength=210

ListOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/train/NORMAL/*.jpg')
ListOfFiles=ListOfFilesT[:NumberOfTrainingImagesToCall]
len(ListOfFilesT)

def readImageFromDrive(fileX):
  training_data=[]
  print(fileX)
  im=image.imread(fileX)
  ImNP=asarray(im)
  training_data.append(np.asanyarray(imResized))
  training_data=np.array(training_data)
  training_data
  trainValidationSplitRatio
  training_data
  training_data=np.reshape(training_data,(-1,xlength,ylength))
  training_data=training_data/127.5-1
  return training_data

readImageFromDrive(ListOfFiles[0])

for file in listOfFiles:
  training_dataset_tmp=[]
  training_dataset_tmp=readImageFromDrive(file)
  training_dataset_tmp=np.append(training_dataset_tmp,'NORMAL')
  training_dataset=np.append(np.array(training_dataset),np.array(training_dataset_tmp),
  #training_dataset[i,0:]=training_dataset_tmp

#reshape
print(len(training_dataset))
FeatureSize=int(len(training_dataset)/NumberOfTrainingImagesToCall)
training_dataset=np.reshape(training_dataset,(NumberOfTrainingImagesToCall,FeatureSize))
training_dataset.shape
training_dataset[1,]
training_dataset_NORMAL=training_dataset

"""**Get Training Pneumonia Data**

"""

listOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/train/PNEUMONIA/*.jpeg')
listOfFiles=listOfFilesT[:NumberOfTrainingImagesToCall]
len(listOfFilesT)

training_dataset=[]
for file in listOfFiles:
  training_dataset_tmp=[]
  training_dataset_tmp=readImageFromDrive(file)
  training_dataset_tmp=np.append(training_dataset_tmp,'PNEUMONIA')
  training_dataset=np.append(np.array(training_dataset),np.array(training_dataset_tmp),)
  #training_dataset[i,0:]=training_dataset_tmp

#reshape
print(len(training_dataset))
FeatureSize=int(len(training_dataset)/NumberOfTrainingImagesToCall)
training_dataset=np.reshape(training_dataset,(NumberOfTrainingImagesToCall,FeatureSize))
training_dataset.shape
training_dataset[1,]
training_dataset_PNEUMONIA=training_dataset

#training_dataset=[]
#training_dataset=np.append(training_dataset,training_dataset_NORMAL)
training_dataset=np.append(np.array(training_dataset_NORMAL),np.array(training_dataset_PNEUMON
training_dataset.shape

"""**Get Test Normal Data**

"""

listOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/test/NORMAL/*.jpeg')
listOfFiles=listOfFilesT[:NumberOfImagesToCall]
len(listOfFilesT)

test_dataset=[]
for file in listOfFiles:
  training_dataset_tmp=[]
  training_dataset_tmp=readImageFromDrive(file)
  training_dataset_tmp=np.append(training_dataset_tmp,'NORMAL')
  training_dataset=np.append(np.array(training_dataset),np.array(training_dataset_tmp),axis=0)

#reshape
print(len(test_dataset))
FeatureSize=int(len(test_dataset)/NumberOfTestImagesToCall)
test_dataset=np.reshape(test_dataset,(NumberOfTestImagesToCall,FeatureSize)
test_dataset.shape
test_dataset[1,]
test_dataset_NORMAL=test_dataset
test_dataset_NORMAL

"""**Get Test PNEUMONIA data**"""

listOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/test/PNEUMONIA/*.jpeg')
listOfFiles=listOfFilesT[:NumberOfImagesToCall]
len(listOfFilesT)



test_dataset=[]
for file in listOfFiles:
  training_dataset_tmp=[]
  training_dataset_tmp=readImageFromDrive(file)
  training_dataset_tmp=np.append(training_dataset_tmp,'PNEUMONIA')
  training_dataset=np.append(np.array(training_dataset),np.array(training_dataset_tmp),axis=0)

#reshape
print(len(test_dataset))
FeatureSize=int(len(test_dataset)/NumberOfTestImagesToCall)
test_dataset=np.reshape(test_dataset,(NumberOfTestImagesToCall,FeatureSize)
test_dataset.shape
test_dataset[1,]
test_dataset_PNEUMONIA=test_dataset
test_dataset_PNEUMONIA.shape

#test_dataset=[]
#test_dataset=np.append(np.array(test_dataset_NORMAL),np.array(test_dataset_PNEUMONIA),axis=
test_dataset.shape

"""**Get Validation NORMAL data**"""

listOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/val/NORMAL/*.jpeg')
listOfFiles=listOfFilesT[:NumberOfImagesToCall]
len(listOfFilesT)

validation_dataset=[]
for file in listOfFiles:
  validation_dataset_tmp=[]
  
  validation_dataset=np.append(np.array(validation_dataset),np.array(validation_dataset

#reshape
print(len(validation_dataset))
FeatureSize=int(len(validation_dataset)/NumberOfTestImagesToCall)
validation_dataset=np.reshape(validation_dataset,(NumberOfTestImagesToCall,FeatureS
validation_dataset.shape
validation_dataset[1,]
validation_dataset_NORMAL=validation_dataset
validation_dataset_NORMAL

"""**Get Validation PNEUMONIA Data**

"""

listOfFilesT=glob.glob('/content/drive/MyDrive/chest_xray/val/PNEUMONIA/*.jpeg')
listOfFiles=listOfFilesT[:NumberOfImagesToCall]
len(listOfFilesT)

validation_dataset=[]
for file in listOfFiles:
  validation_dataset_tmp=[]
  validation_dataset_tmp=readImageFromDrive(file)
  validation_dataset_tmp=np.append(validation_dataset_tmp,'PNEUMONIA')
  validation_dataset=np.append(np.array(validation_dataset),np.array(validation_dataset_

#reshape
print(len(validation_dataset))
FeatureSize=int(len(validation_dataset)/NumberOfValidationImagesToCall)
validation_dataset=np.reshape(validation_dataset,(NumberOfValidationImagesToCall,FeatureS
validation_dataset.shape
validation_dataset[1,]
validation_dataset_PNEUMONIA=validation_dataset
validation_dataset_PNEUMONIA

#validation_dataset=[]
#validation_dataset=np.append(validation_dataset,validation_dataset_NORMAL)
validation_dataset=np.append(np.array(validation_dataset_NORMAL),np.array(validation_datase
validation_dataset.shape

"""**x_train,y_train,x_test,y_test**

"""

#x_train=training_dataset(:)

#y_train=training_dataset(:)
y_train=training_dataset[:,1]
y_train

x_test=test_dataset[:,:FeatureSize-1]
x_test=x_test.astype(np.float)
x_test

y_test=test_dataset[:,-1]
y_test

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
y_train=labelencoder.fit_transform(y_train)
y_train
y_test=labelencoder.fit_transform(y_test)
y_test

validation_dataset=np.append(np.array(validation_dataset_NORMAL),np.array(validataion_datas
x=np.append(np.array(x_train),np.array(x_test),axis=0)
y=np.append(np.array(y_train),np.array(y_test),axis=0)

from numpy import savetxt
savetxt('x_train.csv',x_train,delimiter=',')
savetxt('y_train.csv',y_train,delimiter=',')
savetxt('x_test.csv',x_test,delimiter=',')
savetxt('y_test.csv',y_test,delimiter=',')

"""**NN**"""

from sklearn.neural_network import MLPClassifier
model=MLPClassifier(hidden_layers_sizes=(10,20,20,10),max_iter=1000)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
predictions

from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,predictions))
confusion_matrix(y_test,predictions)

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model,x_test,y_test)
plt.show()

from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

cv=Kfold(n_splits=10)
model=MLPclassifier(hidden_layers_sizes=(10,20,20,10),max_iter=1000)
scores=cross_val_score(model,x,y,cv=cv)
scores

print(np.mean(scores))

from sklearn import svm
clfSVM=svm.SVC()
clfSVM.fit(x_train,y_train)
#test_set
outTest=clfSVM.predict(x_test)
outTest

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(clfSVM,x_test,y_test)
plt.show()

print(classification_report(y_test,outTest))
confusion_matrix(y_test,outTest)

clfSVM=svm.SVC
cv=KFold(n_splits=10)
scores=cross_val_score(clfSVM,x,y,cv=cv)
scores

np.mean(scores)

from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf.fit(x_train,y_train)

#test_set
outTest=clf.precdit(x_test)
outTest

print(classification_report(y_test,outTest))
confusion_matrix(y_test,outTest)

plot_confusion_matrix(clf,x_test,y_test)
plt.show()

from sklearn import tree
clf=tree.DecisionTreeClassifier
cv=KFold€(n_splits=10)
scores=cross_val_score(clf,x,y,cv=cv)
scores

np.mean(scores)