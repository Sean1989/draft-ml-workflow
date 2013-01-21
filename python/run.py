import sys
import yaml
from numpy import genfromtxt
from sklearn import preprocessing
from sklearn import metrics
from classification import *
from datetime import datetime
import re


def run(data_path, algorithm):
    # Read the data
    print "Reading the dataset:", data_path
    data = genfromtxt(data_path, delimiter=',', skip_header=1)
    n_samples = len(data)

    # Scale features
    data[:, 0:-1] = preprocessing.scale(data[:, 0:-1])

    # Split it into train and test sets
    boundary = int(n_samples * 0.6)
    train, test = data[:boundary], data[boundary:]
    X_train, X_test = train[:, :-1], test[:, :-1]
    y_train, y_test = train[:, -1], test[:, -1]

    # Apply a learning algorithm
    try:
        training_algorithm = globals()[algorithm]
        clf = training_algorithm(X_train, y_train)
    except KeyError:
        print "Training algorithm is not located. Please check it again."
        raise

    # Make a prediction
    y_pred = clf.predict(X_test)

    # Evaluate the prediction
    print "Evaluating results..."
    results = dict()
    results['Precision'] = float(metrics.precision_score(y_test, y_pred))
    results['Recall'] = float(metrics.recall_score(y_test, y_pred))
    results['F1 score'] = float(metrics.f1_score(y_test, y_pred))

    print "Precision: \t", results['Precision']
    print "Recall: \t", results['Recall']
    print "F1 score: \t", results['F1 score']

    return results


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        options = yaml.load(open(path))
    except IndexError:
        print "No options file (.yaml) found. Running the default experiment."
        path = '../experiments/default.yaml'
        options = yaml.load(open(path))
    except yaml.scanner.ScannerError:
        print "Error when scanning the options file (.yaml):" +\
            "please check it again."
        raise
    except:
        print "Something went wrong:\n", sys.exc_info()[0]
        raise

    results = run(options['Data'], options['Algorithm'])

    # Write options and results into an output file

    m = re.search('([^/]*)\.yaml', path)
    input_filename = m.group(0)
    output_path = path[0:path.index(input_filename)] + 'results/' +\
        input_filename[0:input_filename.index('.yaml')] + '_' +\
        datetime.now().strftime("%Y%m%d_%H%M") + '.yaml'

    with open(output_path, 'wb') as f:
        yaml.dump(options, f, default_flow_style=False)
        yaml.dump(results, f, default_flow_style=False)
