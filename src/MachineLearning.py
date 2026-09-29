import tensorflow# mlp for regression
from numpy import sqrt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
import tensorflow as tf
import pandas as pd
# load the dataset
import pickle
import numpy as np
import keras
from tqdm import tqdm
from numpy import sqrt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
import tensorflow as tf
import pandas as pd
# load the dataset
import pickle
import numpy as np
import keras
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import normalize
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
import time
import math
from tensorflow.keras import datasets, layers, models, backend
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
import keras
import tensorflow_addons as tfa
########################################################################################################################################################################################################
#######################################################################################################################################################################################################
########################################################################################################################################################################################################
#######################################################################################################################################################################################################
######################LOADING DATA#####################################################################################################################################################################
########################################################################################################################################################################################################
#######################################################################################################################################################################################################
########################################################################################################################################################################################################
#######################################################################################################################################################################################################

pickle_off = open("D:/data_for_training150000_1v_1t.pkl","rb")
emp = pickle.load(pickle_off)

arr = np.asarray(emp)
X=np.array(emp[:2][:][:])
y=np.array(emp[2][:][:])


del emp
del arr

X=X.reshape(len(X[0]),len(X[0][0]),len(X))
y=y.reshape(len(y),len(y[0]))

from tqdm import tqdm
arr=y
shape = arr.shape
result = np.zeros(shape)
count_all=0
count_1=0
percent_occupancy=[0]*shape[0]
for x in tqdm(range(0, shape[0])):
  count_all=0
  count_1=0
  for z in range(0, shape[1]):
        count_all=count_all+1
        if arr[x][z] >= 1:
            result[x][z] = 1
            count_1=count_1+1
        else:
          result[x][z] = 0
        percent_occupancy[x]=(count_1/count_all)*100
print(result)
print(len(result[0]))
#print(y)
del arr
del y
y=result
import numpy
y=y[:,1:]
print(y.shape)
result=y
del y
import numpy
y=result
y=y[:,:-1]
print(y.shape)
#y= numpy.delete(y, y[:,0])
result=y
del y
print(X.shape)
temp=X
temp=temp[:,1:,:]
print(temp.shape)
X=temp
del temp
print(X.shape)
temp=X
temp=temp[:,:-1,:]
print(temp.shape)
X=temp
del temp
X=X.reshape(len(X),len(X[0])*len(X[0][0]))
print(result.shape)

print(X.shape)

X_train= X
del X

Y_train=result
del result




pickle_off = open("D:/data_for_testing100_1v_1t.pkl", "rb")
emp = pickle.load(pickle_off)

# print(emp)
# print(len(emp[0][0]))
# print(len(emp[0]))
# print(len(emp))
# print(type(emp))
arr = np.asarray(emp)
# print(arr)
# print(arr.shape)
# print(len(arr))
# print(len(arr[0]))
# print(len(arr[0][0]))
# (4, 1000, 352)


X_T = np.array(emp[:2][:][:])
y_T = np.array(emp[2][:][:])
del emp
del arr
# print(X.shape)
# print(y.shape)
# X = np.reshape(X, (353,3,1000)).T
X_T = X_T.reshape(len(X_T[0]), len(X_T[0][0]), len(X_T))
y_T = y_T.reshape(len(y_T), len(y_T[0]))
# y = np.reshape(y, (354,1,1000)).T

# print(X.shape)
# print(y.shape)
# print(len(X[0][0]))
# print(len(X[0]))
# print(len(X))
# print(X)
# split into train and test datasets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# determine the number of input features
# n_features = X_train.shape[1]
# n_features = X_train.shape
# n_features_l=n_features[0]
# n_features_b=n_features[1]
# y_len=y_train.shape
from tqdm import tqdm

arr = y_T
shape_T = arr.shape
result_T = np.zeros(shape_T)
count_all = 0
count_1 = 0
percent_occupancy = [0] * shape_T[0]
for x in tqdm(range(0, shape_T[0] - 1)):
    count_all = 0
    count_1 = 0
    for z in range(0, shape_T[1]):
        count_all = count_all + 1
        if arr[x][z] >= 1:
            result_T[x][z] = 1
            count_1 = count_1 + 1
        else:
            result_T[x][z] = 0
        percent_occupancy[x] = (count_1 / count_all) * 100
