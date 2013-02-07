from sklearn import metrics
from classification import *
from mnist import MNIST
from time import time, ctime


def run(data_path):
    # Read the data
    print ctime()
    print "Reading the dataset:", data_path
    mn = MNIST(data_path)
    X_train, y_train = mn.load_training()
    X_test, y_test = mn.load_testing()

    # Apply a learning algorithm
    print ctime()
    print "Applying a learning algorithm..."
    clf = default_svc(X_train, y_train)

    # Make a prediction
    print ctime()
    print "Making predictions"
    y_pred = clf.predict(X_test)

    # Evaluate the prediction
    print ctime()
    print "Evaluating results..."
    print "Precision: \t", metrics.precision_score(y_test, y_pred)
    print "Recall: \t", metrics.recall_score(y_test, y_pred)
    print "F1 score: \t", metrics.f1_score(y_test, y_pred)
    print "Mean accuracy: \t", clf.score(X_test, y_test)


if __name__ == "__main__":
    start_time = time()
    data_path = "../data/mnist"
    results = run(data_path)
    end_time = time()
    print "Overall running time:", end_time - start_time
