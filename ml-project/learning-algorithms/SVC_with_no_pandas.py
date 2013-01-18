import numpy as np
from numpy import genfromtxt
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import preprocessing

# Read the data

data = genfromtxt('../data/float_features_dataset.csv', delimiter=',')
n_samples = len(data)

# Split it into train and test sets

boundary = int(n_samples * 0.6)
train, test = data[:boundary], data[boundary:]
X_train, X_test = np.delete(train,-1,1), np.delete(test,-1,1)
y_train, y_test = train[:,-1], test[:,-1]

# Scale features

X_train, X_test = preprocessing.scale(X_train), preprocessing.scale(X_test)

# Apply a learning algorithm

svc = SVC(kernel='rbf')
svc.fit(X_train, y_train)

# Make a prediction

y_pred = svc.predict(X_test)

# Evaluate the prediction

metrics.precision_score(y_test, y_pred)  
metrics.recall_score(y_test, y_pred)     
metrics.f1_score(y_test, y_pred)         


# Experiment results:

#In [472]: metrics.precision_score(y_test, y_pred)  
#Out[472]: 0.5730337078651685

#In [473]: metrics.recall_score(y_test, y_pred)     
#Out[473]: 1.0

#In [474]: metrics.f1_score(y_test, y_pred)         
#Out[474]: 0.72857142857142854