print(result_T)
print(len(result_T[0]))
# print(y)
del arr
del y_T

y_T = result_T
print(y_T.shape)
print(len(y_T))

import numpy

y_T = y_T[:, 1:]
print(y_T.shape)
# y= numpy.delete(y, y[:,0])
result_T = y_T
del y_T

import numpy

y_T = result_T
y_T = y_T[:, :-1]
print(y_T.shape)
# y= numpy.delete(y, y[:,0])
result_T = y_T
del y_T

print(X_T.shape)
temp_T = X_T
temp_T = temp_T[:, 1:, :]
print(temp_T.shape)
X_T = temp_T
del temp_T

print(X_T.shape)
temp_T = X_T
temp_T = temp_T[:, :-1, :]
print(temp_T.shape)
X_T = temp_T
del temp_T
X_T = X_T.reshape(len(X_T), len(X_T[0]) * len(X_T[0][0]))
print(X_T.shape)



X_test= X_T
del X_T

Y_test=result_T
del result_T



accuracy_score_nn = []
precison_score_nn = []
recall_score_nn = []
f1_score_nn = []
mcc_nn = []
roc_auc_nn = []
tn_nn = []
fp_nn = []
fn_nn = []
tp_nn = []
time_nn = []
test_nn = []
cost_nn = []
epoch_nn = []
batch_nn = []
batch_sizes = [10]
epoch_var = [1]
setting = []
metrices_obtained=[]

start = time.time()

# accuracy: (tp + tn) / (tp + tn + fp + fn)
# precision tp / (tp + fp)
# recall: tp / (tp + fn)
# f1: 2 tp / (2 tp + fp + fn)


