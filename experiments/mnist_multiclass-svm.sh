#!/bin/bash

(
    for i in {1..10}
    do
        echo "===================================="
        echo "Attempt #$i"
        echo "===================================="
        python mnist_svm.py 
        echo ""
    done
) > ../experiments/results/mnist_svm_20130213_1500.txt
