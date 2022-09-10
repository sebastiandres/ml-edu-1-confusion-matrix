import streamlit as st

#st.title("The experiments")
md = """
Let me show you how the previous experiments have worked out:

* Patient 0: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 1: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 2: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#0088ff;">blue pill</span>.
* Patient 3: We predicted <span style="color:#0088ff;">blue pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 4: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 5: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#0088ff;">blue pill</span>.
* Patient 6: We predicted <span style="color:#0088ff;">blue pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 7: We predicted <span style="color:#0088ff;">blue pill</span> and took <span style="color:#ff4400;">red pill</span>.
* Patient 8: We predicted <span style="color:#0088ff;">blue pill</span> and took <span style="color:#0088ff;">blue pill</span>.
* Patient 9: We predicted <span style="color:#ff4400;">red pill</span> and took <span style="color:#ff4400;">red pill</span>.

As you can see, not a stellar record.
Counting by hand, we get the following:

* **True Positive**: For only 1 persons we correctly predicted the preference for positive (<span style="color:#0088ff;">blue pill</span>)
* **True Negative**: For 4 persons we correctly predicted the preference for negative (<span style="color:#ff4400;">red pill</span>).
* **False Positive (Type I error)**: For 3 persons we predicted <span style="color:#0088ff;">blue pill</span> (positive) but people preferred the <span style="color:#ff4400;">red pill</span> (negative). This is sometimes called error type I.
* **False Negative (Type II error)**: For 2 persons we predicted <span style="color:#ff4400;">red pill</span> (negative) but people preferred the <span style="color:#0088ff;">blue pill</span> (positive). This is sometimes called error type II.

"""
st.markdown(md, unsafe_allow_html=True)