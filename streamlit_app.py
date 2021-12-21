import streamlit as st
import streamlit_book as stb

from code import magic

# Streamlit webpage properties
st.set_page_config(page_title="Confusion Matrix", 
                    layout="centered")

# Streamit book properties
stb.set_book_config(path="pages",
                    button="both",
                    button_next="Next",
                    button_previous="Previous",
                    button_refresh="Reload",
                    on_load_header=magic.matrix_effect,
                    #on_load_footer=magic.matrix_effect,
                    toc=False)

# Using a specific theme matrix: .streamlit/config.toml 
# See https://blog.streamlit.io/introducing-theming/