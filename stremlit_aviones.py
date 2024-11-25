# -*- coding: utf-8 -*-
"""stremlit_aviones

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1woQmfP8of-9Sq2F73uKWzjn_MX8o7yOI
"""

# prompt: creame un stremlit que pueda mostrar mi base de datos

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('En este ejemplo usaremos la BBDD **flights.csv**')

# Upload the CSV file directly in the app
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        
        st.header('Primero que todo el head()')
        st.write(data.head())
        st.subheader('Revisemos algunos gráficos')

        # Crear gráfico
        fig, ax = plt.subplots()
        # Check if 'year' and 'passengers' columns exist in the DataFrame
        if 'year' in data.columns and 'passengers' in data.columns:
            ax.bar(data['year'], data['passengers'])
            st.pyplot(fig)
        else:
            st.write("Error: 'year' or 'passengers' column not found in the dataset.")

    except Exception as e:
        st.error(f"Error al cargar o procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo CSV.")