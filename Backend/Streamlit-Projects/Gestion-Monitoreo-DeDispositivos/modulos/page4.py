import streamlit as st
import plotly.express as px
from funciones_comunes import connect_and_load_data

def page4():
    st.title("Nº Dispositivos x Puertos")
    st.markdown("Gráfico del número de dispositivos integrados en cada Puerto")
    
    df = connect_and_load_data()

    if df is not None:
        # Contar la cantidad de dispositivos por puerto
        devices_by_ports = df['port'].value_counts().reset_index()  # 'port' es la columna correcta
        devices_by_ports.columns = ['Puerto', 'Número de Dispositivos']  # Establecemos los nombres correctos de columnas

        # Verificar los nombres de las columnas para asegurarse de que coinciden con los del gráfico
        # st.write(devices_by_ports.columns)  # Esto te ayudará a verificar que los nombres son correctos

        # Crear gráfico de dispersión
        fig_ports = px.scatter(devices_by_ports, 
                               x='Puerto', 
                               y='Número de Dispositivos',  # Asegúrate de que el nombre de la columna coincida
                               title="Dispositivos por Puerto",
                               labels={'Puerto': 'Puerto', 'Número de Dispositivos': 'Cantidad de Dispositivos'},
                               color='Puerto',  # Opcional, para usar color según el puerto
                               template="plotly_dark")

        # Mejorar la apariencia
        fig_ports.update_layout(
            xaxis_title="Puerto",
            yaxis_title="Número de Dispositivos",
            title={
                'text': '📊 Dispositivos por Puerto',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center',  # Anclar en el centro
                'yanchor': 'top'  # Anclar en la parte superior
            },
            showlegend=False
        )

        st.plotly_chart(fig_ports)  # Mostrar el gráfico en Streamlit