import streamlit as st
import streamlit_book as stb

from code import magic

# Streamlit webpage properties
st.set_page_config(page_title="Confusion Matrix", 
                    layout="centered")

# Streamit book properties
stb.set_chapter_config(
                        path="docs",
                        button="bottom",
                        button_next="Next",
                        button_previous="Previous",
                        button_refresh="Reload",
                        on_load_header=magic.matrix_effect,
                        toc=False)

# Using a specific theme from The Matrix: .streamlit/config.toml 
# See https://blog.streamlit.io/introducing-theming/
