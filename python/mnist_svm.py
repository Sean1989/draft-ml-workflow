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
    mnist = fetch_mldata('MNIST original')
    mnist.data, mnist.target = shuffle(mnist.data, mnist.target)

    # Trunk the data
    n_train = 600
    n_test = 400

    # Define training and testing sets
    indices = arange(len(mnist.data))
    random.seed(0)
    train_idx = random.sample(indices, n_train)
    test_idx = random.sample(indices, n_test)
    X_train, y_train = mnist.data[train_idx], mnist.target[train_idx]
    X_test, y_test = mnist.data[test_idx], mnist.target[test_idx]

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
