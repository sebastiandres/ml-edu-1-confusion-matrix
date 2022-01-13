import streamlit as st

#st.title("The code")
md = """
Doing all work by hand is wasteful. Let's put everything in vectors and use python libraries!

```python
true_condition = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
pred_condition = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
```

As you can see, the person `i` was predicted `pred_condition[i]` 
but in reality we obtained `true_condition[i]`. 

We can automate the counting process with the following code:

The confusion matrix can be computed easily as:

```python
from sklearn.metrics import confusion_matrix
CM = confusion_matrix(true_condition, pred_condition)
```
"""
st.markdown(md, unsafe_allow_html=True)

true_condition = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
pred_condition = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
from sklearn.metrics import confusion_matrix
CM = confusion_matrix(true_condition, pred_condition)
st.write(CM)

md = """
Sometimes people unwrap the values as follows

```python
from sklearn.metrics import confusion_matrix
TN, FP, FN, TP = confusion_matrix(true_condition, pred_condition).ravel()
```

So we obtain:
"""
st.markdown(md, unsafe_allow_html=True)

from sklearn.metrics import confusion_matrix
TN, FP, FN, TP = confusion_matrix(true_condition, pred_condition).ravel()
st.code(f"True Negatives, TN = {TN} \nFalse Positives, FP = {FP}\nFalse Negatives, FN = {FN}\nTrue Positives, TP = {TP}")