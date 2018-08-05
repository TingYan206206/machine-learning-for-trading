"""
Template for implementing QLearner  (c) 2015 Tucker Balch
"""

import numpy as np
import random as rand

# name: Ting Yan
# id: tyan37

class QLearner(object):

    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):

        self.verbose = verbose
        self.num_actions = num_actions
        self.s = 0
        self.a = 0
        self.rar = rar
        self.radr = radr
        self.alpha = alpha
        self.gamma = gamma
        self.Q =np.zeros((num_states,num_actions),dtype= float)
        self.dyna =dyna
        self.data = []


    def querysetstate(self, s):
        """
        @summary: Update the state without updating the Q-table
        @param s: The new state
        @returns: The selected action
        """
        self.s = s
        self.a = np.argmax(self.Q[s])
        return self.a

    def query(self,s_prime,r):
        """
        @summary: Update the Q table and return an action
        @param s_prime: The new state
        @param r: The ne state
        @returns: The selected action
        """

        self.Q[self.s, self.a] = (1 - self.alpha) * self.Q[self.s, self.a] + self.alpha * (
                    r + self.gamma * self.Q[s_prime, np.argmax(self.Q[s_prime])])
        self.data.append((self.s, self.a, s_prime, r))

        """dyna implementation"""
        train_data = np.random.randint(len(self.data), size=self.dyna)
        for i in range(0, self.dyna):
            pre_s, pre_a, new_s, reward = self.data[train_data[i]]
            self.Q[pre_s, pre_a] = (1 - self.alpha) * self.Q[pre_s, pre_a] + self.alpha * (reward + self.gamma * self.Q[new_s, np.argmax(self.Q[new_s])])

        # choose a random step:
        if rand.uniform(0.0, 1.0) <= self.rar:
            action = rand.randint(0,self.num_actions-1)  #chosose the random direction
        else:
            action = np.argmax(self.Q[s_prime])

        self.rar = self.rar * self.radr
        self.s = s_prime
        self.a = action
        return action

    def author(self):
        return 'tyan37'
if __name__=="__main__":
    print "Remember Q from Star Trek? Well, this isn't him"
