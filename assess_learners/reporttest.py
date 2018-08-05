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
    inf = open(sys.argv[1])
    # print "inf: ",inf
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

    # print testX.shape
    # print testY.shape

    # create a learner and train it
    #learner = lrl.LinRegLearner(verbose = True) # create a LinRegLearner
    RMSE_in = []
    RMSE_out = []
    for i in range(1, 31):
        single_RMSE_in = []
        single_RMSE_out = []
        for j in range(1, 51):
            # learner = dt.DTLearner(leaf_size = i,verbose = True)  # create a DTLearner
            # learner = rt.RTLearner(leaf_size = i,verbose = True)  # create a DTLearner
            learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": i}, bags=20, boost=False, verbose=True)
            # learner = bl.BagLearner(learner=rt.RTLearner, kwargs={"leaf_size": 1}, bags=20, boost=False, verbose=True)
            learner.addEvidence(trainX, trainY) # train it
            # print learner.author()

            # evaluate in sample
            predY = learner.query(trainX) # get the predictions
            rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])

            # print "In sample results"
            # print "RMSE: ", rmse
            single_RMSE_in.append(rmse)
            c = np.corrcoef(predY, y=trainY)
            # print "corr: ", c[0,1]

            # evaluate out of sample
            predY = learner.query(testX) # get the predictions
            rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
            # print
            # print "Out of sample results"
            # print "RMSE: ", rmse
            single_RMSE_out.append(rmse)
            c = np.corrcoef(predY, y=testY)
            # print "corr: ", c[0,1]
        single_RMSE_in = np.array(single_RMSE_in)
        single_RMSE_out = np.array(single_RMSE_out)
        # print "In sample results with  ", i, " leaf is: " , single_RMSE_in.mean()
        # print "out sample results with  ", i, " leaf is: ", single_RMSE_out.mean()
        RMSE_in.append(single_RMSE_in.mean())
        RMSE_out.append(single_RMSE_out.mean())
    print "RMSE_in result: "
    for k in RMSE_in:
        print k
    print "==================="
    print "RMSE_out result: "
    for l in RMSE_out:
        print l