import streamlit as st
from warnings import filterwarnings

import os


filterwarnings(action='ignore')
st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='centered')
logger = st.logger.get_logger(__name__)

# Header
st.title('📉 Welcome to Data Science & Statistics!')
st.markdown('---')

# Introduction
st.markdown('''
Welcome to an interactive exploration of fundamental concepts in **Data Science** and **Statistics**!

This app provides hands-on, visual learning experiences to help you understand key statistical 
concepts through interactive demonstrations and real-world examples.
''')

st.markdown('---')

# Available Topics Section
st.header('📚 Available Topics')

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    ### 1️⃣ Common Distributions
    
    Explore probability distributions that form the foundation of statistical analysis:
    - **Discrete Distributions**: Uniform, Binomial, Hypergeometric, Geometric, Negative Binomial, Poisson
    - **Continuous Distributions**: Learn about continuous probability distributions
    
    Visualize how different parameters affect the shape and behavior of each distribution.
    ''')
    
    st.markdown('''
    ### 2️⃣ Central Limit Theorem
    
    Discover one of the most important theorems in statistics! 
    
    The Central Limit Theorem states that the distribution of sample means approaches a normal 
    distribution as the sample size increases, regardless of the original population distribution.
    
    Create your own custom distribution and watch the magic happen!
    ''')

with col2:
    st.markdown('''
    ### 3️⃣ Covariance and Correlation
    
    Understand the relationships between variables:
    - Learn the difference between **covariance** and **correlation**
    - Visualize positive, negative, and no relationships
    - Explore correlation matrices and heatmaps
    - See real-world examples with penguin data
    
    Discover common misconceptions and gain deeper insights into these fundamental concepts.
    ''')

st.markdown('---')

# Features Section
st.header('✨ Features')

feature_cols = st.columns(3)

with feature_cols[0]:
    st.markdown('''
    **🎯 Interactive Learning**
    
    Adjust parameters in real-time and see immediate visual feedback
    ''')
    
with feature_cols[1]:
    st.markdown('''
    **📊 Visual Demonstrations**
    
    Beautiful charts and graphs to help you understand complex concepts
    ''')
    
with feature_cols[2]:
    st.markdown('''
    **🔬 Real-World Examples**
    
    Explore actual datasets to see statistics in action
    ''')

st.markdown('---')

# Getting Started
st.header('🚀 Getting Started')

st.markdown('''
Navigate to any topic using the sidebar on the left. Each page contains:
- **Clear explanations** of statistical concepts
- **Mathematical formulas** with LaTeX notation
- **Interactive widgets** to experiment with parameters
- **Visualizations** that update in real-time

Feel free to explore and experiment! The best way to learn statistics is by doing.
''')

st.markdown('---')

# Footer
st.markdown('''
<div style="text-align: center; color: gray;">
    <p>Happy learning! 📚</p>
</div>
''', unsafe_allow_html=True)

logger.info(f"Current App Version: {os.environ.get('DOCKER_TAG')}")
