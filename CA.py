import numpy as np
import matplotlib.pyplot as plt

plt.ion()


def pattern(n_pattern):
    """ Function to identify neighbour pattern

    """
    if n_pattern[0] == 1:
        if n_pattern[1] == 1:
            if n_pattern[2] == 1:
                # print "111"
                new_state = 0
            if n_pattern[2] == 0:
                # print "110"
                new_state = 1
        if n_pattern[1] == 0:
            if n_pattern[2] == 1:
                # print "101"
                new_state = 1
            if n_pattern[2] == 0:
                # print "100"
                new_state = 0
    elif n_pattern[0] == 0:
        if n_pattern[1] == 1:
            if n_pattern[2] == 1:
                # print "011"
                new_state = 1
            if n_pattern[2] == 0:
                # print "010"
                new_state = 1
        if n_pattern[1] == 0:
            if n_pattern[2] == 1:
                # print "001"
                new_state = 1
            if n_pattern[2] == 0:
                # print "000"
                new_state = 0

    return new_state


foo = np.random.randint(2, size=(100))
bar = foo.copy()

result = np.empty([100, 100])
n_pattern = np.empty([3])

for j in range(100):
    tmp = foo.copy()
    for i in range(len(tmp)):

        if i + 1 < len(tmp):
            n_pattern[0] = tmp[i - 1]
            n_pattern[1] = tmp[i]
            n_pattern[2] = tmp[i + 1]
        elif i + 1 == len(tmp):
            n_pattern[0] = tmp[i - 1]
            n_pattern[1] = tmp[i]
            n_pattern[2] = tmp[0]

        print n_pattern
        new_state = pattern(n_pattern)
        bar[i] = new_state

    result[j, :] = bar.reshape(-1)
    tmp = bar.copy()


plt.imshow(result, interpolation="None")
