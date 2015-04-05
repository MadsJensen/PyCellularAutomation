from copy import deepcopy

import matplotlib.pyplot as plt
import numpy as np


plt.ion()


class CA(object):
    """A 1 dimensional celluar automatica

    """

    def __init__(self, orig_conf):
        self.orig_conf = orig_conf

    def update(self, n_update=100, rule=[0, 1, 1, 0, 1, 1, 1, 0]):
        """ Function to update a CA

        Parameters
        ----------
        CA : 1d CA
        n_update : The number of updates that will be ran
        rule : A list with 8 elements.
            The rule used for the update. Rule is a 8 elemenet list.
            It follows the convention:
            111, 110, 101, 100, 011, 010, 001, 000
        """

        self.data = np.empty([n_update, len(self.orig_conf)])
        n_pattern = np.empty([3])
        state = deepcopy(self.orig_conf)
        state_updated = np.empty_like(self.orig_conf)

        for j in range(n_update):
            for i in range(len(state)):
                if i + 1 < len(state):
                    n_pattern[0] = state[i - 1]
                    n_pattern[1] = state[i]
                    n_pattern[2] = state[i + 1]
                else:
                    n_pattern[0] = state[i - 1]
                    n_pattern[1] = state[i]
                    n_pattern[2] = state[0]

                # print n_pattern
                new_state = pattern(n_pattern, rule)
                state_updated[i] = new_state

            self.data[j, :] = state_updated.reshape(-1)
            state = deepcopy(state_updated)

    def plot(self, interpolation="None", cmap="binary"):
        """Plot updated data

        Parameters
        ----------
        interpolation : use interpolation, default: none
        cmap : which color map to use, default: Binary

        """

        if hasattr(self, "data"):
            plt.imshow(self.data, interpolation="None", cmap="binary")
        else:
            raise ValueError('Objects has no data attr., run "update"')


def pattern(n_pattern, rule):
    """ Function to identify neighbour pattern

    Parameters
    ----------
    n_pattern : the set of cells to calculate the new state from.
    rule : the rule that is used to update from

    """

    if n_pattern[0] == 1:
        if n_pattern[1] == 1:
            if n_pattern[2] == 1:
                # print "111"
                new_state = rule[0]
            if n_pattern[2] == 0:
                # print "110"
                new_state = rule[1]
        if n_pattern[1] == 0:
            if n_pattern[2] == 1:
                # print "101"
                new_state = rule[2]
            if n_pattern[2] == 0:
                # print "100"
                new_state = rule[3]
    elif n_pattern[0] == 0:
        if n_pattern[1] == 1:
            if n_pattern[2] == 1:
                # print "011"
                new_state = rule[4]
            if n_pattern[2] == 0:
                # print "010"
                new_state = rule[5]
        if n_pattern[1] == 0:
            if n_pattern[2] == 1:
                # print "001"
                new_state = rule[6]
            if n_pattern[2] == 0:
                # print "000"
                new_state = rule[7]

    return new_state


rules = {"30": [0, 0, 0, 1, 1, 1, 1, 0],
         "90": [0, 1, 0, 1, 1, 0, 1, 0],
         "110": [0, 1, 1, 0, 1, 1, 1, 0],
         "184": [1, 0, 1, 1, 1, 0, 0, 0]}
