#!/bin/bash

(
    for i in {1..10}
    do
        echo "Attempt #$i"
        python mnist_random-forest.py | grep "Overall running time"
        echo ""
    done
) > ../experiments/results/mnist_rf_runtimes-with-mnist-package.txt
