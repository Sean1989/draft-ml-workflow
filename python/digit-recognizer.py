from numpy import genfromtxt
from numpy.random import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics


# Read data
data_path = '../data/digit-recognizer/train_debug.csv'
data = genfromtxt(data_path, skip_header=1, delimiter=',')

# Split it into train and test sets
shuffle(data)
features, target = data[:, 1:], data[:, 1]
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.33, random_state=17)

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

