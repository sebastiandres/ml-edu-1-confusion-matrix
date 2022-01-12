import streamlit as st
import streamlit_book as stb

md = """
# Sources

* Matrix Effect: using the pure html version of the [matrix effect]() 

* Error types, false positives and false negatives: Chris Albon's machine learning flashcards.

* Confusion Matrix displays:
  * [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
  * [pandas]()

* Styling pandas tables: https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
"""
st.markdown(md, unsafe_allow_html=True)