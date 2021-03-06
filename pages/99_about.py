import streamlit as st
import streamlit_book as stb

md = """
Your training has ended. For now.

Hopefully, you have now a good understanding of confusion matrix.
"""
st.markdown(md, unsafe_allow_html=True)

st.header("About the app")
md = """
This web app was build with Streamlit, streamlit book, numpy, scikit learn, pandas and matplotlib.

Content and images have been taken from various sources.

Developped by [sebastiandres](http://sebastiandres.xyz)
"""
st.markdown(md, unsafe_allow_html=True)

st.header("Sharing")
md = """
Please share and comment!
"""
st.markdown(md, unsafe_allow_html=True)
stb.share("https://bit.ly/3phBbmf", "Check out this cool confusion matrix interactive page")
