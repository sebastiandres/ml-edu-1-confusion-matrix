import streamlit as st

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

md = """
A problem is defined by the total of known cases (labels) ($M$) and the total number of positive ($P$) and negative labels ($N$). As we have $M = P + N$, we must have $0 \leq P , N \leq M$.

From this, we get that true positive, true negative, false positive and false negative have specific trivial boundaries:
$ 0 \leq TP, FN \leq P (\leq M)$
$ 0 \leq TN, FP \leq N (\leq M)$
Nevertheless, $TP + FP$ and $FN + TN$ do not have a similar boundary as they depend on the prediction, and at most can be bounded directly by $M$. Indeed, we could end up with the border cases: 
* $TP + FP = P + N = M$ with $FN + TN = 0 + 0 = 0$
* $FP + TN = 0 + 0 = 0$ with $TP + FN = P + N = M$
"""
st.markdown(md, unsafe_allow_html=True)