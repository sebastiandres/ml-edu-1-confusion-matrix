import streamlit as st

st.title("Matrix to Metrics")
md = """
Any confusion matrix can be completely reduced to 4 variables:
* $M$: total number of cases
* $P$: number of positive cases
* $TP$: true positive cases
* $TN$: true negative cases

Having fixed those, we can always obtain the other variables:
* $FP = P - TP$: false positive cases
* $FN = N - TN$: false negative cases
* $FP + FN$: total number of negative (false) cases
* $TP + FP$: total number of positive (true) cases
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
Use the widgets to see how changing any of these variables have an impact on the matrix and on the metrics.
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
Interactive app!
"""
st.markdown(md, unsafe_allow_html=True)