import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(page_title="Machine Learning Education", 
                    #layout="wide", 
                    page_icon="🤖")

# Streamit book properties
stb.set_book_config(path="pages", toc=True)

# Using a specific theme matrix: .streamlit/config.toml 
# See https://blog.streamlit.io/introducing-theming/