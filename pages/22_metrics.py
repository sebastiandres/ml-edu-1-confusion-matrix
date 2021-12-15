import streamlit as st

st.title("Metrics")
md = """
From the confusion matrix, the following metrics are usually defined:
* Accuracy: $Acc = (TP + TN) / M$
* Precision: $Prec = TP / (TP + FP)$
* Recall: $Rec = TP / (TP + FN)$
* Specificity: $Spec = TN / (TN + FP)$
* F1-score: $F1 = 2 * (Prec * Rec) / (Prec + Rec)$
* False Negative Rate (FNR): $FNR = FN / N$
* False Positive Rate (FPR): $FPR = FP / P$
* True Positive Rate (TPR): $TPR = TP / P$
* True Negative Rate (TNR): $TNR = TN / N$
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
Notice that if two matrices are identically except for scaling (linear transformation), they will have the same metrics.):
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
Interactive app!
"""
st.markdown(md, unsafe_allow_html=True)

md = """"
From this, we learn that the metrics do not uniquely defined a confusion matrix."""
st.markdown(md, unsafe_allow_html=True)
