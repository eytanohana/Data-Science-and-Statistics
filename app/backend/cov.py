import numpy as np
import streamlit as st
import seaborn as sns


def covariance(x, y):
    return np.sum((x - x.mean()) * (y - y.mean())) / (len(x) - 1)


def correlation(x, y):
    return covariance(x, y) / (x.std() * y.std())

@st.cache
def pairplot(data):
    return sns.pairplot(data)
