import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

VALUES = 'values'
DIST_VALS = 'dist_vals'
PROBS = 'probs'
SAMPLE_MEANS = 'sample_means'
SAMPLE_SIZE = 'sample_size'
GENERATED_SAMPLE_MEANS = 'generate_sample_means'


def is_init():
    return DIST_VALS in st.session_state


def init():
    st.session_state[VALUES] = []
    st.session_state[DIST_VALS] = np.array([])
    st.session_state[PROBS] = np.array([])
    st.session_state[SAMPLE_MEANS] = np.array([])
    st.session_state[SAMPLE_SIZE] = 0
    st.session_state[GENERATED_SAMPLE_MEANS] = False


def update_distribution(i):
    st.session_state[VALUES].append(i)
    values, counts = np.unique(st.session_state[VALUES], return_counts=True)
    st.session_state[DIST_VALS] = values
    st.session_state[PROBS] = counts / counts.sum()


def clear_distribution():
    init()


def has_distribution():
    return len(np.unique(st.session_state[DIST_VALS])) > 1


def generate_sample_means(sample_size, n_samples):
    if len(st.session_state[VALUES]) == 0:
        st.error('You must create a distribution before generating sample means.')
        return
    st.session_state[SAMPLE_MEANS] = np.array([np.random.choice(st.session_state[DIST_VALS],
                                                                p=st.session_state[PROBS],
                                                                size=sample_size).mean()
                                               for _ in range(n_samples)])
    st.session_state[SAMPLE_SIZE] = sample_size


def get_distribution_mean():
    return np.sum(st.session_state[DIST_VALS] * st.session_state[PROBS])


def get_distribution_std():
    return np.sqrt(
        np.sum(st.session_state[DIST_VALS] ** 2 * st.session_state[PROBS])
        - get_distribution_mean() ** 2
    )


def get_theoretical_sample_means_mean():
    return get_distribution_mean()


def get_theoretical_sample_means_std():
    return get_distribution_std() / np.sqrt(st.session_state[SAMPLE_SIZE])


@st.cache(show_spinner=False)
def plotly_distribution_chart(n_dist_values, mean, std):
    return px.bar(
        x=st.session_state[DIST_VALS],
        y=st.session_state[PROBS],
        range_x=(0, n_dist_values + 1),
        labels={'x': 'k', 'y': 'P(x=k)'},
        title=f'μ = {mean:.3f} σ = {std:.3f}'
    )


def plotly_sample_means_chart():
    fig = ff.create_distplot(
        [st.session_state[SAMPLE_MEANS]],
        group_labels=['Sample Means'],
        bin_size=0.1,
        show_rug=False
    )
    title = f'#### Distribution of {len(st.session_state[SAMPLE_MEANS])} sample ' \
            f'means using sample size {st.session_state[SAMPLE_SIZE]}.'
    return fig, title


def sample_means():
    return st.session_state[SAMPLE_MEANS]
