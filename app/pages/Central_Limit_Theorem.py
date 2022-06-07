import numpy as np

from app.utils.clt import update_distribution, CltConsts

import streamlit as st
import plotly.express as px

st.set_page_config(page_title='CLT', page_icon='📉', layout='wide')

st.header('The Central Limit Theorem')

st.markdown('''The central theorem limit states that for *almost* any distribution with mean,
               $\mu$, and standard deviation, $\sigma$, if we take the means sufficiently many samples 
               of size n that as we increase the sample size n, the distribution of the sample 
               means will look more and more normal.''')

st.subheader('Create a random distribution')
if CltConsts.DIST not in st.session_state:
    st.session_state[CltConsts.VALUES] = []
    st.session_state[CltConsts.DIST] = {CltConsts.VALUES: np.array([0]), CltConsts.PROB: np.array([0])}

n_dist_values = 20
dist_value_cols = st.columns(n_dist_values)
for i, dist_col in enumerate(dist_value_cols, 1):
    dist_col.button(f'{i}', on_click=update_distribution, args=(i,))

mean = np.sum(st.session_state[CltConsts.DIST][CltConsts.VALUES]
              * st.session_state[CltConsts.DIST][CltConsts.PROB])
std = np.sqrt(np.sum(st.session_state[CltConsts.DIST][CltConsts.VALUES]**2 *
                     st.session_state[CltConsts.DIST][CltConsts.PROB]) - mean**2)

st.plotly_chart(
    px.bar(
        x=st.session_state[CltConsts.DIST][CltConsts.VALUES],
        y=st.session_state[CltConsts.DIST][CltConsts.PROB],
        range_x=(0, n_dist_values + 1),
        labels={'x': 'k', 'y': 'P(x=k)'},
        title=f'Distribution with mean {mean:.3f} and standard deviation {std:.3f}'
    )
)
