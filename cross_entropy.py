import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    return -np.sum(np.float_(Y) * np.log(np.float_(P)) + (1 - np.float_(Y)) * np.log(1 - np.float_(P)))
