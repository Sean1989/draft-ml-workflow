import pandas
from sklearn.svm import LinearSVC
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

# Fit a Linear Support Vector Classification model

clf = LinearSVC()
clf = clf.fit(X_train, y_train)

# Make a prediction

y_pred = clf.predict(X_test)

# Simplify y_test to compare it with y_pred

y_test = [int(i) for i in y_test.values]

# Evaluate the prediction

metrics.precision_score(y_test, y_pred)  
metrics.recall_score(y_test, y_pred)     
metrics.f1_score(y_test, y_pred)         
