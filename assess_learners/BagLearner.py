import numpy as np
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rt


class BagLearner(object):

    def __init__(self, learner, kwargs, bags, boost, verbose=False):
        self.learner = learner
        self.bags = bags
        self.kwargs = kwargs



        self.learners = []
        for i in range(0, bags):
            if kwargs == {}:
                self.learners.append(learner(verbose))
            elif "leaf_size" in kwargs:

                self.learners.append(learner(leaf_size = kwargs['leaf_size']))
            else:
                self.learners.append(learner())


        # move along, these aren't the drones you're looking for

    def author(self):
        return 'tyan37'  # replace tb34 with your Georgia Tech username

    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        ## generate random data,randomly selected n items
        n = int(dataX.shape[0])

        # print "rowNum", rowNum
        self.models =[]
        for l in self.learners:
            rowNum = np.random.choice(dataX.shape[0], size=n, replace=True)

            l.addEvidence(dataX[rowNum], dataY[rowNum])
            self.models.append(l)


    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        result = np.zeros((points.shape[0],1), dtype=float)
        for l in self.models:
            y = l.query(points)

            result = np.column_stack((result, y))

        result = result[: , 1: ]

        return np.mean(result, axis=1)

