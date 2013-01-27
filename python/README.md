Semi-supervised learning with pairwise constraints
======

# Setting

* a small amount of labelled data; 
* a large amount of unlabelled data with partial information in the form of pairwise constraints ("Do A and B belong to the same class?").

# Input:
* Labeled data: (x_i, y_i) - 
_n_ samples.
* Partially labeled data in the form of pairwise constraints: 
(x_a, x_b, +1/-1): 
+1 if they belong to the same class, 
-1 otherwise -
_m_ samples.

__References__: 

1. Brian Kulis et al. Semi-supervised graph clustering: a kernel approach. ICML 2005 
http://dl.acm.org/citation.cfm?id=1102351.1102409

2. Nam Nguyen and Rich Caruana. Improving Classification with Pairwise Constraints: A Margin-Based Approach. ECML PKDD 2008.
http://link.springer.com/chapter/10.1007%2F978-3-540-87481-2_8?LI=true

