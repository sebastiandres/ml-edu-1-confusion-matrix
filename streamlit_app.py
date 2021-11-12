import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

def error_function(x, y, model):
    y_model = model(x)
    square_diff = np.sum( (y - y_model)**2 )
    normalized_error = (square_diff / x.shape[0] )**.5
    #st.write(square_diff, normalized_error, x.shape[0])
    return normalized_error

def model_eval(x, y, model):
    x_min = np.min(x)
    x_max = np.max(x)
    x = np.linspace(x_min, x_max)
    y = model(x)
    return {"x":x, "y":y}

# Parameters
x_min, x_max = -5, +5

# True function
def p_n(x):
    return (x-4)*x*(x+4) / 20

# Set wide display
st.set_page_config(layout="wide")
st.title("ML Edu")
st.subheader("Educación en Machine Learning")

if "x_train" not in st.session_state: st.session_state["x_train"] = np.array([])    
if "y_train" not in st.session_state: st.session_state["y_train"] = np.array([])
if "x_test" not in st.session_state: st.session_state["x_test"] = np.array([])
if "y_test" not in st.session_state: st.session_state["y_test"] = np.array([])
if "x_val" not in st.session_state: st.session_state["x_val"] = np.array([])
if "y_val" not in st.session_state: st.session_state["y_val"] = np.array([])
# Side Bar
## Generar datos
st.sidebar.write("**Definición del dataset**")
E = st.sidebar.slider("Error Promedio", min_value=0.01, max_value=2.0, value=1.0, step=0.1)
N = st.sidebar.slider("Tamaño dataset", min_value=100, max_value=10000, value=100, step=100) 
st.sidebar.write("**Propiedades del entrenamiento**")
train_size = st.sidebar.slider("Porcentaje datos entrenamiento", min_value=0, max_value=100, value=70, step=5)
dataset_generado = st.sidebar.button("Generar dataset")
if dataset_generado:
    # Dataset
    x = x_min + np.random.rand(N)*(x_max-x_min)
    y = p_n(x) + np.random.normal(scale=E, size=N)
    # Split
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_size/100)
    st.session_state["x_train"] = x_train
    st.session_state["y_train"] = y_train
    st.session_state["x_test"] = x_test
    st.session_state["y_test"] = y_test
    # Validation dataset
    N_val = 100
    x_min, x_max = 1.5*x_min, 1.5*x_max
    x = x_min + np.random.rand(N_val)*(x_max-x_min)
    y = p_n(x) + np.random.normal(scale=E, size=N_val)
    st.session_state["x_val"] = x
    st.session_state["y_val"] = y
    if "model" in st.session_state:
        del st.session_state["model"]
    if "model_values" in st.session_state:
        del st.session_state["model_values"]
    if "error" in st.session_state:
        del st.session_state["error"]

## Modelo
st.sidebar.write("**Metaparámetros**")
n = st.sidebar.slider("Grado del polinomio", min_value=1, max_value=15, value=1)
if st.sidebar.button("Ajustar modelo"):
    z = np.polyfit(st.session_state["x_train"], st.session_state["y_train"], n)
    p_model = np.poly1d(z)
    st.session_state["model_values"] = z
    #x_model = np.linspace(x_min, x_max)
    #y_model = p_model(x_model)
    #st.session_state["model"] = (x_model, y_model)
    st.session_state["model"] = p_model
    E_train = error_function( st.session_state["x_train"], st.session_state["y_train"], p_model)
    E_test = error_function( st.session_state["x_test"], st.session_state["y_test"], p_model)
    E_val = error_function( st.session_state["x_val"], st.session_state["y_val"], p_model)
    st.session_state["error"] = {"train":E_train, "test":E_test, "val":E_val}

## Mostrar validation set?
show_val = st.sidebar.checkbox("Mostrar set validacion")

## Autor
st.sidebar.markdown("Creado por [sebastiandres](https://sebastiandres.xyz)") 

# Main view
## Model
st.write("Modelo:")
latex = "a_0 + " + " + ".join("a_{"+str(i)+"} x^{"+str(i)+"}" for i in range(1,n+1))
st.latex(latex)
fit_model_text = st.empty()
fit_model_values = st.empty()
if "model" in st.session_state:
        fit_model_text.write("Modelo ajustado:")
        a = list(st.session_state["model_values"])[::-1]
        #st.write(a, type(a))
        latex = f"{a[0]:+.3f} " + " ".join(f"{a[i]:+.3f} " + " x^{"+ str(i)+"}" for i in range(1, len(a)))
        fit_model_values.latex(latex)

## Graphs
c1, c2, c3 = st.columns(3)
fig = plt.figure()
plt.plot(st.session_state["x_train"], st.session_state["y_train"], 'k.', alpha=0.5)
if "model" in st.session_state:
    model_train = model_eval(st.session_state["x_train"], st.session_state["y_train"], st.session_state["model"])
    plt.plot(model_train["x"],model_train["y"], 'r', lw=2.0)
    #plt.plot(st.session_state["model"][0], st.session_state["model"][1], 'r', lw=2.0)
title = f"Set de entrenamiento, {st.session_state['x_train'].shape[0]:,d} puntos"
if "error" in st.session_state:
    title += f"\nError = {st.session_state['error']['train']:.2f}"
plt.suptitle(title)
plt.xlabel("x")
plt.ylabel("y")
c1.pyplot(fig)

fig = plt.figure()
plt.plot(st.session_state["x_test"], st.session_state["y_test"], 'k.', alpha=0.5)
if "model" in st.session_state:
    model_test = model_eval(st.session_state["x_test"], st.session_state["y_test"], st.session_state["model"])
    plt.plot(model_test["x"], model_test["y"], 'r', lw=2.0)
    #plt.plot(st.session_state["model"][0], st.session_state["model"][1], 'r', lw=2.0)
title = f"Set de testeo, {st.session_state['x_test'].shape[0]:,d} puntos"
if "error" in st.session_state:
    title += f"\nError = {st.session_state['error']['test']:.2f}"
plt.suptitle(title)
plt.xlabel("x")
plt.ylabel("y")
c2.pyplot(fig)

if show_val:
    fig = plt.figure()
    plt.plot(st.session_state["x_val"], st.session_state["y_val"], 'k.', alpha=0.5)
    if "model" in st.session_state:
        model_val = model_eval(st.session_state["x_val"], st.session_state["y_val"], st.session_state["model"])
        plt.plot(model_val["x"],model_val["y"], 'r', lw=2.0)
        #plt.plot(st.session_state["model"][0], st.session_state["model"][1], 'r', lw=2.0)
    title = f"Set de validación, {st.session_state['x_val'].shape[0]:,d} puntos"
    if "error" in st.session_state:
        title += f"\nError = {st.session_state['error']['val']:.2f}"
    plt.suptitle(title)
    plt.xlabel("x")
    plt.ylabel("y")
    c3.pyplot(fig)