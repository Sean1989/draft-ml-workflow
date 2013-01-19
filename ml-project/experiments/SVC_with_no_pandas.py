import numpy as np
from numpy import genfromtxt
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import preprocessing

# Read the data

data = genfromtxt('../data/float_features_dataset.csv', delimiter=',', skiprows=1)
n_samples = len(data)

# Scale features

data[:, 0:-1] = preprocessing.scale(data[:,0:-1])

# Split it into train and test sets

boundary = int(n_samples * 0.6)
train, test = data[:boundary], data[boundary:]
X_train, X_test = np.delete(train,-1,1), np.delete(test,-1,1)
y_train, y_test = train[:,-1], test[:,-1]

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

#In [86]: metrics.precision_score(y_test, y_pred)  
#Out[86]: 1.0

#In [87]: metrics.recall_score(y_test, y_pred)     
#Out[87]: 1.0

#In [88]: metrics.f1_score(y_test, y_pred)         
#Out[88]: 1.0


