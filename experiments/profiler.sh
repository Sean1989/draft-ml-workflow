# Running SVC on MNIST with plop profiler
#
# plop, Python low-overhead profiler
# https://github.com/bdarnell/plop
#
python -m plop.collector mnist_run.py
python -m plop.viewer --datadir=/tmp
