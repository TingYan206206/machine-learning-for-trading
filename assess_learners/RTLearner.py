import numpy as np
import random


class RTLearner(object):

    def __init__(self,leaf_size, verbose=False):
        self.leaf_size = leaf_size
        # pass  # move along, these aren't the drones you're looking for

    def author(self):
        return 'tyan37'  # replace tb34 with your Georgia Tech username

    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        if dataX.shape[0] == 1:
            self.tree = np.array([[-1, dataY, -1, -1]], dtype= float)
            return self.tree
        if np.isclose(dataY, dataY[0]).all():
            self.tree = np.array([[-1, dataY[0], -1, -1]], dtype= float)
            return self.tree
        if dataX.shape[0] <= self.leaf_size:
            self.tree = np.array([[-1, np.mean(dataY), -1, -1]])
            return self.tree
        else:
            index = random.randint(0, dataX.shape[1]-1)

            while True:

                SplitVal = np.median(dataX[:, index], axis=0)
                if np.isclose(dataX[:, index], dataX[0, index]).all():
                    index = random.randint(0, dataX.shape[1] - 1)
                    continue


                elif SplitVal >= np.nanmax(dataX[:, index]):
                    SplitVal = (dataX[:, index].max() + dataX[:, index].min()) / 2
                    break

                else:
                    break
            lefttree = np.array(
                self.addEvidence(dataX[dataX[:, index] <= SplitVal], dataY[dataX[:, index] <= SplitVal]))
            righttree = np.array(self.addEvidence(dataX[dataX[:, index] > SplitVal], dataY[dataX[:, index] > SplitVal]))

            root = np.array([[index, SplitVal, 1, lefttree.shape[0] + 1]], dtype= float)
            self.tree = np.vstack((root, lefttree))
            self.tree = np.vstack((self.tree, righttree))

            return self.tree

    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        result = []
        # print "result shape: ", result.shape
        tree = np.array(self.tree)

        for i in range(0, points.shape[0]):
            j = 0
            while self.tree[j, 0] != -1:
                ## if value is smaller than splitval, go to left tree
                splitV = tree[j, 1]
                index = int(tree[j, 0])

                if points[i, index] <= splitV:
                    j = j + 1

                else:
                    j = j + int(tree[j, 3])

            result.append(float(tree[j, 1]))


        return result


