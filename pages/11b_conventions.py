import streamlit as st

st.title("Conventions")
md = """
A confusion matrix is an arragement of the countings of each of these outcome posibilities. 
To create a confusion matrix, there are some arbitrarily decision regarding order and orientation. 
There are 4 options, as shown on the picture:

<img src="https://github.com/sebastiandres/ml_edu_confusion_matrix/blob/main/images/conventions.png?raw=true" alt="Conventions" width="700">

As you can see, the differences are essencially if rows should be the true condition or prediction, 
and if values should be in order positive-negative, or negative-positive. 

As in any arbitrary choice, not everyone will agree and use the same. Be careful when reading and interpreting the results!

"Convention A" is the convention explained by [wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix).

"Convention B" is used by [scikit learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html). 

"Convention C" is the convention taken by Andrew Ng's on his [courses on Machine Learning](https://medium.com/@aiii/machine-learning-diagnostics-b2256d78d51e). 

"Convention D" is not frequently used, as far as I know. 

There is a nice discussion on [stackoverflow](https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed) regarding  this issue.

We will take the convention B (easier to generalize to multiclass), and use that convention on the rest of the explanations.
"""
st.markdown(md, unsafe_allow_html=True)