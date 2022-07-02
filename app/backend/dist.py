import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom, hypergeom, geom

PROPS = dict(boxstyle='round', facecolor='wheat', alpha=0.5)


class Uniform:

    @classmethod
    def plot_dist(cls, a, b):
        k = np.arange(a, b+1)
        pmf = np.ones_like(k) / (b - a + 1)
        fig = plt.figure(figsize=(5, 2))
        plt.xticks(np.arange(a, b+1), fontsize=5)
        plt.yticks(fontsize=5)
        sns.barplot(k, pmf, color='cadetblue')
        text = f'E(X) = {cls.expectation(a, b):.2f}\nV(X) = {((b-a+1)**2-1)/12:.2f}'
        plt.text(0.01, 0.95, text, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', bbox=PROPS)
        plt.grid(ls='dashed')
        plt.title(f'Uniform distribution from {a} to {b}', fontsize=6)
        plt.ylim(0, 1)
        return fig

    @staticmethod
    def expectation(a, b):
        return (a + b) / 2

    @staticmethod
    def variance(a, b):
        return ((b - a + 1) ** 2 - 1) / 12


class Binomial:

    @classmethod
    def plot_dist(cls, n, p):
        k = np.arange(0, n+1)
        pmf = binom(n, p).pmf(k)
        fig = plt.figure(figsize=(5, 2))
        sns.barplot(k, pmf, color='cadetblue')
        text = f'E(X) = {cls.expectation(n, p):.2f}\nV(X) = {cls.variance(n, p)}'
        plt.xticks(fontsize=5)
        plt.yticks(fontsize=5)
        plt.text(0.01, 0.95, text, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', bbox=PROPS)
        plt.grid(ls='dashed')
        plt.title(f'Binomial distribution with {n=} and {p=}', fontsize=6)
        plt.ylim(0, 1)
        return fig

    @staticmethod
    def expectation(n, p):
        return n * p

    @staticmethod
    def variance(n, p):
        return n * p * (1 - p)


class Hypergeometric:

    @classmethod
    def plot_dist(cls, M, n, N):
        k = np.arange(max(0, N - M + n), min(n, N) + 1)
        pmf = hypergeom(M, n, N).pmf(k)
        fig = plt.figure(figsize=(5, 2))
        sns.barplot(k, pmf, color='cadetblue')
        text = f'E(X) = {cls.expectation(M, n, N):.2f}\nV(X) = {cls.variance(M, n, N)}'
        plt.xticks(fontsize=5)
        plt.yticks(fontsize=5)
        plt.text(0.01, 0.95, text, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', bbox=PROPS)
        plt.grid(ls='dashed')
        plt.title(f'Hypergeometric distribution with {M=} elements and {n=} specials choosing {N=} times', fontsize=6)
        plt.ylim(0, 1)
        return fig

    @staticmethod
    def expectation(M, n, N):
        return N * n / M

    @staticmethod
    def variance(M, n, N):
        return (M - N) / (M - 1) * N * n / M * (1 - n / M)


class Geometric:

    @classmethod
    def plot_dist(cls, p):
        k = np.arange(1, 30)
        pmf = geom(p).pmf(k)
        fig = plt.figure(figsize=(5, 2))
        sns.barplot(k, pmf, color='cadetblue')
        text = f'E(X) = {cls.expectation(p):.2f}\nV(X) = {cls.variance(p)}'
        plt.xticks(fontsize=5)
        plt.yticks(fontsize=5)
        plt.text(0.01, 0.95, text, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', bbox=PROPS)
        plt.grid(ls='dashed')
        plt.title(f'Geometric distribution with probability {p=} for success', fontsize=6)
        plt.ylim(0, 1)
        return fig

    @staticmethod
    def expectation(p):
        return 1 / p

    @staticmethod
    def variance(p):
        return (1 - p) / p**2
