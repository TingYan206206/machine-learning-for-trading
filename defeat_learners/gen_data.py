"""
template for generating data to fool learners (c) 2016 Tucker Balch
"""

import numpy as np
import math

# this function should return a dataset (X and Y) that will work
# better for linear regression than decision trees
def best4LinReg(seed=1489683273):
    np.random.seed(seed)
    # X = np.zeros((100,2))
    X = np.random.random(size = (50,3))*200-50
    # Here's is an example of creating a Y from randomly generated
    # X with multiple columns
    # Y = X[:,0] + np.sin(X[:,1]) + X[:,2]**2 + X[:,3]**3
    Y = X[:, 0] * 1.0
    return X, Y

def best4DT(seed=1489683273):
    np.random.seed(seed)
    # X = np.zeros((100,2))
    X = np.random.random(size = (50,3))*200-50
    Y = X[:,0] + np.sin(X[:,1]) + X[:,2]**2


    return X, Y

def author():
    return 'tyan37' #Change this to your user ID

if __name__=="__main__":
    print "they call me Tim."
