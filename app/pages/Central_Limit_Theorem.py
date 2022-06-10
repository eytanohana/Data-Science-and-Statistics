import numpy as np

from app.utils import clt

import streamlit as st
import plotly.express as px

st.set_page_config(page_title='CLT', page_icon='📉', layout='wide')

st.header('The Central Limit Theorem')

st.markdown('''The central theorem limit states that for *almost* any distribution with mean,
               $\mu$, and standard deviation, $\sigma$, if we take the means sufficiently many samples 
               of size n that as we increase the sample size n, the distribution of the sample 
               means will look more and more normal.''')

n_dist_values = 20
st.subheader(f'Create a random distribution with {n_dist_values} distinct possible values')
if clt.DIST_VALS not in st.session_state:
    st.session_state[clt.VALUES] = []
    st.session_state[clt.DIST_VALS] = np.array([])
    st.session_state[clt.PROBS] = np.array([])

dist_value_cols = st.columns(n_dist_values)
for i, dist_col in enumerate(dist_value_cols, 1):
    dist_col.button(f'{i}', on_click=clt.update_distribution, args=(i,))

mean = clt.get_distribution_mean()
std = clt.get_distribution_std()

st.plotly_chart(
    px.bar(
        x=st.session_state[clt.DIST_VALS],
        y=st.session_state[clt.PROBS],
        range_x=(0, n_dist_values + 1),
        labels={'x': 'k', 'y': 'P(x=k)'},
        title=f'μ = {mean:.3f} σ = {std:.3f}'
    )
)

st.markdown('---')

sample_size = st.number_input('Sample size', 1, 100, value=5)
sample_means = st.number_input('Number of samples', 100, 10_000, value=500)

st.button('Generate sample means', on_click=clt.generate_sample_means, args=(sample_size, sample_means))
