from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def linear_svc(X_train, y_train):
    print "Training: Linear support vector classification..."
    clf = LinearSVC()
    clf = clf.fit(X_train, y_train)
    return clf


def svc_rbf(X_train, y_train):
    print "Training: SVC with a Radial Basis Function (RBF) kernel..."

    # Grid search
    # http://scikit-learn.org/dev/auto_examples/grid_search_digits.html

    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                        'C': [1, 10, 100, 1000]},
                        {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

    scores = [
        ('precision', precision_score),
        ('recall', recall_score),
    ]

    for score_name, score_func in scores:
        clf = GridSearchCV(SVC(C=1), tuned_parameters, score_func=score_func)
        clf.fit(X_train, y_train, cv=5)

        print "Best parameters set found on development set:"
        print
        print clf.best_estimator_
        print
        print "Grid scores on development set:"
        print
        for params, mean_score, scores in clf.grid_scores_:
            print "%0.3f (+/-%0.03f) for %r" % (
                mean_score, scores.std() / 2, params)

    svc = SVC(kernel='rbf')
    svc.fit(X_train, y_train)
    return svc
