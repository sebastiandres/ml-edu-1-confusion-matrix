import streamlit as st
import streamlit_book as stb
import pandas as pd

st.title("Matrix to Metrics")
md = """
Any confusion matrix can be completely reduced to 4 variables:
* $T$: total number of cases
* $P$: number of (actual) positive cases
* $TP$: number of true positive cases
* $TN$: number of true negative cases

Having fixed those, we can always obtain the other variables:
* $N = T - P$: the number of (actual) negative cases.
* $FP = P - TP$: number of false positive cases
* $FN = N - TN$: number of false negative cases
* $PN = FP + FN$: predicted number of negative (false) cases
* $PP = TP + FP$: predicted number of positive (true) cases
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
Use the widget to see how changing any of these variables have an impact on the matrix:
"""
st.markdown(md, unsafe_allow_html=True)

if "P_rate" not in st.session_state:
    st.session_state.P_rate = 0.5
if "TP_rate" not in st.session_state:
    st.session_state.TP_rate = 0.5
if "TN_rate" not in st.session_state:
    st.session_state.TN_rate = 0.5


c1, c2, c3, c4 = st.columns(4)
# Slider for total. Is independent of others.
T = c1.slider(label="Total T", min_value=100, max_value=10000, value=1000, step=100)
# Slider for positive value. Depends on changes on Total
P_value = int(st.session_state.P_rate*T)
P = c2.slider(label="Positive P", min_value=0, max_value=T, 
                value=P_value, step=1)
st.session_state.P_rate = P/T
# Slider for true positive value. Depends on changes on Total
TP_value = int(st.session_state.TP_rate*P)
TP = c3.slider(label="True Positive TP", min_value=0, max_value=P, 
                value=TP_value, step=1)
st.session_state.TP_rate = TP/P
# Slider for true negative value. Depends on changes on Positive and Total
N = (T-P)
TN_value = int(st.session_state.TN_rate*N)
TN = c4.slider(label="True Negative TN", min_value=0, max_value=(T-P), value=TN_value, step=1)
st.session_state.TN_rate = TN/N

FN = N - TN
FP = P - TP
df = pd.DataFrame(data=[[f"Total = {T}", f"PP = {TP + FN}", f"PN = {FP + TN}"],
                        [f"P = {P}", f"TP = {TP}", f"FP = {FP}"],
                        [f"N = {N}", f"FN = {FN}", f"TN = {TN}"]], 
                        columns=["", "Prediction Positive", "Prediction Negative"])
st.write(df)

stb.share("sebastiandres.xyz", "My_text")