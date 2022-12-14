# -*- coding: utf-8 -*-
"""Artificial Neural Network

# This code is generated by Dr. Kazi Monzure Khoda

### Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error
from keras.callbacks import EarlyStopping 
from keras.callbacks import ModelCheckpoint

tf.__version__

"""## Part 1 - Data Preprocessing

### Importing the dataset
"""

dataset = pd.read_excel('WGR1b.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:, 0:7])
X[:, 0:7] = imputer.transform(X[:, 0:7])

"""### Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1) #, random_state = 0


## Part 2 - Building the ANN
ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=100, activation='relu', input_dim = 6))
ann.add(tf.keras.layers.Dense(units=100, activation='relu'))
ann.add(tf.keras.layers.Dense(units=100, activation='relu'))
ann.add(tf.keras.layers.Dense(units=100, activation='relu'))

ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer = 'adam', loss = 'mean_squared_error',loss_weights={}, weighted_metrics={})  # , metrics=["mae", "acc"]


checkpointer = ModelCheckpoint(filepath='results.h5', monitor='val_loss', save_best_only=True)
early_stopping_monitor = EarlyStopping(monitor='loss', min_delta=0.000005, patience =20000, verbose=1, mode='min', baseline=.000005, restore_best_weights=False)
history_mse = ann.fit(X_train, y_train, batch_size = 32, epochs = 20000, callbacks = [checkpointer,early_stopping_monitor], verbose = 1, validation_split = 0.1)


print('Loss:    ', history_mse.history['loss'][-1], '\nVal_loss: ', history_mse.history['val_loss'][-1])

# EVALUATE MODEL IN THE TEST SET
score_mse_test = ann.evaluate(X_test, y_test)
print('Test Score:', score_mse_test)

# EVALUATE MODEL IN THE TRAIN SET
score_mse_train = ann.evaluate(X_train, y_train)
print('Train Score:', score_mse_train)

"""### Training the ANN model on the Training set"""

#ann.fit(X_train, y_train, batch_size = 32, epochs = 20000)

#ann.save('my_model_epoxyR4')
# R4 has 1.0216e-09 so far the best
# ann.save('my_model_epoxyR5') also good
# ann.save('my_model_epoxyR6') # R6 is the best 

ann.save('my_model_WGR1_4')
"""### Predicting the results of the Test set"""

#y_pred = ann.predict(np.array([[4.795,	2.54,	206.633,	2.059,	0.53,	0.901]]))
#y_pred = ann.predict(np.array([[12.95, 0.35, 13.30, 0.8, 35.8, 700, 20, 30 ]]))
#y_pred = ann.predict(np.array([[6.025, 3.295, 271.808, 2.422, 0.596, 0.901, 0.261, 0.309, 37.799, 0.369, 1.247, 0.964, 0.374, 0.363, 56.825, 0.523, 1.142, 0.974]]))
y_pred1 = ann.predict(np.array([[0.45,	0.29,	0.64,	0.45,	1,	2.11]]))
y_pred2 = ann.predict(np.array([[0.5,	0.41,	0.82,	0.51,	0.98,	2.72]]))
y_pred3 = ann.predict(np.array([[0.52,	0.49,	0.94,	0.44,	1.18,	3.13]]))
y_pred4 = ann.predict(np.array([[0.57,	0.35,	0.62,	0.58,	0.98,	3.48]]))
y_pred5 = ann.predict(np.array([[0.65,	0.39,	0.59,	0.67,	0.97,	3.57]]))
y_pred6 = ann.predict(np.array([[0.76,	0.56,	0.74,	0.75,	1.01,	4.08]]))
#max
#y_pred7 = ann.predict(np.array([[0.14,	0.29,	0.12,	0.39,	0.14,	2.11]]))
#y_pred8 = ann.predict(np.array([[0.348,	0.734,	0.436,	0.622,	0.641,	3.586]]))
y_pred9 = ann.predict(np.array([[0.65,	1.306,	0.94,	1.2,	1.18,	5.45]]))




fig = plt.figure(figsize=(12,6))
#plt.figure(figsize=(15, 6))
#ax = fig.add_subplot(211)
plt.plot(history_mse.history['loss'], lw =3, ls = '--', label = 'Loss')
plt.plot(history_mse.history['val_loss'],lw =2, ls = '-', label = 'Val Loss')
plt.xlabel('Epochs', fontsize=15)
plt.ylabel('Loss', fontsize=15)
plt.title('MSE')
plt.legend()
plt.show()

#history_mse.history['loss'][19000:200000]
#min_w = min(history_mse.history['loss'])
