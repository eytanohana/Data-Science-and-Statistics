import streamlit as st
import sys
import os


st.set_page_config(page_title='Data Science & Statistics', page_icon='📉', layout='centered')
st.header('Welcome!')

sys.path.extend([os.path.dirname(__file__), f'{os.path.dirname(__file__)}/backend'])
