import streamlit as st

md = """
**Confusion matrices** are used to evaluate the performance of a classification algorithm. 

In our case, Neo, we need to predict what pill a person will take: red or blue. 

The <span style="color:#ff4400;">red pill</span> is the base or negative case. People that prefers to keep living as usual.

The <span style="color:#0088ff;">blue pill</span> is the positive case. People that wants to learn about the confusion matrix, like us.

We want to be as good as posible: anyone who ends up taking the red pill is a waste or time and valuable resources we could be using
on people wanting to take the blue pill. 

After making a prediction with the algoritm, we can contrast the prediction with the ground truth. 

There are 4 posibilities:
* **True Positive**: We correctly predicted the preference for positive (<span style="color:#0088ff;">blue pill</span>).
* **True Negative**: We correctly predicted the preference for negative (<span style="color:#ff4400;">red pill</span>).
* **False Positive**: We predicted <span style="color:#0088ff;">blue pill</span> (positive) but people preferred the <span style="color:#ff4400;">red pill</span> (negative). This is sometimes called error type I.
* **False Negative**: We predicted <span style="color:#ff4400;">red pill</span> (negative) but people preferred the blue one (positive). This is sometimes called error type II.

Remembering the definitions of type I and type II is hard because is completely arbitrary. 
One way to rememeber is Chris Albon's mnemotechtic rule:

<img src="https://github.com/sebastiandres/ml_edu_confusion_matrix/blob/main/images/error_types.png?raw=true" alt="Conventions" width="700">

"""
st.markdown(md, unsafe_allow_html=True)