'''METRICS = [
      #keras.metrics.TruePositives(name='tp'),
      #keras.metrics.FalsePositives(name='fp'),
      #keras.metrics.TrueNegatives(name='tn'),
      #keras.metrics.FalseNegatives(name='fn'),      
      keras.metrics.BinaryAccuracy(name='accuracy'),
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall'),
      #keras.metrics.AUC(name='auc'),
      #keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
      tfa.metrics.MatthewsCorrelationCoefficient(num_classes=len(Y_train[0]),name='MatthewsCorrelationCoefficient'), #Trying something new
      tfa.metrics.HammingLoss(num_classes=len(Y_train[0]),mode='multilabel',name='hamming_loss')
      #tfa.metrics.F1Score(num_classes=len(result[0]),name='f1_score')

]'''
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
############################ JUST TRAINING A MODEL WITH NO BIAS OR ANYTHING################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
'''
# define model
#filepath='/content/gdrive/Shareddrives/Winter Simulation 2021/model_epoch'
#keras.callbacks.ModelCheckpoint(filepath, monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)

model = Sequential()
model.add(Dense(1000, kernel_initializer='he_uniform',activation='relu', input_shape=(len(X_train[0]),)))
model.add(Dense(1000, activation='relu'))
model.add(Dense(1000, activation='relu'))
model.add(Dense(1000, activation='relu'))
#model.add(Dense(1000, activation='relu'))
#model.add(Dense(1000, activation='relu'))
#model.add(Dense(1000, activation='relu'))
#model.add(Dense(1000, activation='relu'))
#model.add(Dense(8000, activation='relu', kernel_initializer='he_normal'))
model.add(Flatten())
#model.add(Dense(len(y[0]), activation='linear'))
#model.add(Dense(1000, activation='linear'))

model.add(Dense(len(Y_test[0]), activation='sigmoid'))

#model.add(Dense(2, activation='softmax'))
#Multiclass classification/ multi label classification 
#loss and dimensions


#model.add(Dense((len(y_train[0])))
# compile the model
#model.compile(optimizer='adam', loss='mean_squared_error')
#model.compile(loss='mean_squared_error', optimizer=opt)
#model.compile(optimizer='rmsprop',loss='mse')


model.compile(optimizer="adam", loss="binary_crossentropy")
#Try decay rate and see . 

model.summary()
# fit the model


#model.fit(X_train, y_train, epochs=150, batch_size=1, verbose=0)
#model.fit(X, y,validation_split=0.33, epochs=250, batch_size=100, verbose=1)
model.fit(X_train, Y_train, validation_split=0.33,epochs=8, batch_size=1500, verbose=1)


model.save("D/my_model_9_13_21_4_layer_classifier_multilabel_1v_1t")
np.save('D/my_history_9_13_21_4_layers_1v_1t.npy',model.history.history)
#model.fit(X, result,epochs=500, batch_size=10, verbose=0,callbacks=[tqdm_callback])
# evaluate the model
#loss: 27.3783 - mae: 2.5900 - val_loss: 47.2541 - val_mae: 3.5472

import keras
reconstructed_model = keras.models.load_model("D/my_model_9_13_21_4_layer_classifier_multilabel_1v_1t")

y_pred=model.predict(X_train)
print("training accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_train))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

print("other training results")
from sklearn.metrics import multilabel_confusion_matrix
y_pred=model.predict(X_train)
y_pred = (y_pred>0.5) 
cc=multilabel_confusion_matrix(Y_train, y_pred)

TN=0
for i in range(0,len(cc)):
  TN=TN+cc[i][0][0]

FN=0
for i in range(0,len(cc)):
  FN=FN+cc[i][1][0]

TP=0
for i in range(0,len(cc)):
  TP=TP+cc[i][1][1]

FP=0
for i in range(0,len(cc)):
  FP=FP+cc[i][0][1]


precision=TP/(TP+FP)
recall=TP/(TP+FN)
f1=2*TP/(2*TP+FP+FN)
print(precision)
print(recall)
print(f1)



y_pred=model.predict(X_test)
print("testing accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_test))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

print("other testing results")
from sklearn.metrics import multilabel_confusion_matrix
y_pred=model.predict(X_test)
y_pred = (y_pred>0.5) 
cc=multilabel_confusion_matrix(Y_test, y_pred)

TN=0
for i in range(0,len(cc)):
  TN=TN+cc[i][0][0]

FN=0
for i in range(0,len(cc)):
  FN=FN+cc[i][1][0]

TP=0
for i in range(0,len(cc)):
  TP=TP+cc[i][1][1]

FP=0
for i in range(0,len(cc)):
  FP=FP+cc[i][0][1]


precision=TP/(TP+FP)
recall=TP/(TP+FN)
f1=2*TP/(2*TP+FP+FN)
print(precision)
print(recall)
print(f1)
del model




#Epoch 17/20
#134/134 [==============================] - 20s 152ms/step - loss: 0.1207 - val_loss: 0.1210
#Epoch 18/20
#134/134 [==============================] - 20s 151ms/step - loss: 0.1207 - val_loss: 0.1210
#Epoch 19/20
#134/134 [==============================] - 20s 150ms/step - loss: 0.1206 - val_loss: 0.1212
#Epoch 20/20
#134/134 [==============================] - 20s 150ms/step - loss: 0.1206 - val_loss: 0.1210
#2021-09-13 19:17:09.846187: W tensorflow/python/util/util.cc:348] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.
#training accuracy
#94.58978821569156

#testing accuracy
#94.61039391545243

#DOESNOT IMPROVE TESTING ACCURACY EVEN WHEN THE NUMBER OF EPOCHS ARE INCREASED
#JUST PREDICTING 0S AS THEY ARE MORE IN NUMBER 

'''

#########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
##########################Adding output bias for initialization##############################################################################################################################3
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
'''p = np.sum(Y_train, axis=0)
pos = np.sum(p)
tot = len(Y_train) * len(Y_train[0])
neg = tot - pos
initial_bias = pos / (neg + pos)
output_bias = tf.keras.initializers.Constant(initial_bias)

model = Sequential()
model.add(Dense(3000, activation='relu', input_shape=(len(X_train[0]),)))
model.add(Dense(2000, activation='relu'))
model.add(Dense(500, activation='relu'))
# model.add(Dense(500, activation='relu'))
model.add(Dense(1000, activation='relu'))

model.add(Dense(len(Y_train[0]), activation='sigmoid', bias_initializer=output_bias))

model.summary()
e = 1
b = 1500
# model.compile(optimizer="Adamax", loss="binary_crossentropy",metrics=METRICS)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
# print(e_v, "  ", b_s)

model.fit(X_train, Y_train, epochs=e, batch_size=b, verbose=1)
mid = time.time()

metrics_model = model.evaluate(X_test, Y_test)
predictions_nn = model.predict(X_test)
predictions_nn = (predictions_nn > 0.5)
accuracy_score_nn.append(accuracy_score(Y_test, predictions_nn))
model.evaluate(X_test, Y_test)

from sklearn.metrics import multilabel_confusion_matrix

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)
cc = multilabel_confusion_matrix(Y_test, y_pred)

print(cc)
del model'''


