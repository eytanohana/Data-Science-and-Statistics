import streamlit as st

st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='wide')


st.markdown('''
# Distributions
A **Distribution** is just a set of values and the probabilities of getting those values.
From that we know that all the probabilities in the distribution should sum up to 100%.
There are two types of distributions.

**Discrete Distributions** are distributions that contain only discrete values like 1, 2, 3, ...

**Continuous Distributions** are distributions that can contain any value like 1.3 or 13.059

## Common Discrete Distributions
''')

st.markdown('''
### The Uniform distribution $X \sim U(a, b)$
> X is a random variable that takes on discrete values between a and b with equal probability.
''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)=\\frac{1}{b-a+1}\;\\textrm{, for } k = a, ..., b$')
b.markdown('$E(X) = \\frac{a+b}{2}$')
c.markdown('$V(X) = \\frac{(b - a + 1)^2 - 1}{12}$')
