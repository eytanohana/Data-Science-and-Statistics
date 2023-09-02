import streamlit as st
from warnings import filterwarnings

import os


filterwarnings(action='ignore')
st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='centered')
st.header('Welcome!')

print(f"Current Version: {os.environ.get('DOCKER_TAG')}")
