import streamlit as st
import streamlit_book as stb
import pandas as pd

st.session_state["do_matrix_effect"] = False

md = """
Use the widget to construct any confusion matrix:
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

# The code to write the confusion matrix
FP = N - TN
FN = P - TP
labels = ["red pill", "blue pill"]
index = [["actual values" for _ in labels], labels]
cols = [["prediction" for _ in labels], labels]
df_CM = pd.DataFrame(index=index, columns=cols, data=[[TN, FP], [FN, TP]])
#st.write(df_CM)
# This is a small hack that shows the dataframe better in streamlit
st.markdown(df_CM.to_html(), unsafe_allow_html=True)