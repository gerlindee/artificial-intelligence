from math import exp


def identical(x):
    return x


def derr_Identical():
    return 1


def ReLU(x):
    return max(0, x)


def derr_ReLU(x):
    if x > 0:
        return 1
    return 0


def threshold(x):
    if x > 0.2:
        return 1
    return 0


def derr_threshold():
    return 1


def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))


def derr_sigmoid(x):
    return x * (1.0 - x)