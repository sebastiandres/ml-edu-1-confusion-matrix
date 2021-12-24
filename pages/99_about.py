import streamlit as st

st.title("About")
md = """
## Conclusion

Hopefully, you have now a good understanding of confusion matrix and prediction metrics.

Please share and comment!

stb.share
Check out this cool confusion matrix interactive page
https://bit.ly/3phBbmf

## About the app

This web app was build with Streamlit, streamlit book, numpy, scikit learn, pandas and matplotlib.

Content and images have been taken from various sources, duly referenced where used.

Developped by [sebastiandres](sebastiandres.xyz)
"""
st.markdown(md, unsafe_allow_html=True)