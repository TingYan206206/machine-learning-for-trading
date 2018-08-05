"""
Test a learner.  (c) 2015 Tucker Balch
"""

import numpy as np
import math
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import sys

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "Usage: python testlearner.py <filename>"
        sys.exit(1)
    print type(sys.argv[1])
    inf = open(sys.argv[1])
    print "inf: ",inf
    print type(inf)
    # if inf == 'Istanbul.csv':
    #     inf = inf[1:, 1:]
    data = np.array([map(float,s.strip().split(',')[1:]) for s in inf.readlines()[1:]])
    # data = np.array([map(float, s.strip().split(',')) for s in inf.readlines()])

    # compute how much of the data is training and testing
    train_rows = int(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data[:train_rows,0:-1]
    trainY = data[:train_rows,-1]
    testX = data[train_rows:,0:-1]
    testY = data[train_rows:,-1]

    print testX.shape
    print testY.shape

    # create a learner and train it
    #learner = lrl.LinRegLearner(verbose = True) # create a LinRegLearner
    # learner = dt.DTLearner(leaf_size = 1,verbose = True)  # create a DTLearner
    learner = rt.RTLearner(leaf_size = 30,verbose = True)  # create a DTLearner
    # learner = bl.BagLearner(learner=lrl.LinRegLearner, kwargs={}, bags=10, boost=False, verbose=True)
    # learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": 30}, bags=20, boost=False, verbose=True)
    # learner = bl.BagLearner(learner=rt.RTLearner, kwargs={"leaf_size": 1}, bags=20, boost=False, verbose=True)
    learner.addEvidence(trainX, trainY) # train it
    print learner.author()

    # evaluate in sample
    predY = learner.query(trainX) # get the predictions
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
    # print predY
    # print predY.shape
    print "In sample results"
    print "RMSE: ", rmse
    c = np.corrcoef(predY, y=trainY)
    print "corr: ", c[0,1]

    # evaluate out of sample
    predY = learner.query(testX) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    print
    print "Out of sample results"
    print "RMSE: ", rmse
    c = np.corrcoef(predY, y=testY)
    print "corr: ", c[0,1]
