import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

from backend import cov

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
    st.markdown(f'**COV = {cov.covariance(x, y):.3f}, CORR = {cov.correlation(x, y):.3f}**')
with b:
    x = np.random.normal(loc=5, scale=2, size=500)
    y = np.random.normal(loc=0, scale=7, size=500)
    fig = plt.figure()
    plt.title('No relationship', fontdict={'size': 20})
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'**COV = {cov.covariance(x, y):.3f}, CORR = {cov.correlation(x, y):.3f}**')
with c:
    x = np.random.normal(loc=5, scale=2, size=500)
    y = -5 * x + np.random.normal(loc=0, scale=10, size=500)
    fig = plt.figure()
    plt.title('Negative relationship', fontdict={'size': 20})
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'**COV = {cov.covariance(x, y):.3f}, CORR = {cov.correlation(x, y):.3f}**')

st.markdown("""
---
## So What's the difference between Covariance and Correlation?""")

a, b = st.columns(2)
a.markdown('''
**The covariance between two variables is defined by:**

$$Cov(X,Y) = \\frac{1}{n-1}\\sum_{i=1}^{n}(x_i-\\bar{x})(y_i-\\bar{y})$$

**Covariance** only measures the direction of the relationship between the variables.
Whether they have a positive, negative, or no relationship. The strength of the
number itself does not give us any useful information. We only care about its sign.
''')
b.markdown('''
**The correlation between two variables is defined by:**

$$Corr(X,Y) = \\frac{Cov(X,Y)}{\\sigma_X \\sigma_Y}$$

**Correlation** measures the linearity of the relationship between the variables.
Correlation always falls between -1 and 1. A Correlation of -1 means the variables
form a perfect line with a negative slope, while +1 means the variables form a perfect line
with a positive slope. A Correlation of 0 means the two variables are unrelated and either form
a line with no slope or do not form a line at all but the line of best fit through the data has 0 slope.
Like in the middle graph above.
''')

st.markdown('''
## Misconceptions about Correlation
---
Many people think Correlation measures how strong the relationship is between the two variables
(ie how large the slope is between the two variables). In reality, like mentioned above, Correlation
measures the linearity between the variables. Meaning how well the two variables form a line with
non-zero slope.

For example, in the two graphs below, while the graph on the left has a steeper slope, the graph
on the right actually has a higher Correlation because the data fits closer around the regression line.
''')
a, b = st.columns(2)
with a:
    x = np.linspace(0, 10, 500)
    y = 10 * x + np.random.normal(0, 20, 500)
    fig = plt.figure()
    plt.title('Stronger Slope', fontdict={'size': 20})
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'#### Cov(X,Y) = {cov.covariance(x, y):.4f} | Corr(X,Y) = {cov.correlation(x, y):.4f}')
with b:
    x = np.linspace(0, 10, 500)
    y = 5 * x + np.random.normal(0, 1, 500)
    fig = plt.figure()
    plt.title('Higher cov/corr', fontdict={'size': 20})
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    sns.regplot(x, y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'#### Cov(X,Y) = {cov.covariance(x, y):.4f} | Corr(X,Y) = {cov.correlation(x, y):.4f}')