'''
7/7 [==============================] - 0s 8ms/step - loss: 0.1205 - acc: 0.0000e+00
7/7 [==============================] - 0s 8ms/step - loss: 0.1205 - acc: 0.0000e+00
[[[198   0]
  [  2   0]]

 [[197   0]
  [  3   0]]

 [[197   0]
  [  3   0]]

 ...

 [[200   0]
  [  0   0]]

 [[200   0]
  [  0   0]]

 [[200   0]
  [  0   0]]]


  #learns nothing

'''
###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
############################################################################Since op bias didnt work at all...we used different loss function#############################
###########################################################################################################################################################################
##########################################################################################################################################################################
###########################################################################################################################################################################
##########################################################################################################################################################################


'''p = np.sum(Y_train, axis=0)
pos = np.sum(p)
tot = len(Y_train) * len(Y_train[0])
neg = tot - pos
# initial_bias = np.log([pos/neg]) #Could use this as well
initial_bias = pos / (neg + pos)
output_bias = tf.keras.initializers.Constant(initial_bias)


positive_weights = {}
negative_weights = {}
for c in range(0,len(Y_train[0])):
    positive_weights[c] = Y_train.shape[0]/(2*np.count_nonzero(Y_train[c][:]==1))
    negative_weights[c] = Y_train.shape[0]/(2*np.count_nonzero(Y_train[c][:]==0))
print(positive_weights)
print(negative_weights)

class_weight = {0: negative_weights, 1: positive_weights}

import tensorflow
def loss_fn(y_true,y_pred):
    loss = 0
    for i in range(0,len(Y_train[0])):
      loss -= (positive_weights[i]*y_true[0]*tensorflow.keras.backend.log(y_pred[0]) + negative_weights[1]*(1-y_true[0])*tensorflow.keras.backend.log(1-y_pred[0]))


    return loss


start = time.time()

# accuracy: (tp + tn) / (tp + tn + fp + fn)
# precision tp / (tp + fp)
# recall: tp / (tp + fn)
# f1: 2 tp / (2 tp + fp + fn)


METRICS = [
    # keras.metrics.TruePositives(name='tp'),
    # keras.metrics.FalsePositives(name='fp'),
    # keras.metrics.TrueNegatives(name='tn'),
    # keras.metrics.FalseNegatives(name='fn'),
    keras.metrics.BinaryAccuracy(name='accuracy'),
    # keras.metrics.Precision(name='precision'),
    # keras.metrics.Recall(name='recall'),
    # keras.metrics.AUC(name='auc'),
    # keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
    # tfa.metrics.MatthewsCorrelationCoefficient(num_classes=len(Y_train[0]),name='MatthewsCorrelationCoefficient'), #Trying something new
    # tfa.metrics.HammingLoss(num_classes=len(Y_train[0]),mode='multilabel',name='hamming_loss')
    # tfa.metrics.F1Score(num_classes=len(result[0]),name='f1_score')

]

p = np.sum(Y_train, axis=0)
pos = np.sum(p)
tot = len(Y_train) * len(Y_train[0])
neg = tot - pos
# initial_bias = np.log([pos/neg])
initial_bias = pos / (neg + pos)
output_bias = tf.keras.initializers.Constant(initial_bias)

model = Sequential()

model.add(Dense(1500, activation='relu', input_shape=(len(X_train[0]),)))
model.add(Dense(1000, activation='relu'))
model.add(Dense(500, activation='relu'))
model.add(Dense(1000, activation='relu'))
#model.add(Dense(1500, activation='relu'))


# model.add(Dense(1500, activation='relu')) #Added on 6-25-2021

model.add(Dense(len(Y_train[0]), activation='sigmoid', bias_initializer=output_bias))

model.summary()
e = 1
b = 1500
tf.keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=100, verbose=0, mode="auto", baseline=None,
                                 restore_best_weights=True)
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=1e-2, decay_steps=10, decay_rate=0.9)
tf.keras.optimizers.Adam(learning_rate=lr_schedule, beta_1=0.8, beta_2=0.999, epsilon=1e-07, name="Adam")
model.compile(optimizer="Adam", loss=loss_fn, metrics=METRICS)
# model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
# print(e_v, "  ", b_s)

history = model.fit(X_train, Y_train, validation_split=0.1, epochs=e, batch_size=b, verbose=1)
mid = time.time()
# ,validation_split = 0.1
metrics_model = model.evaluate(X_test, Y_test)
predictions_nn = model.predict(X_test)
predictions_nn = (predictions_nn > 0.5)
accuracy_score_nn.append(accuracy_score(Y_test, predictions_nn))
model.evaluate(X_test, Y_test)

from sklearn.metrics import multilabel_confusion_matrix

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)
cc = multilabel_confusion_matrix(Y_test, y_pred)

TN = 0
for i in range(0, len(cc)):
    TN = TN + cc[i][0][0]

FN = 0
for i in range(0, len(cc)):
    FN = FN + cc[i][1][0]

TP = 0
for i in range(0, len(cc)):
    TP = TP + cc[i][1][1]

FP = 0
for i in range(0, len(cc)):
    FP = FP + cc[i][0][1]

precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * TP / (2 * TP + FP + FN)

precison_score_nn.append(precision)
recall_score_nn.append(recall)

f1_score_nn.append(f1)

# tn,fp,fn,tp=confusion_matrix(Y_test,predictions_nn).ravel()
# mcc_nn.append(((TP*TN)-(FP*FN))/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
# fpr, tpr, threshold = roc_curve(Y_test,predictions_nn)
# roc_auc_nn.append(auc(fpr, tpr))
tn_nn.append(TN)
fp_nn.append(FP)
fn_nn.append(FN)
tp_nn.append(TP)
end = time.time()
time_nn.append(mid - start)
test_nn.append(end - mid)
cost_nn.append(((FP) * 100) + ((FN) * 1000))
# epoch_nn.append((e_v))
# batch_nn.append((b_s))
metrices_obtained.append(metrics_model)

y_pred=model.predict(X_train)
print("training accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_train))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

y_pred=model.predict(X_test)
print("testing accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_test))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

model.save("D/my_model_9_13_4_LAYERS")
np.save('D/my_history_9_14_4_LAYERS.npy', model.history.history)
del model'''

