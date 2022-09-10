import streamlit as st

md = """
So we work with the following convention for confusion matrices:

<img src="https://github.com/sebastiandres/ml_edu_confusion_matrix/blob/main/images/confusion_matrix1.png?raw=true" alt="Conventions" width="700">

The true condition is fixed. What's positive is positive and what's negative is negative. You cannot change reality (at least for now, Neo). 
So the total of Positive $P$ and Negative $N$, and the total number of patients $T$ is fixed. 
Only your predictions can change, altering the true positive, true negative, false positive, and false negative.

Therefore, any confusion matrix can be completely reduced to 4 variables:
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

<img src="https://github.com/sebastiandres/ml_edu_confusion_matrix/blob/main/images/confusion_matrix2.png?raw=true" alt="Conventions" width="700">

From this, we get that true positive, true negative, 
false positive and false negative have specific trivial boundaries:

* $0 \leq TP, FN \leq P$
* $0 \leq TN, FP \leq N$

Nevertheless, $TP + FP$ and $FN + TN$ do not have a similar boundary as they depend on the prediction, 
and at most can be bounded directly by $M$.
"""
st.markdown(md, unsafe_allow_html=True)