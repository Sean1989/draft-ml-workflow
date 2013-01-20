import classification
from numpy import genfromtxt
from sklearn import preprocessing
from sklearn import metrics

# Read the data

data = genfromtxt('../data/float_features_dataset.csv', delimiter=',', skiprows=1)
n_samples = len(data)

# Scale features

data[:, 0:-1] = preprocessing.scale(data[:,0:-1])

# Split it into train and test sets

boundary = int(n_samples * 0.6)
train, test = data[:boundary], data[boundary:]
X_train, X_test = train[:,:-1], test[:,:-1]
y_train, y_test = train[:,-1], test[:,-1]

# Apply a learning algorithm

svc = svc_with_rbf_kernel(X_train, y_train)

# Make a prediction

y_pred = svc.predict(X_test)

# Evaluate the prediction

metrics.precision_score(y_test, y_pred)  
metrics.recall_score(y_test, y_pred)     
metrics.f1_score(y_test, y_pred)         


