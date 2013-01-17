import pandas
from sklearn.svm import LinearSVC

# Read the data

data = pandas.read_csv('../data/accurate-dataset.csv')
n_samples = len(data)

# Split it into train and test sets

boundary = int(n_samples * 0.6)
train = data[:boundary]
test = data[boundary:]
del test['result']

# Fit a Linear Support Vector Classification model

clf = LinearSVC()
X = train.ix[:, :'y']
y =  train.ix[:, 'result':]
clf = clf.fit(X, y)




