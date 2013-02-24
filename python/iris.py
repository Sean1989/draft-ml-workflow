from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn import metrics


# Load the data
iris = load_iris()

# 200-fold cross-validation
# as in Table 6 of the following paper:
""" 
    A New Approach for Handling the Iris Data Classification Problem.
    Shyi-Ming Chen and Yao-De Fang. 
    International Journal of Applied Science and Engineering
    2005. 3, 1: 37- 49
"""

average_score = 0
n_folds = 200

for i in range(n_folds):

    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.4, random_state=i)

    clf = SVC(kernel='rbf')
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    
    print "Precision:\t", metrics.precision_score(y_test, y_pred)
    print "Recall:\t", metrics.recall_score(y_test, y_pred)
    print "F1 score:\t", metrics.f1_score(y_test, y_pred)
    print "Mean accuracy:\t", clf.score(X_test, y_test)
    average_score += clf.score(X_test, y_test)
    print

    print "Classification report:", metrics.classification_report(y_test, y_pred, 
                                      target_names=iris.target_names)
    print "=" * 40

average_score /= n_folds
print "Overall average score:", average_score
