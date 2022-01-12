# Helper functions for matrix effect

import streamlit as st
from streamlit.components.v1 import html
import time

def blinking_effect(blinking_time=0.5, blinking_duration=2.5):
    c = st.empty()
    for i in range(int(blinking_duration/blinking_time)):
        c.markdown("▉")
        time.sleep(blinking_time)
        c.markdown("")
        time.sleep(blinking_time)

def matrix_effect(height=1600, sleep_time=3):
    """
    Applies the matrix effect to the current page.
    """
    # If not required, skip the matrix effect
    if "do_matrix_effect" not in st.session_state:
        return
    if not st.session_state["do_matrix_effect"]:
        return
    # If not, do the effect.
    if "count" not in st.session_state:
        st.session_state.count = 0
    st.session_state.count += 1
    my_id=f"Matrix{st.session_state.count}"
    my_html = """
    <canvas id="Matrix"></canvas>
    <script>
    const canvas = document.getElementById('Matrix');
    const context = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
    const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const nums = '0123456789';

    const alphabet = katakana + latin + nums;

    const fontSize = 16;
    const columns = canvas.width/fontSize;

    const rainDrops = [];

    for( let x = 0; x < columns; x++ ) {
        rainDrops[x] = 1;
    }

    const draw = () => {
        context.fillStyle = 'rgba(0, 0, 0, 0.05)';
        context.fillRect(0, 0, canvas.width, canvas.height);
        
        context.fillStyle = '#0F0';
        context.font = fontSize + 'px monospace';

        for(let i = 0; i < rainDrops.length; i++)
        {
            const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
            context.fillText(text, i*fontSize, rainDrops[i]*fontSize);
            
            if(rainDrops[i]*fontSize > canvas.height && Math.random() > 0.975){
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    };

    setInterval(draw, 30);

    setTimeout(() => {  
        var elem = document.getElementById("Matrix");
        elem.remove();
    }, timer_time);

    </script>
    """.replace("Matrix", my_id).replace("timer_time", str(int(sleep_time*1000)))
    # Render the html
    placeholder = html(my_html, height=height)
    time.sleep(sleep_time)
    placeholder.empty()
    return