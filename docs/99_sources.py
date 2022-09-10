import streamlit as st
import streamlit_book as stb

md = """
# Sources

* Matrix Effect: using the pure html version of the [matrix effect](https://github.com/javascriptacademy-stash/digital-rain) 

* Error types, false positives and false negatives: [Chris Albon's machine learning flashcards](https://machinelearningflashcards.com/).

* Confusion Matrix displays:
  * [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
  * [pandas](https://datatofish.com/confusion-matrix-python/)

* Sharing buttons: Inspired by awesomeness of [sharingbuttons.io](https://sharingbuttons.io/)
"""
st.markdown(md, unsafe_allow_html=True)