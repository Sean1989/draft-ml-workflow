## Procedures for reading datasets of different types 
## * Function `numbers` works for comma-separated files with real or integer numbers 
## * Convert categorical or text features here.

from numpy import genfromtxt

def numbers(data_path):
    raw_data = genfromtxt(data_path, delimiter=',')
    return raw_data
