import streamlit as st
import plotly.express as px
from funciones_comunes import connect_and_load_data

def page3():
    st.title("Nº Dispositivos x Departamento")
    st.markdown("Gráfico de Barras Interactivo del Número de dispositivos por Departamento")

    # Cargar los datos de dispositivos
    df = connect_and_load_data()

    if df is not None:
        # Contar la cantidad de dispositivos por departamento
        devices_by_department = df['department'].value_counts().reset_index()
        devices_by_department.columns = ['Departamento', 'Número de Dispositivos']

        # Colores según departamento
        department_colors = {
            "Producción": "lightblue",
            "Calidad": "lightgreen",
            "Logística": "lightcoral",
            "Mantenimiento": "lightyellow"
        }

        # Crear gráfico de barras interactivo con Plotly
        fig = px.bar(devices_by_department, 
                     x='Departamento', 
                     y='Número de Dispositivos', 
                     color='Departamento',
                     color_discrete_map=department_colors,
                     title="Número de Dispositivos por Departamento",
                     labels={'Departamento': 'Departamento', 'Número de Dispositivos': 'Cantidad de Dispositivos'},
                     template="plotly_dark")

        # Mejorar la apariencia
        fig.update_layout(
            xaxis_tickangle=-45,  # Rotar las etiquetas del eje X
            barmode='group',
            xaxis_title="Departamento",
            yaxis_title="Número de Dispositivos",
            title={
                'text': '📊 Número de Dispositivos por Departamento',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center',  # Anclar en el centro
                'yanchor': 'top'  # Anclar en la parte superior
            },
        )

        # Mostrar el gráfico interactivo en Streamlit
        st.plotly_chart(fig)