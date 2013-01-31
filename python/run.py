import sys
import yaml
from sklearn import metrics
from get_data import *
from classification import *
from preprocess import *
from datetime import datetime
import re


def run(data_path, read_as, algorithm):
    # Read the data
    print "Reading the dataset:", data_path
    try:
        data_reading_function = globals()[read_as]
        raw_data = data_reading_function(data_path)
    except KeyError:
        print "Data reading function is not located. Please check it again."
        raise

    # Preprocess the data
    X_train, X_test, y_train, y_test, constraints = preprocess(raw_data)

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
    results['Mean accuracy'] = clf.score(X_test, y_test)

    print "Precision: \t", results['Precision']
    print "Recall: \t", results['Recall']
    print "F1 score: \t", results['F1 score']
    print "Mean accuracy: \t", results['Mean accuracy']

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

    results = run(options['Data'], options['Read as'], options['Algorithm'])

    # Write options and results into an output file

    m = re.search('([^/]*)\.yaml', path)
    input_filename = m.group(0)
    output_path = path[0:path.index(input_filename)] + 'results/' +\
        input_filename[0:input_filename.index('.yaml')] + '_' +\
        datetime.now().strftime("%Y%m%d_%H%M") + '.yaml'

    with open(output_path, 'wb') as f:
        yaml.dump(options, f, default_flow_style=False)
        yaml.dump(results, f, default_flow_style=False)