'''
SO FAR THE MOST PROMISING 
SAME PARAMETERS AS IN THE PAPER
BETTER RESULTS 
PAPER SAYS 60% TESTING 
180/180 [==============================] - 179s 784ms/step - loss: 245788.8125 - accuracy: 0.7476 - val_loss: 201948.5625 - val_accuracy: 0.7570
7/7 [==============================] - 11s 12ms/step - loss: 250276.7969 - accuracy: 0.7571
7/7 [==============================] - 0s 12ms/step - loss: 250276.7969 - accuracy: 0.7571
training accuracy
58.752653657165155
testing accuracy
58.411566735584316
'''




###########################################################################################################################################################################
###########################################################################################################################################################################
###########################################################################################################################################################################
############################################################################Other matrices for training#############################
###########################################################################################################################################################################
##########################################################################################################################################################################
###########################################################################################################################################################################
##########################################################################################################################################################################


p = np.sum(Y_train, axis=0)
pos = np.sum(p)
tot = len(Y_train) * len(Y_train[0])
neg = tot - pos
# initial_bias = np.log([pos/neg]) #Could use this as well
initial_bias = pos / (neg + pos)
output_bias = tf.keras.initializers.Constant(initial_bias)


positive_weights = {}
negative_weights = {}
for c in range(0,len(Y_train[0])):
    positive_weights[c] = Y_train.shape[0]/(2*np.count_nonzero(Y_train[c][:]==1))
    negative_weights[c] = Y_train.shape[0]/(2*np.count_nonzero(Y_train[c][:]==0))
