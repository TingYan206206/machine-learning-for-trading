import numpy as np
import LinRegLearner as lrl
import BagLearner as bl


class InsaneLearner(object):

    def __init__(self, verbose=False):

        self.learners = []

        for i in range(0, 20):

            self.learners.append(bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {}, bags = 20, boost = False, verbose = False))


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


        for l in self.learners:
            l.addEvidence(dataX, dataY)


    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        result = np.zeros((points.shape[0],), dtype=float)
        for l in self.learners:
            y = l.query(points)
            result = np.column_stack((result, y))
        result = result[:, 1:]
        return np.mean(result, axis=1)