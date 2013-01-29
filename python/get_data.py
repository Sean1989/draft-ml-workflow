## Procedures for reading datasets of different types
## ____________________________________________________
##
## * Function `numbers` works for comma-separated files
##   with real or integer numbers.
##
## * Convert categorical or text features here.


from numpy import genfromtxt
import csv



def numbers(data_path):
    raw_data = genfromtxt(data_path, delimiter=',')
    return raw_data


def iris(data_path):

    # Read everything the standard function can
    raw_data = genfromtxt(data_path, delimiter=',')

    # Now convert information about classes (NaNs)
    # into something usable.

    # Read the class label for each training sample
    class_labels = []
    with open(data_path) as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            if row:  # is not empty
                class_labels += [row[-1]]

    class_names = list(set(class_labels))
    raw_data[:, -1] = [class_names.index(i) for i in class_labels]

    return raw_data