#print(positive_weights)
#print(negative_weights)

class_weight = {0: negative_weights, 1: positive_weights}

import tensorflow
def loss_fn(y_true,y_pred):
    loss = 0
    for i in range(0,len(Y_train[0])):
      loss -= (positive_weights[i]*y_true[0]*tensorflow.keras.backend.log(y_pred[0]) + negative_weights[1]*(1-y_true[0])*tensorflow.keras.backend.log(1-y_pred[0]))


    return loss


start = time.time()

# accuracy: (tp + tn) / (tp + tn + fp + fn)
# precision tp / (tp + fp)
# recall: tp / (tp + fn)
# f1: 2 tp / (2 tp + fp + fn)
#G-Mean = sqrt(Sensitivity * Specificity)


METRICS = [
    # keras.metrics.TruePositives(name='tp'),
    # keras.metrics.FalsePositives(name='fp'),
    # keras.metrics.TrueNegatives(name='tn'),
    # keras.metrics.FalseNegatives(name='fn'),
    #keras.metrics.BinaryAccuracy(name='accuracy'),
    # keras.metrics.Precision(name='precision'),
    # keras.metrics.Recall(name='recall'),
    # keras.metrics.AUC(name='auc'),
    # keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
    tfa.metrics.MatthewsCorrelationCoefficient(num_classes=len(Y_train[0]),name='MatthewsCorrelationCoefficient'), #Trying something new
    #tfa.metrics.HammingLoss(num_classes=len(Y_train[0]),mode='multilabel',name='hamming_loss')
    # tfa.metrics.F1Score(num_classes=len(result[0]),name='f1_score')
    #tfa.metrics.Mean() #https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/
    #keras.backend.sqrt( keras.metrics.Sensitivity()*keras.metrics.Specificity())
    #tf.keras.metrics.SpecificityAtSensitivity(0.3)
    #tf.compat.v1.metrics.mean_per_class_accuracy()
    #tf.keras.metrics.CategoricalAccuracy(name='categorical_accuracy', dtype=None) #categorical crossentropy when one sample can have multiple classes or labels are soft probabilities (like [0.5, 0.3, 0.2]).
    

]

p = np.sum(Y_train, axis=0)
pos = np.sum(p)
tot = len(Y_train) * len(Y_train[0])
neg = tot - pos
# initial_bias = np.log([pos/neg])
initial_bias = pos / (neg + pos)
output_bias = tf.keras.initializers.Constant(initial_bias)

