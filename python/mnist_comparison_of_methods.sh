#!/bin/bash

(
    echo "===================================="
    echo "K-nearest neighbors:"
    echo "===================================="
    python mnist_knn.py
    echo
    echo "===================================="
    echo "Support vector machines:"
    echo "===================================="
    python mnist_svm.py
    echo
    echo "===================================="
    echo "Random forest:"
    echo "===================================="
    python mnist_random-forest.py
    echo
) > ../experiments/results/mnist_comparison_of_methods.txt
