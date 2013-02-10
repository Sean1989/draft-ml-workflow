""" Repeating selected steps from the tutorial:

    http://nbviewer.ipython.org/urls/raw.github.com/temporaer/
    tutorial_ml_gkbionics/master/
    5%2520-%2520k%2520Nearest%2520Neighbors.ipynb

"""
from sklearn import metrics
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from classification import *
from mnist import MNIST
import time


def run(data_path):
    print "Reading the dataset:", data_path
    mn = MNIST(data_path)
    X_train, y_train = mn.load_training()
    X_test, y_test = mn.load_testing()

    # Trunk the data
    X_digits, y_digits = shuffle(X_train, y_train)

    X_digits_train = X_digits[:1000]
    y_digits_train = y_digits[:1000]
    X_digits_valid = X_digits[1000:2000]
    y_digits_valid = y_digits[1000:2000]
    X_digits_test = X_digits[2000:3000]
    y_digits_test = y_digits[2000:3000]

    knn_digits = KNeighborsClassifier(n_neighbors=10)
    knn_digits.fit(X_digits_train, y_digits_train)
    print "KNN validation accuracy on MNIST digits: ",
    print knn_digits.score(X_digits_valid, y_digits_valid)

"""    # Apply a learning algorithm
    print "Applying a learning algorithm..."
    clf = default_svc(X_train, y_train)

    # Make a prediction
    print "Making predictions..."
    y_pred = clf.predict(X_test)

    # Evaluate the prediction
    print "Evaluating results..."
    print "Precision: \t", metrics.precision_score(y_test, y_pred)
    print "Recall: \t", metrics.recall_score(y_test, y_pred)
    print "F1 score: \t", metrics.f1_score(y_test, y_pred)
    print "Mean accuracy: \t", clf.score(X_test, y_test)
"""

if __name__ == "__main__":
    start_time = time.time()
    data_path = "../data/mnist"
    results = run(data_path)
    end_time = time.time()
    print "Overall running time:", end_time - start_time
