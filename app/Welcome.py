import streamlit as st
from warnings import filterwarnings

import os


filterwarnings(action='ignore')
st.set_page_config(page_title='Data Science & Stats', page_icon='📉', layout='centered')
logger = st.logger.get_logger(__name__)

st.header('Welcome!')

logger.info(f"Current Version: {os.environ.get('DOCKER_TAG')}")
