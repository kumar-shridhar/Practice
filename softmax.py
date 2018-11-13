import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.

L=[5,6,7]
def softmax(L):
    return np.divide(np.exp(L), np.exp(L).sum())