model = Sequential()
initializer = tf.keras.initializers.HeNormal()
model.add(Dense(3500, activation='LeakyReLU', input_shape=(len(X_train[0]),)))
model.add(Dense(2500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(1500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(1000, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(1000, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(1500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(2500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
model.add(Dense(3500, activation='relu',kernel_initializer=initializer,
    bias_initializer='zeros'))
#model.add(Dense(1500, activation='relu'))


# model.add(Dense(1500, activation='relu')) #Added on 6-25-2021

model.add(Dense(len(Y_train[0]), activation='sigmoid', bias_initializer=output_bias))

model.summary()
e = 100
b = 1500
tf.keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=100, verbose=0, mode="auto", baseline=None,
                                 restore_best_weights=True)
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=1e-2, decay_steps=10, decay_rate=0.9)
tf.keras.optimizers.Adam(learning_rate=lr_schedule, beta_1=0.8, beta_2=0.999, epsilon=1e-07, name="Adam")
model.compile(optimizer="Adam", loss=loss_fn, metrics=METRICS)
# model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
# print(e_v, "  ", b_s)

history = model.fit(X_train, Y_train, validation_split=0.1, epochs=e, batch_size=b, verbose=1)
mid = time.time()
# ,validation_split = 0.1
metrics_model = model.evaluate(X_test, Y_test)
predictions_nn = model.predict(X_test)
predictions_nn = (predictions_nn > 0.5)
accuracy_score_nn.append(accuracy_score(Y_test, predictions_nn))
model.evaluate(X_test, Y_test)

from sklearn.metrics import multilabel_confusion_matrix

y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)
cc = multilabel_confusion_matrix(Y_test, y_pred)

TN = 0
for i in range(0, len(cc)):
    TN = TN + cc[i][0][0]

FN = 0
for i in range(0, len(cc)):
    FN = FN + cc[i][1][0]

TP = 0
for i in range(0, len(cc)):
    TP = TP + cc[i][1][1]

FP = 0
for i in range(0, len(cc)):
    FP = FP + cc[i][0][1]

precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * TP / (2 * TP + FP + FN)

precison_score_nn.append(precision)
recall_score_nn.append(recall)

f1_score_nn.append(f1)

# tn,fp,fn,tp=confusion_matrix(Y_test,predictions_nn).ravel()
# mcc_nn.append(((TP*TN)-(FP*FN))/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
# fpr, tpr, threshold = roc_curve(Y_test,predictions_nn)
# roc_auc_nn.append(auc(fpr, tpr))
tn_nn.append(TN)
fp_nn.append(FP)
fn_nn.append(FN)
tp_nn.append(TP)
end = time.time()
time_nn.append(mid - start)
test_nn.append(end - mid)
cost_nn.append(((FP) * 100) + ((FN) * 1000))
# epoch_nn.append((e_v))
# batch_nn.append((b_s))
metrices_obtained.append(metrics_model)

y_pred=model.predict(X_train)
print("training accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_train))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

y_pred=model.predict(X_test)
print("testing accuracy")
accuracy =(1-sum(sum(abs(y_pred-Y_test))/len(y_pred))/len(y_pred[0]))*100
print(accuracy)

model.save("D/my_model_9_13_4_LAYERS")
np.save('D/my_history_9_14_4_LAYERS.npy', model.history.history)

from sklearn.metrics import classification_report
import numpy as np


y_pred = model.predict(X_test)
print(classification_report(Y_test, y_pred))

'''
7/7 [==============================] - 11s 13ms/step - loss: 239957.5625 - MatthewsCorrelationCoefficient: 0.0000e+00 - hamming_loss: 0.0296
7/7 [==============================] - 0s 13ms/step - loss: 239957.5625 - MatthewsCorrelationCoefficient: 0.0000e+00 - hamming_loss: 0.0296
training accuracy
56.197433798791586
testing accuracy
56.21659890747848


7/7 [==============================] - 11s 11ms/step - loss: 258649.0469 - MatthewsCorrelationCoefficient: -0.0072
7/7 [==============================] - 0s 11ms/step - loss: 258649.0469 - MatthewsCorrelationCoefficient: -0.0072
training accuracy
64.06643720594701
testing accuracy
64.09519382760332



Epoch 17/20
180/180 [==============================] - 142s 788ms/step - loss: 212049.0469 - MatthewsCorrelationCoefficient: 1.7634e-04 - val_loss: 188399.4219 - val_MatthewsCorrelationCoefficient: 3.9253e-04
Epoch 18/20
180/180 [==============================] - 141s 786ms/step - loss: 211422.5625 - MatthewsCorrelationCoefficient: 1.5741e-04 - val_loss: 189519.3906 - val_MatthewsCorrelationCoefficient: 3.9677e-04
Epoch 19/20
180/180 [==============================] - 143s 795ms/step - loss: 211895.4219 - MatthewsCorrelationCoefficient: 1.0112e-04 - val_loss: 190232.5625 - val_MatthewsCorrelationCoefficient: 7.9613e-04
Epoch 20/20
180/180 [==============================] - 141s 786ms/step - loss: 208047.6250 - MatthewsCorrelationCoefficient: -2.5797e-04 - val_loss: 187531.2969 - val_MatthewsCorrelationCoefficient: 2.9758e-04
7/7 [==============================] - 11s 13ms/step - loss: 217491.7656 - MatthewsCorrelationCoefficient: 0.0000e+00
7/7 [==============================] - 0s 13ms/step - loss: 217491.7656 - MatthewsCorrelationCoefficient: 0.0000e+00
training accuracy
53.59009768133433
testing accuracy
53.53736312620313

180/180 [==============================] - 185s 819ms/step - loss: 234296.3438 - hamming_loss: 0.0301 - val_loss: 186904.6406 - val_hamming_loss: 0.0298
7/7 [==============================] - 11s 13ms/step - loss: 242508.3125 - hamming_loss: 0.0296
7/7 [==============================] - 0s 12ms/step - loss: 242508.3125 - hamming_loss: 0.0296
training accuracy
58.83860663643219
testing accuracy
58.952588281712

To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 2500)              5222500
_________________________________________________________________
dense_1 (Dense)              (None, 2000)              5002000
_________________________________________________________________
dense_2 (Dense)              (None, 1500)              3001500
_________________________________________________________________
dense_3 (Dense)              (None, 1000)              1501000
_________________________________________________________________
dense_4 (Dense)              (None, 500)               500500
_________________________________________________________________
dense_5 (Dense)              (None, 1000)              501000
_________________________________________________________________
dense_6 (Dense)              (None, 1500)              1501500
_________________________________________________________________
dense_7 (Dense)              (None, 1044)              1567044
=================================================================
Total params: 18,797,044
Trainable params: 18,797,044
Non-trainable params: 0
_________________________________________________________________
2021-09-14 17:50:12.321865: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:185] None of the MLIR Optimization Passes are enabled (registered 2)
180/180 [==============================] - 219s 1s/step - loss: 232010.6562 - accuracy: 0.7483 - val_loss: 192564.7031 - val_accuracy: 0.7566
7/7 [==============================] - 11s 31ms/step - loss: 244615.0938 - accuracy: 0.7552
7/7 [==============================] - 0s 32ms/step - loss: 244615.0938 - accuracy: 0.7552


training accuracy
59.53636768835361
testing accuracy
59.53796314743573


1/7 [===>..........................] - ETA: 0s - loss: 231250.9375 - accuracy: 0.7452 - MatthewsCorrelationCoefficien2/7 [=======>......................] - ETA: 0s - loss: 171278.0312 - accuracy: 0.7434 - MatthewsCorrelationCoefficien3/7 [===========>..................] - ETA: 0s - loss: 201295.9531 - accuracy: 0.7412 - MatthewsCorrelationCoefficien4/7 [================>.............] - ETA: 0s - loss: 228038.7188 - accuracy: 0.7398 - MatthewsCorrelationCoefficien5/7 [====================>.........] - ETA: 0s - loss: 277419.8125 - accuracy: 0.7394 - MatthewsCorrelationCoefficien6/7 [========================>.....] - ETA: 0s - loss: 269271.5625 - accuracy: 0.7382 - MatthewsCorrelationCoefficien7/7 [==============================] - 0s 48ms/step - loss: 267775.6250 - accuracy: 0.7385 - MatthewsCorrelationCoefficient: 0.0000e+00
training accuracy
61.69523581990338
testing accuracy
61.58614200883152


_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 3500)              7311500
_________________________________________________________________
dense_1 (Dense)              (None, 2500)              8752500
_________________________________________________________________
dense_2 (Dense)              (None, 1500)              3751500
_________________________________________________________________
dense_3 (Dense)              (None, 1000)              1501000
_________________________________________________________________
dense_4 (Dense)              (None, 500)               500500
_________________________________________________________________
dense_5 (Dense)              (None, 1000)              501000
_________________________________________________________________
dense_6 (Dense)              (None, 1500)              1501500
_________________________________________________________________
dense_7 (Dense)              (None, 2500)              3752500
_________________________________________________________________
dense_8 (Dense)              (None, 3500)              8753500
_________________________________________________________________
dense_9 (Dense)              (None, 1044)              3655044
=================================================================
Total params: 39,980,544
Trainable params: 39,980,544
Non-trainable params: 0
_________________________________________________________________
2021-09-16 12:54:05.513391: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:185] None of the MLIR Optimization Passes are enabled (registered 2)
180/180 [==============================] - 294s 1s/step - loss: 247880.5156 - categorical_accuracy: 0.0069 - val_loss: 186661.0000 - val_categorical_accuracy: 0.0090
7/7 [==============================] - 12s 57ms/step - loss: 240267.6875 - categorical_accuracy: 0.0050
7/7 [==============================] - 0s 59ms/step - loss: 240267.6875 - categorical_accuracy: 0.0050
training accuracy
57.33001135493863
testing accuracy
57.3298002648456

Next step -
https://machinelearningmastery.com/threshold-moving-for-imbalanced-classification/



'''