import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + x + 1
def g(x):
    return x**2
def h(x):
    return x

st.title("Análisis Interactivo de Complejidad: f(x) = x^2 + x + 1")
st.write("")
st.sidebar.header("Parámetros")
x_min = st.sidebar.slider('Valor mínimo de x', min_value=0, max_value=50, value=0)
x_max = st.sidebar.slider('Valor máximo de x', min_value=10, max_value=100, value=20)
num_points = st.sidebar.slider('Cantidad de puntos en el gráfico', min_value=100, max_value=1000, value=400)
st.sidebar.write("""
Puedes ajustar el rango de x para observar cómo se comporta la función en diferentes intervalos.
El gráfico compara la función $f(x)$ con $O(x^2)$ y $O(x)$.
""")
x_vals = np.linspace(x_min, x_max, num_points)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_vals, f(x_vals), label='f(x) = $x^2 + x + 1$', color='blue', linewidth=2)
ax.plot(x_vals, g(x_vals), label='O($x^2$)', color='green', linestyle='--', linewidth=2)
ax.plot(x_vals, h(x_vals), label='O(x)', color='red', linestyle='--', linewidth=2)
ax.set_title('Comparación de f(x) con O(x^2) y O(x)', fontsize=16)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('Valor de la función', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)
st.pyplot(fig)
st.write("")
st.write("""
### Conclusión:
- $f(x) = x^2 + x + 1$ pertenece a la clase de complejidad **O($x^2$)**, pero no **O(x)**.
""")
