import streamlit as st

from backend import dist

st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='wide')

st.markdown('''
# Distributions
A **Distribution** is just a set of values and the probabilities of getting those values.
From that we know that all the probabilities in the distribution should sum up to 100%.
There are two types of distributions.

**Discrete Distributions** are distributions that contain only discrete values like 1, 2, 3, ...

**Continuous Distributions** are distributions that can contain any value like 1.3 or 13.059

## Common Discrete Distributions
---
''')

st.markdown('''
### The Uniform Distribution $X \sim U(a, b)$
> X is a random variable that takes on discrete values between a and b with equal probability.
''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)=\\frac{1}{b-a+1}\;\\textrm{, for } k = a, ..., b$')
b.markdown('$E(X) = \\frac{a+b}{2}$')
c.markdown('$V(X) = \\frac{(b - a + 1)^2 - 1}{12}$')
a, b = st.columns(2)
start = a.slider('a', min_value=1, max_value=5, value=1)
end = b.slider('b', min_value=6, max_value=10, value=6)
st.pyplot(dist.Uniform.plot_dist(start, end))

st.markdown('''
---
###  The Binomial Distribution $X \sim B(n, p)$
> X is a random variable that counts the number of successes out of $n$
>independent events with the same probability $p$ for success.
''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)={n \choose k} p^k (1-p)^{n-k}\;\\textrm{, for } k = 0, 1,  ..., n$')
b.markdown('$E(X) = np$')
c.markdown('$V(X) = np(1-p)$')
a, b = st.columns(2)
n = a.slider('n', min_value=0, max_value=30, value=15)
p = b.slider('p', min_value=0.0, max_value=1.0, value=0.5)
st.pyplot(dist.Binomial.plot_dist(n, p))

st.markdown('''
---
###  The Hypergeometric Distribution $X \sim HG(M, n, N)$
> X is a random variable that counts the number of "special" items taken from
>choosing $N$ times out of a total population size of $M$ without replacement.
''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)=\large{\\frac{{n \choose k}{M-n \choose N-k}}{M \choose N}}'
           '\\textrm{ for } k =\\textrm{max}(0,N-(M-n)),...,\\textrm{min}(N, n)$')
b.markdown('$E(X) = N\\frac{n}{M}$')
c.markdown('$V(X) = \\frac{M-N}{M-1}N\\frac{n}{M}(1 - \\frac{n}{M})$')
a, b, c = st.columns(3)
M = a.slider('M', min_value=50, max_value=100, value=50)
n = b.slider('n', min_value=0, max_value=50, value=30)
N = c.slider('N', min_value=0, max_value=50, value=30)
st.pyplot(dist.Hypergeometric.plot_dist(M, n, N))

st.markdown('''
---
###  The Geometric Distribution $X \sim G(p)$
> X is a random variable that counts the number of attempts up til and including the first
>"success" in an independent series of attempts with the same chance for success, $p$.
''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)=(1-p)^{k-1}p'
           '\\textrm{ for } k = 1,2,3,...$')
b.markdown('$E(X) = \\frac{1}{p}$')
c.markdown('$V(X) = \\frac{1-p}{p^2}$')
p = st.slider('p', min_value=0.0, max_value=1.0, value=0.5, step=0.05)
st.pyplot(dist.Geometric.plot_dist(p))

st.markdown('''
---
###  The Negative Binomial Distribution $X \sim NB(n, p)$
> $X$ is a random variable that counts the number of attempts up until and
> including the $n^{th}$ success, in an independent series of attempts with the same chance for success, $p$.

''')
a, b, c = st.columns(3)
a.markdown('$P(X=k)={k-1 \choose n-1} p^n (1-p)^{k-n} \;\\textrm{ for } k = n, n+1, n+2, ...$')
b.markdown('$E(X) = \\frac{n}{p}$')
c.markdown('$V(X) = n\\frac{1-p}{p^2}$')
a, b = st.columns(2)
n = a.slider('n', min_value=1, max_value=50)
p = b.slider('p', min_value=0.0, max_value=1.0, value=0.5, step=0.05, key='nbp')
st.pyplot(dist.NegativeBinomial.plot_dist(n, p))
