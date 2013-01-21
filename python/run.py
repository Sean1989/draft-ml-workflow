import sys
import yaml
from numpy import genfromtxt
from sklearn import preprocessing
from sklearn import metrics
from classification import *

def run(data_path, algorithm):
    # Read the data
    print "Reading the dataset:", data_path
    data = genfromtxt(data_path, delimiter=',', skip_header=1)
    n_samples = len(data)

    # Scale features
    data[:, 0:-1] = preprocessing.scale(data[:,0:-1])

    # Split it into train and test sets
    boundary = int(n_samples * 0.6)
    train, test = data[:boundary], data[boundary:]
    X_train, X_test = train[:,:-1], test[:,:-1]
    y_train, y_test = train[:,-1], test[:,-1]

    # Apply a learning algorithm
    try:
        training_algorithm = locals()[algorithm]
        clf = training_algorithm(X_train, y_train)
    except KeyError:
        print "Training algorithm is not located. Please check it again." 
        raise

    # Make a prediction
    y_pred = clf.predict(X_test)

    # Evaluate the prediction
    print "Evaluating results..."
    print "Precision: \t", metrics.precision_score(y_test, y_pred)  
    print "Recall: \t", metrics.recall_score(y_test, y_pred)     
    print "F1 score: \t", metrics.f1_score(y_test, y_pred)        

    # Dump the results in a file
    # ... return results into the main function -> and later save them into ...._results.yaml


if __name__ == "__main__":
    try:
        options = yaml.load(open(sys.argv[1]))
        run(options['Data'], options['Algorithm'])
    except yaml.scanner.ScannerError:
        print "Error when scanning the options file (.yaml): please check it again."
    except IndexError:
        print "No options file (.yaml) found. Running the default experiment."
        options = yaml.load(open('../experiments/default.yaml'))
        run(options['Data'], options['Algorithm'])
    except:
        print "Something went wrong:\n", sys.exc_info()[0]
        raise


