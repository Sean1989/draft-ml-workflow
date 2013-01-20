from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import metrics

def linear_svc(X_train, y_train):
    print "Training: Linear support vector classification..."
    clf = LinearSVC()
    clf = clf.fit(X_train, y_train)
    return clf

def svc_with_rbf_kernel(X_train, y_train):
    print "Training: SVC with a Radial Basis Function (RBF) kernel..."
    svc = SVC(kernel='rbf')
    svc.fit(X_train, y_train)
    return svc

