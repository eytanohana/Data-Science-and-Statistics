import pandas as pd

from app.backend import clt

import streamlit as st

st.set_page_config(page_title='CLT', page_icon='📉', layout='wide')

st.header('The Central Limit Theorem')

st.markdown('>**The central theorem limit states that for *almost* any distribution with mean, '
            '$\mu$, and standard deviation, $\sigma$, if we take the means sufficiently many samples '
            'of size n that as we increase the sample size n, the distribution of the sample '
            'means will look more and more normal.**')

n_dist_values = 20
st.subheader(f'Create a random distribution from {n_dist_values} distinct possible values')
if not clt.is_init():
    clt.init()

dist_value_cols = st.columns(n_dist_values)
for i, dist_col in enumerate(dist_value_cols, 1):
    dist_col.button(f'{i}', on_click=clt.update_distribution, args=(i,))

mean = clt.get_distribution_mean()
std = clt.get_distribution_std()

st.plotly_chart(
    clt.plotly_distribution_chart(n_dist_values, mean, std)
)
st.button('Clear', on_click=clt.clear_distribution)

st.markdown('---')
a, b = st.columns(2)
sample_size = a.number_input('Sample size', value=10)
n_samples = b.number_input('Number of samples', value=500)

if clt.has_distribution():
    with st.spinner(f'Generating {n_samples} sample means'):
        clt.generate_sample_means(sample_size, n_samples)
    fig, title = clt.plotly_sample_means_chart()
    st.markdown(title)
    st.plotly_chart(fig)

    theoretical_mean, theoretical_std = clt.get_theoretical_sample_means_mean(), clt.get_theoretical_sample_means_std()
    actual_mean, actual_std = clt.sample_means().mean(), clt.sample_means().std()
    st.dataframe(pd.DataFrame({'Theoretical': [theoretical_mean, theoretical_std],
                               'Actual': [actual_mean, actual_std],
                               'Gap': [abs(theoretical_mean - actual_mean), abs(theoretical_std - actual_std)]},
                              index=['Mean', 'Standard Deviation']))
