import streamlit as st

md = """
You can use pandas to print it in a more readable way, renaming the columns and rows:

```python
import pandas as pd
from sklearn.metrics import confusion_matrix

true_condition = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
pred_condition = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
CM = confusion_matrix(true_condition, pred_condition)
labels = ["red pill", "blue pill"]
index = [["actual values" for _ in labels], labels]
cols = [["prediction" for _ in labels], labels]
df_CM = pd.DataFrame(index=index, columns=cols, data=CM)
```

will produce the following output:
"""
st.markdown(md, unsafe_allow_html=True)

# The actual code
import pandas as pd
from sklearn.metrics import confusion_matrix

true_condition = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
pred_condition = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
CM = confusion_matrix(true_condition, pred_condition)
labels = ["red pill", "blue pill"]
index = [["actual values" for _ in labels], labels]
cols = [["prediction" for _ in labels], labels]
df_CM = pd.DataFrame(index=index, columns=cols, data=CM)
#st.write(df_CM)
# This is a small hack that shows the dataframe better in streamlit
st.markdown(df_CM.to_html(), unsafe_allow_html=True)

md = """
<br><br>
You can even get fancy and show it in matplotlib:

```python
from sklearn.metrics import ConfusionMatrixDisplay
CM_fig = ConfusionMatrixDisplay.from_predictions(true_condition, pred_condition)
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
