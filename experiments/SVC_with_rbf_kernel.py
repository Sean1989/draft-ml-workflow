import pandas
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import preprocessing

# Read the data

data = pandas.read_csv('../data/float_features_dataset.csv')
n_samples = len(data)

# Preprocessing

data.x = preprocessing.scale(data.x)
data.y = preprocessing.scale(data.y)

# Split it into train and test sets

boundary = int(n_samples * 0.6)
train, test = data[:boundary], data[boundary:]
X_train, X_test = train.ix[:, :'y'], test.ix[:, :'y']
y_train, y_test = train.ix[:, 'result':], test.ix[:, 'result':]
y_train = [int(i) for i in y_train.values]

# Apply a learning algorithm

svc = SVC(kernel='rbf')
svc.fit(X_train.values, y_train)

# Make a prediction

y_pred = svc.predict(X_test)

# Simplify y_test to compare it with y_pred

y_test = [int(i) for i in y_test.values]

# Evaluate the prediction

metrics.precision_score(y_test, y_pred)  
metrics.recall_score(y_test, y_pred)     
metrics.f1_score(y_test, y_pred)         


# Experiment results:
# Precision     1.0
# Recall        1.0
# F1 score      1.0
