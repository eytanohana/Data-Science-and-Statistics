import streamlit as st
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='wide')

st.header('Covariance and Correlation')


st.markdown('''Covariance and Correlation describe the relationship between two variables.

>If two variables move in the same direction, we say they have a positive relationship.
>ie when one variable increases and the other does too, vice versa.
>
>If they move in opposite directions, then we say they have a negative relationship.
>ie when one variable increases and the other decreases, vice versa.
>
>And if they dont move together at all then we say they have no relationship.
>ie when one variable increases and the other one either increases or decreases.
''')

sns.set()
a, b, c = st.columns(3)
with a:
    x = np.random.normal(loc=5, scale=2, size=500)
    y = 5 * x + np.random.normal(loc=0, scale=10, size=500)
    fig = plt.figure()
    plt.title('Positive relationship', fontdict={'size': 20})
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
with b:
    x = np.random.normal(loc=5, scale=2, size=500)
    y = np.random.normal(loc=0, scale=7, size=500)
    fig = plt.figure()
    plt.title('No relationship', fontdict={'size': 20})
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
with c:
    x = np.random.normal(loc=5, scale=2, size=500)
    y = -5 * x + np.random.normal(loc=0, scale=10, size=500)
    fig = plt.figure()
    plt.title('Negative relationship', fontdict={'size': 20})
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)

st.markdown('---')
a, b = st.columns(2)
a.markdown('''
**The covariance between two variables is defined by:**

$$Cov(X,Y) = \\frac{1}{n-1}\\sum_{i=1}^{n}(x_i-\\bar{x})(y_i-\\bar{y})$$
''')
b.markdown('''
**The correlation between two variables is defined by:**

$$Corr(X,Y) = \\frac{Cov(X,Y)}{\\sigma_X \\sigma_Y}$$
''')
