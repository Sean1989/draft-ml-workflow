# Preprocessing tools:
# 	- Generate X training examples per class
#	- Generate Y pairwise constraints
#
# Partially based on sklearn/cross_validation.py
# (https://github.com/scikit-learn)

import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing


def preprocess(data,
               training_samples_per_class=5,
               pairwise_constraints=10,
               n_iter=10):

    # Shuffle the original data n_iter times
    n_samples = len(data)
    indices = np.arange(n_samples)
    for _ in range(n_iter):
        np.random.shuffle(indices)
    data = data[indices]

    # Scale features
    features = preprocessing.scale(data[:, 0:-1])
    target = data[:, -1]

    # Split it into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.33, random_state=17)

    # Generate pairwise constraints
    constraints = []
    random.seed(0)
    for _ in range(pairwise_constraints):
        i, j = random.sample(indices, 2)
        constraint = 1 if target[i] == target[j] else -1
        constraints += [(features[i], features[j], constraint)]

    print "Resulting pairwise constraints:"
    for item in constraints:
        print item

    return [X_train, X_test, y_train, y_test, constraints]
