import streamlit as st
import time

from code import magic

# This helps accelerating for debug purposes
SECS = 1
QUESTION = "This is your last chance. After this, there is no turning back."
BLUE_PILL = "You take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. "
RED_PILL = "You take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes."

def button_on_click(pill, BLUE_PILL=BLUE_PILL, SECS=SECS):
    from code import magic
    if pill==BLUE_PILL:
        st.success("Are you sure? \n You've been down there, Neo. \nYou already know that road. \nYou know exactly where it ends. \nAnd I know that's not where you want to be")
        st.session_state["do_matrix_effect"] = False
    else:
        st.session_state["do_matrix_effect"] = True
        with st.spinner("Buckly up Dorothy, because Kansas is going bye-bye!"):
            magic.pause(2.0*SECS)
        st.session_state["button"] = st.session_state["default_button"]      

if "do_matrix_effect" not in st.session_state:
    st.session_state["do_matrix_effect"] = False

if "page_run_count" not in st.session_state:
    st.session_state["page_run_count"] = 0
    st.session_state["default_button"] = st.session_state.button
    st.session_state.button = ""
else:
    st.session_state["page_run_count"] += 1

if st.session_state["do_matrix_effect"]:
    magic.matrix_effect(height=400, sleep_time=3)

if st.session_state["page_run_count"] == 0:
    # Blinking effect, only on first run
    magic.blinking_effect(blinking_time=0.5*SECS, blinking_duration=2.5*SECS)

#######################################
# CODE BEFORE SELECTION OR ON BLUE PILL
if not st.session_state.do_matrix_effect:
    md = """
    Hello Neo.               
    You know why you're here.              
    It's the question that drives us, Neo. 
    It's the question that brought you here. You know the question, just as I did.
    What is the **_Confusion Matrix_**?            
    Unfortunately, no one can be told what the **_Confusion Matrix_** is. You have to learn it for yourself.
    """
    # Render line by line if first time, otherwise render whole text
    for line in md.split("\n"):
        st.markdown(line, unsafe_allow_html=True)
        if st.session_state["page_run_count"] == 0:
            magic.pause(SECS * len(line) / 30) # 30 chars per second
    if st.session_state["page_run_count"] == 0:
        magic.pause(1*SECS)

    # Do the pill question!
    pill = st.radio(QUESTION, [BLUE_PILL, RED_PILL])
    st.button("What do you choose, Neo?", on_click=button_on_click, args=(pill,))    

####################################
# CODE ON RED PILL
# Let's go: click on next
if st.session_state.do_matrix_effect:
    md = """
    Use the arrows to navigate through the content. 
    
    Some pages will have interactive content that should be self-explanatory.
    
    Now click on Next to start the journey, Neo!
    """
    st.markdown(md)
