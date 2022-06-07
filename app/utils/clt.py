import numpy as np
import streamlit as st


class CltConsts:
    DIST_VALUES = 'dist_values'
    DIST = 'dist'


def update_distribution(i):
    st.session_state[CltConsts.DIST_VALUES].append(i)
    values, counts = np.unique(st.session_state[CltConsts.DIST_VALUES], return_counts=True)
    probs = counts / counts.sum()
    st.session_state[CltConsts.DIST] = dict(zip(values, probs))

