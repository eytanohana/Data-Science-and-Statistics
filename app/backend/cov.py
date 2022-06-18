import numpy as np


def covariance(x, y):
    return np.sum((x - x.mean()) * (y - y.mean())) / (len(x) - 1)


def correlation(x, y):
    return covariance(x, y) / (x.std() * y.std())
