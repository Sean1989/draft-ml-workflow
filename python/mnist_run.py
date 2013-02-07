from sklearn import metrics
from classification import *
from mnist import MNIST


def run(data_path):
    # Read the data
    print "Reading the dataset:", data_path
    mn = MNIST(data_path)
    X_train, y_train = mn.load_training()
    X_test, y_test = mn.load_testing()

    # Apply a learning algorithm
    clf = default_svc(X_train, y_train)

    # Make a prediction
    y_pred = clf.predict(X_test)

    # Evaluate the prediction
    print "Evaluating results..."
    print "Precision: \t", float(metrics.precision_score(y_test, y_pred))
    print "Recall: \t", float(metrics.recall_score(y_test, y_pred))
    print "F1 score: \t", float(metrics.f1_score(y_test, y_pred))
    print "Mean accuracy: \t", float(clf.score(X_test, y_test))


if __name__ == "__main__":
    data_path = "../data/mnist"
    results = run(data_path)
