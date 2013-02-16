import time
import random
from numpy import arange
from numpy import genfromtxt
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics


# Remember starting time
start_time = time.time()

# Read data
print "Reading the data..."
data_path = '../data/digit-recognizer/'

train_data = genfromtxt(data_path + 'train.csv', skip_header=1, delimiter=',')
X_train, y_train = train_data[:, 1:], train_data[:, 0]

test_data = genfromtxt(data_path + 'test.csv', skip_header=1, delimiter=',')
X_test = test_data

# Apply a learning algorithm
print "Applying a learning algorithm..."
#clf = OneVsRestClassifier(LinearSVC()).fit(X_train, y_train)
clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(X_train, y_train)

# Make a prediction
print "Making predictions..."
y_pred = clf.predict(X_test)

# Write it down in a file
with open('../experiments/results/digit_recognizer_submission_knn.csv', 'wb') as output_file:
    for item in y_pred:
        output_file.write(str(int(item)) + '\n')

# Calculate overall time
end_time = time.time()
print "Overall running time:", end_time - start_time
