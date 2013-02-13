import numpy as np
from sklearn import metrics
from sklearn.datasets import fetch_mldata
from sklearn.utils import shuffle
from numpy import arange
from classification import *
import time
import random


def run(data_path):
    print "Reading the dataset:", data_path
    
    ## http://continuum.io/blog/wiserf-use-cases-and-benchmarks

    mnist = fetch_mldata('MNIST original')
    mnist.data, mnist.target = shuffle(mnist.data, mnist.target)
 
    # Define training and testing sets
    inds = arange(len(mnist.data))
    test_i = random.sample(xrange(len(inds)), int(0.1*len(inds)))
    train_i = np.delete(inds, test_i)

    X_train = mnist.data[train_i].astype(np.double)
    y_train = mnist.target[train_i].astype(np.int)
 
    X_test = mnist.data[test_i].astype(np.double)
    y_test = mnist.target[test_i].astype(np.int)

    # Trunk the data
    X_train, y_train = X_train[:600], y_train[:600]
    X_test, y_test = X_test[:100], y_test[:100]

    # Apply a learning algorithm
    print "Applying a learning algorithm..."
    clf = default_svc(X_train, y_train)

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


if __name__ == "__main__":
    start_time = time.time()
    data_path = "../data/mnist"
    results = run(data_path)
    end_time = time.time()
    print "Overall running time:", end_time - start_time
