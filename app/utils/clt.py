import numpy as np
import streamlit as st


class CltConsts:
    VALUES = 'values'
    DIST_VALS = 'dist_vals'
    PROB = 'prob'


def update_distribution(i):
    st.session_state[CltConsts.VALUES].append(i)
    values, counts = np.unique(st.session_state[CltConsts.VALUES], return_counts=True)
    probs = counts / counts.sum()
    st.session_state[CltConsts.DIST_VALS] = values
    st.session_state[CltConsts.PROB] = probs


def generate_sample_means(sample_size, sample_means):
    if len(st.session_state[CltConsts.DIST_VALS]) == 0:
        st.error('')
        return
    with st.spinner('Generating sample means'):
        sample_means = np.array([np.random.choice(st.session_state[CltConsts.DIST_VALS],
                                                  p=st.session_state[CltConsts.PROB],
                                                  size=sample_size).mean()
                                 for _ in range(sample_means)])
    return sample_means
