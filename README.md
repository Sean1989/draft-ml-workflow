softml: Semi-supervised learning
======
Work in progress. More details later.

# How to run an experiment

    cd python
    python run.py

This will run the default experiment (../experiments/default.yaml).

You can use another YAML file as a parameter:

    python run.py ../experiments/svn_rbf.yaml

Feel free to check out the ../experiments directory to see how to define a YAML file with experiment settings.

# Project structure

* __data__: for data files used in the experiments. Some of them are available from [UCL Machine Learning Repository](http://www.ics.uci.edu/~mlearn/) and were not redistributed here.

* __experiments__: files that define experiment parameters (what dataset is used, what algorithm etc.) This should help to reproduce the results for each experiment.

* __experiments/results__: automatically generated files that contain a result of each experiment. File names are generated automatically as well: file name of the initial experiment and a time stamp.

* __python__: my Python code to run the experiments. Under construction.
