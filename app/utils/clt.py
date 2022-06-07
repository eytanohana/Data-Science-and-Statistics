import numpy as np
import streamlit as st


class CltConsts:
    VALUES = 'values'
    DIST = 'dist'
    COUNTS = 'counts'


def update_distribution(i):
    st.session_state[CltConsts.VALUES].append(i)
    values, counts = np.unique(st.session_state[CltConsts.VALUES], return_counts=True)
    probs = counts / counts.sum()
    st.session_state[CltConsts.DIST] = dict(zip(values, probs))

