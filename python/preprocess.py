# Preprocessing tools:
# 	- Generate X training examples per class
#	- Generate Y pairwise constraints

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing


def preprocess(raw_data, options=0):
    
    # Scale features
    features = preprocessing.scale(raw_data[:, 0:-1])
    target = raw_data[:, -1]

    # Split it into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.33, random_state=17)

    return [X_train, X_test, y_train, y_test]

