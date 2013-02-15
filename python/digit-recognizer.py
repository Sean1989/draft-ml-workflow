import time
import random
from numpy import arange
from numpy import genfromtxt
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics


# Remember starting time
start_time = time.time()

# Read data
print "Reading the data..."
data_path = '../data/digit-recognizer/train.csv'
raw_data = genfromtxt(data_path, skip_header=1, delimiter=',')

# Trunk the data
n_train = 600
n_test = 400

# Define training and testing sets
print "Splitting into a training and a testing set..."
indices = arange(len(raw_data))
random.seed(0)
train_idx = random.sample(indices, n_train)
test_idx = random.sample(indices, n_test)
X_train, y_train = raw_data[train_idx, 1:], raw_data[train_idx, 0]
X_test, y_test = raw_data[test_idx, 1:], raw_data[test_idx, 0]

# Apply a learning algorithm
print "Applying a learning algorithm..."
clf = OneVsRestClassifier(LinearSVC()).fit(X_train, y_train)

# Make a prediction
print "Making predictions..."
y_pred = clf.predict(X_test)

print y_pred

# Evaluate the prediction
print "Evaluating results..."
print "Precision: \t", metrics.precision_score(y_test, y_pred)
print "Recall: \t", metrics.recall_score(y_test, y_pred)
print "F1 score: \t", metrics.f1_score(y_test, y_pred)
print "Mean accuracy: \t", clf.score(X_test, y_test)

# Calculate overall time
end_time = time.time()
print "Overall running time:", end_time - start_time
