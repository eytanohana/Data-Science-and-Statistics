from os.path import dirname, join
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

############################################################################################################

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

############################################################################################################

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

############################################################################################################

st.markdown('''
## Misconceptions about Correlation
---
Many people think Correlation measures how strong the relationship is between the two variables
(ie how large the slope is between the two variables). In reality, like mentioned above, Correlation
measures the linearity between the variables. Meaning how well the two variables form a line with
non-zero slope.

For example, in the graph below, the red line has a steeper slope but the blue line
actually has a higher Correlation because the data fits closer around it.
''')
x = np.linspace(0, 10, 500)
y = 10 * x + np.random.normal(0, 20, 500)
xx = np.linspace(0, 10, 500)
yy = 5 * x + np.random.normal(0, 1, 500)
fig = plt.figure(figsize=(10, 5))
plt.xlim(0, 10)
plt.ylim(0, 100)
sns.regplot(x, y, ci=None, line_kws={'color': 'red', 'label': 'Stronger Slope'})
sns.regplot(xx, yy, ci=None, line_kws={'color': 'blue', 'label': 'Stronger Correlation'})
plt.legend()
st.pyplot(fig)

a, b = st.columns(2)
a.markdown(f'#### <span style="color: red">Correlation(X,Y) = {cov.correlation(x, y):.4f}</span>',
           unsafe_allow_html=True)
b.markdown(f'#### <span style="color: blue">Correlation(X,Y) = {cov.correlation(xx, yy):.4f}</span>',
           unsafe_allow_html=True)

############################################################################################################

st.markdown('''
---
### Playing around

Now we'll generate some new random data. Pay attention to the covariance and correlation
as you choose the trend and scale of the randomly generated data.
''')
a, b = st.columns(2)
slope = a.slider('Trend', min_value=-10, max_value=10, help='The general slope of the data.')
scale = b.slider('Scale', min_value=0, max_value=50, help='How scattered the data should be.')
x = np.linspace(0, 10, 500)
y = slope * x + np.random.normal(0, scale, 500)
fig = plt.figure(figsize=(10, 5))
plt.title(f'Cov = {cov.covariance(x, y)} | Corr = {cov.correlation(x, y)}')
plt.xlim(0, 10)
plt.ylim(-100, 100)
sns.regplot(x, y, ci=None, line_kws={'color': 'black'})
plt.legend()
st.pyplot(fig)

############################################################################################################

st.markdown('''
---
### A real world example

Here we have a common dataset that tracks multiple measurements between different species of penguins.
''')
penguins = sns.load_dataset('penguins').dropna().reset_index(drop=True)
a, b = st.columns(2)
a.dataframe(penguins)
b.image(join(dirname(dirname(__file__)), 'images/penguins-pairplot.png'))

st.markdown('''
The plot above shows the relationship between every two numeric variable in the dataset.
''')
