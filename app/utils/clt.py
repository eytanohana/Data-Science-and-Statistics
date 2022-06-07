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
    st.session_state[CltConsts.DIST][CltConsts.VALUES] = values
    st.session_state[CltConsts.DIST][CltConsts.PROB] = probs

