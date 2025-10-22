import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("calculadora de figuras trigonometricas 🎨")
st.sidebar.write("Nombre: Sasha Torres Davidson, Matricula: 385944. Grupo: 3L")

# Selección de figura
figura = st.selectbox("Selecciona una figura", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

# Círculo
if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.0, 20.0, 5.0)
# calculo del area
    area = math.pi * radio**2
#calculo del perimetro
    perimetro = 2 * math.pi * radio
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Triángulo
elif figura == "Triángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 20.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 20.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 20.0, 5.0)
# calculo del area
    area = 0.5 * base * altura
# calculo del perimetro
    perimetro = lado_a + lado_b + lado_c
#resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Rectángulo
elif figura == "Rectángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
# calculo del area
    area = base * altura
# calculo del perimetro
    perimetro = 2 * (base + altura)
# calculos
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Cuadrado
elif figura == "Cuadrado":
    lado = st.slider("Selecciona el lado", 0.0, 20.0, 5.0)
# calculo del area
    area = lado**2
# calculo del perimetro
    perimetro = 4 * lado
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Selector de color
color = st.color_picker("Selecciona el color del borde", "#00f900")

# Crear figura de matplotlib
fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), radio, color=color, fill=False)
    ax.add_artist(circle)
    ax.set_xlim(-radio - 1, radio + 1)
    ax.set_ylim(-radio - 1, radio + 1)

elif figura == "Cuadrado":
    square = plt.Rectangle((-lado/2, -lado/2), lado, lado, edgecolor=color, fill=False)
    ax.add_artist(square)
    ax.set_xlim(-lado, lado)
    ax.set_ylim(-lado, lado)

elif figura == "Rectángulo":
    rect = plt.Rectangle((-base/2, -altura/2), base, altura, edgecolor=color, fill=False)
    ax.add_artist(rect)
    ax.set_xlim(-base, base)
    ax.set_ylim(-altura, altura)

elif figura == "Triángulo":
    x = [-base/2, base/2, 0]
    y = [0, 0, altura]
    triangle = plt.Polygon(list(zip(x, y)), edgecolor=color, fill=False)
    ax.add_artist(triangle)
    ax.set_xlim(-base, base)
    ax.set_ylim(0, altura + 2)

# Configuración final del gráfico
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# Selección de función
funcion = st.selectbox("Selecciona una función", ["sin(x)", "cos(x)", "tan(x)"])

# Parámetros
rango_max = st.slider("Rango máximo (x)", np.pi, 4 * np.pi, 2 * np.pi)
amplitud = st.slider("Amplitud", 0.1, 2.0, 1.0)

# Generar valores
x = np.linspace(0, rango_max, 300)

# Graficar función seleccionada
st.write(f"Función seleccionada: {funcion}")

if funcion == "sin(x)":
    y = amplitud * np.sin(x)
elif funcion == "cos(x)":
    y = amplitud * np.cos(x)
elif funcion == "tan(x)":
    y = amplitud * np.tan(x)
    y = np.clip(y, -10, 10)  # limitar valores extremos para tan(x)

# Mostrar gráfico
fig, ax = plt.subplots()
ax.plot(x, y, label=funcion)
ax.set_title(f"Gráfica de {funcion}")
ax.grid(True)
ax.legend()
st.pyplot(fig)
