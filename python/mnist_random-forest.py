from sklearn import metrics
from classification import *
from mnist import MNIST
from sklearn.ensemble import RandomForestClassifier
import time


def run(data_path):
    print "Reading the dataset:", data_path
    mn = MNIST(data_path)
    X_train, y_train = mn.load_training()
    X_test, y_test = mn.load_testing()

    # Trunk the data
    X_train, y_train = X_train[:600], y_train[:600]
    X_test, y_test = X_test[:100], y_test[:100]

    # Apply a learning algorithm
    print "Applying a learning algorithm..."
    clf = RandomForestClassifier(n_estimators=10, n_jobs=1)
    clf.fit(X_train, y_train)

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
