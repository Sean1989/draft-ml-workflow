#!/bin/bash

(
    echo "===================================="
    echo "K-nearest neighbors:"
    echo "===================================="

    for (( i = 1 ; i <= 200; i++ )) 
    do
          python mnist_knn.py | grep 'Overall running time'
    done
    
    echo
    echo "===================================="
    echo "Support vector machines:"
    echo "===================================="

    for (( i = 1 ; i <= 200; i++ )) 
    do
        python mnist_svm.py  | grep 'Overall running time'
    done

    echo
    echo "===================================="
    echo "Random forest:"
    echo "===================================="

    for (( i = 1 ; i <= 200; i++ )) 
    do
        python mnist_random-forest.py  | grep 'Overall running time'
    done

    echo
)

# > ../experiments/results/mnist_comparison_of_methods_.txt
