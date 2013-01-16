import pandas
from sklearn.svm import LinearSVC

data = pandas.read_csv('../data/accurate-dataset.csv')
n_samples = len(data)

train = data[:132]
test = data[132:]

clf = LinearSVC()
X = train.ix[:, :'y']
y =  train.ix[:, 'result':]
clf = clf.fit(X, y)


