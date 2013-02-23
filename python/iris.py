from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn import metrics


# Load the data
iris = load_iris()

# 10-fold cross-validation
for i in range(10):

    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.4, random_state=i)

    clf = SVC(kernel='rbf')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    
    print "Precision:\t", metrics.precision_score(y_test, y_pred)
    print "Recall:\t", metrics.recall_score(y_test, y_pred)
    print "F1 score:\t", metrics.f1_score(y_test, y_pred)
    print "Mean accuracy:\t", clf.score(X_test, y_test)
    print

    print "Classification report:", metrics.classification_report(y_test, y_pred, 
                                      target_names=iris.target_names)
    print "=" * 40


