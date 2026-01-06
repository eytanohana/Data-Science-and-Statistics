from os import path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from backend import cov

IMAGES_PATH = path.join(path.dirname(path.dirname(__file__)), 'images')
DATA_POINTS = 200

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

sns.set_theme()
a, b, c = st.columns(3)
with a:
    x = np.random.normal(loc=5, scale=2, size=DATA_POINTS)
    y = 5 * x + np.random.normal(loc=0, scale=10, size=DATA_POINTS)
    fig = plt.figure()
    plt.title('Positive relationship', fontdict={'size': 20})
    sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'**COV = {cov.covariance(x, y):.3f}, CORR = {cov.correlation(x, y):.3f}**')
with b:
    x = np.random.normal(loc=5, scale=2, size=DATA_POINTS)
    y = np.random.normal(loc=0, scale=7, size=DATA_POINTS)
    fig = plt.figure()
    plt.title('No relationship', fontdict={'size': 20})
    sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'k'})
    st.pyplot(fig)
    st.markdown(f'**COV = {cov.covariance(x, y):.3f}, CORR = {cov.correlation(x, y):.3f}**')
with c:
    x = np.random.normal(loc=5, scale=2, size=DATA_POINTS)
    y = -5 * x + np.random.normal(loc=0, scale=10, size=DATA_POINTS)
    fig = plt.figure()
    plt.title('Negative relationship', fontdict={'size': 20})
    sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'k'})
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
x = np.linspace(0, 10, DATA_POINTS)
y = 10 * x + np.random.normal(0, 20, DATA_POINTS)
xx = np.linspace(0, 10, DATA_POINTS)
yy = 5 * x + np.random.normal(0, 4, DATA_POINTS)
fig = plt.figure(figsize=(10, 5))
plt.xlim(0, 10)
plt.ylim(0, 100)
sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'red', 'label': 'Stronger Slope'})
sns.regplot(x=xx, y=yy, ci=None, line_kws={'color': 'blue', 'label': 'Stronger Correlation'})
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


@st.fragment()
def cov_corr_graphs():
    a, b = st.columns(2)
    slope = a.slider('Trend', min_value=-10, max_value=10, value=-10, help='The general slope of the data.')
    scale = b.slider('Scale', min_value=0, max_value=50, value=20, help='How scattered the data should be.')
    x = np.linspace(0, 10, DATA_POINTS)
    y = slope * x + np.random.normal(0, scale, DATA_POINTS)
    fig = plt.figure(figsize=(10, 5))
    plt.title(f'Cov = {cov.covariance(x, y)} | Corr = {cov.correlation(x, y)}')
    plt.xlim(0, 10)
    plt.ylim(-100, 100)
    sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'black'})
    st.pyplot(fig)


cov_corr_graphs()

############################################################################################################

st.markdown('''
---
### A real world example
''')
a, b = st.columns(2)
a.image(path.join(IMAGES_PATH, 'penguin-bill.png'), width=500)
b.markdown('''
Here we have a common dataset that contains multiple measurements between 3 different species of penguins
in Antarctica. The dataset measures bill length, bill depth, flipper length, and body mass in both
Male and Female penguins. We'll use a couple techniques to visualize the data and see which features are
correlated, if any at all.
''')
penguins = sns.load_dataset('penguins').dropna().reset_index(drop=True)
a, b = st.columns(2)
a.dataframe(penguins)
a.markdown('''
The plot to the right (known as a pairplot) helps to visualize the relationship between every pair of numeric variable in the dataset.
From looking at the plot we can tell there's a positive correlation between body mass and flipper length.
''')
b.image(path.join(IMAGES_PATH, 'penguins-pairplot.png'))

st.markdown('''

This dataset is relatively small so we can generate a nice pairplot to visualize the relationship
between each variable, but when we have a larger dataset creating a graph like above can be resource
expensive and time consuming. Even for this dataset, constantly regenerating this same pairplot 
slows down the app too much, which is why I ended up saving the plot as an image ;)

For larger datasets we can create a **Correlation Matrix** to display a heatmap **showing the relationship
between all the variables** in a much less expensive way.
''')

penguin_corr = penguins.corr(numeric_only=True)
a, b = st.columns(2)
with a:
    st.title('The correlation matrix')
    st.dataframe(penguin_corr)
    st.markdown('''
    **remember! The correlation matrix describes the correlation between every pair of variables in the dataset.**''')
with b:
    fig = plt.figure()
    sns.heatmap(penguin_corr, vmin=-1, vmax=1, cmap='ocean', annot=True, linewidths=1, linecolor='k')
    st.pyplot(fig)

st.markdown('''From the heatmap it looks like bill depth and flipper length or bill depth and body mass
are negatively correlated; but if you look at the pairplot above again, what we really see is 3
distinct species of penguins where bill depth and flipper length/body mass are actually
positively correlated. We can see this if we view their individual heatmaps''')


@st.fragment()
def species_heatmap():
    species = penguins.species.unique()
    a, b = st.columns(2)
    with a:
        spec = st.selectbox('Species', options=species)
        spec_df = penguins[penguins.species == spec]
        fig = plt.figure()
        sns.heatmap(spec_df.corr(numeric_only=True), vmin=-1, vmax=1, cmap='ocean', annot=True, linewidths=1, linecolor='k')
        st.pyplot(fig)
    with b:
        st.image(path.join(IMAGES_PATH, f'{spec}-pairplot.png'))


species_heatmap()

st.markdown('''
Even though the first heatmap showed some features had a seemingly negative correlation, only
by massaging the data and trying to visualize it as many ways as possible can we start to get
the whole picture of what's really going on.''')
st.image(path.join(IMAGES_PATH, 'penguins-pairplot-species.png'), width='content')
