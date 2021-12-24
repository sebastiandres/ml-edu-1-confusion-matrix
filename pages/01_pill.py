import streamlit as st
import time

from code import magic

#st.session_state["page_run_count"] = 1

if "page_run_count" not in st.session_state:
    st.session_state["page_run_count"] = 0
    st.session_state["default_button"] = st.session_state.button
    st.session_state.button = ""
else:
    st.session_state["page_run_count"] += 1

# Blinking effect, only on first run
if st.session_state["page_run_count"] == 0:
    magic.blinking_effect()

matrix_effect_placeholder = st.empty()
md = """
Hello Neo.               
You know why you're here.              
It's the question that drives us, Neo. 
It's the question that brought you here. You know the question, just as I did.
What is the **_Confusion Matrix_**?            
Unfortunately, no one can be told what the **_Confusion Matrix_** is. You have to learn it for yourself.
This web app will try explain the terminology used in classification systems, confusion matrix and prediction metrics (accuracy, recall, type I/II error, et cetera). 
Use the arrows to navigate through the content. Some pages will have interactive content that should be self-explanatory.
"""
# Render line by line if first time, otherwise render whole text
if st.session_state["page_run_count"] == 0:
    for line in md.split("\n"):
        st.markdown(line, unsafe_allow_html=True)
        time.sleep(len(line) / 30)
    time.sleep(1.0)
else:
    st.markdown(md.replace("\n", "\n\n"), unsafe_allow_html=True)

# Do the pill question!
QUESTION = "This is your last chance. After this, there is no turning back."
BLUE_PILL = "You take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. "
RED_PILL = "You take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes."
pill = st.radio(QUESTION, [BLUE_PILL, RED_PILL])
if st.button("What do you choose, Neo?"):
    if pill==BLUE_PILL:
        st.success("Are you sure? \n You've been down there, Neo. \nYou already know that road. \nYou know exactly where it ends. \nAnd I know that's not where you want to be")
    else:
        with st.spinner("Buckly up Dorothy, because Kansas is going bye-bye!"):
            time.sleep(1.0)
        st.session_state["do_matrix_effect"] = True
        st.session_state["button"] = "both"        
        magic.matrix_effect(height=400, sleep_time=3)
        