import streamlit as st

md = """
You can use pandas to print it in a more readable way.

```python
import pandas as pd
```
"""
st.markdown(md, unsafe_allow_html=True)

st.write("df")

md = """
If you want to get fancy and show it in matplotlib:

```python
from sklearn.metrics import ConfusionMatrixDisplay
CM_fig = ConfusionMatrixDisplay.from_predictions(true_condition, pred_condition)
print(type(CM_fig))
st.pyplot(CM_fig)
```
"""
st.markdown(md, unsafe_allow_html=True)

true_condition = [0,0,0,1,0,0,1,1,1,0]
pred_condition = [0,0,1,0,0,1,0,0,1,0]
from sklearn.metrics import ConfusionMatrixDisplay
from matplotlib import pyplot as plt
ConfusionMatrixDisplay.from_predictions(true_condition, pred_condition, cmap="gray_r")
CM_fig = plt.gcf()
st.pyplot(CM_fig)
