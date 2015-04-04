import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

plt.ion()


def pattern(n_pattern, rule):
    """ Function to identify neighbour pattern

    ---
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


def update_CA(CA, n_update=100, rule=[0, 1, 1, 0, 1, 1, 1, 0]):
    """ Function to update a CA

    ---
    CA : 1d CA
    n_update : the number of updates that will be ran
    """

    n_pattern = np.empty([3])
    result = np.empty([n_update, len(CA)])
    state = deepcopy(CA)
    state_updated = np.empty_like(CA)

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

        result[j, :] = state_updated.reshape(-1)
        state = deepcopy(state_updated)

    return result

rules = {"30": [0, 0, 0, 1, 1, 1, 1, 0],
         "90": [0, 1, 0, 1, 1, 0, 1, 0],
         "110": [0, 1, 1, 0, 1, 1, 1, 0]}

foo = np.random.randint(2, size=(200))

result = update_CA(foo, 500,  rule=rules["30"])
plt.imshow(result, interpolation="None", cmap="binary")
