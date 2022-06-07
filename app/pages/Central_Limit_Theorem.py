import streamlit as st

st.set_page_config(page_title='CLT', page_icon='📉', layout='wide')

st.header('The Central Limit Theorem')

st.markdown('''The central theorem limit states that for *almost* any distribution with mean,
               $\mu$, and standard deviation, $\sigma$, if we take the means sufficiently many samples 
               of size n that as we increase the sample size n, the distribution of the sample 
               means will look more and more normal.''')

st.subheader('Create a random distribution')
n_dist_values = 20
if 'distribution' not in st.session_state:
    st.session_state.distribution_values = []
    st.session_state.distribution = {}

dist_value_cols = st.columns(n_dist_values)
for i, dist_col in enumerate(dist_value_cols, 1):
    dist_col.button(f'{i}', on_click=update_distribution, args=(i,))
