import numpy as np
import streamlit as st


class CltConsts:
    VALUES = 'values'
    DIST_VALS = 'dist_vals'
    PROB = 'prob'
    SAMPLE_MEANS = 'sample_means'


def update_distribution(i):
    st.session_state[CltConsts.VALUES].append(i)
    values, counts = np.unique(st.session_state[CltConsts.VALUES], return_counts=True)
    probs = counts / counts.sum()
    st.session_state[CltConsts.DIST_VALS] = values
    st.session_state[CltConsts.PROB] = probs


def generate_sample_means(sample_size, n_samples):
    if len(st.session_state[CltConsts.DIST_VALS]) == 0:
        st.error('You must create a distribution before generating sample means.')
        return
    with st.spinner('Generating sample means'):
        sample_means = np.array([np.random.choice(st.session_state[CltConsts.DIST_VALS],
                                               p=st.session_state[CltConsts.PROB],
                                               size=sample_size).mean()
                              for _ in range(n_samples)])
    st.session_state[CltConsts.SAMPLE_MEANS] = sample_means
