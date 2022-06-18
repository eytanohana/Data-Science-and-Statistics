import numpy as np
import seaborn as sns
import streamlit as st


def covariance(x, y):
    return np.sum((x - x.mean()) * (y - y.mean())) / (len(x) - 1)


def correlation(x, y):
    return covariance(x, y) / (x.std() * y.std())


@st.cache(show_spinner=False, hash_funcs={sns.axisgrid.PairGrid: lambda _: None})
def pairplot(data, hue=None):
    return sns.pairplot(data, hue=hue)
