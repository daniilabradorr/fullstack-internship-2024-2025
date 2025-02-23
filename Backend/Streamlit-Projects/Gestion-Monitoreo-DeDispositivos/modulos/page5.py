import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from funciones_comunes import connect_and_load_data

def page5():
    st.title("Salud General de Dispositivos por Departamento y Estado")
    st.markdown("Gráfico de Radar interactivo que muestra la salud de los dispositivos según su estado y departamento")

    # Cargar los datos de dispositivos
    df = connect_and_load_data()

    if df is not None:
        # Definir departamentos y estados
        departments = df['department'].unique().tolist()
        statuses = df['status'].unique().tolist()

        # Crear un diccionario para almacenar los valores por estado y departamento
        health_data = {department: {status: 0 for status in statuses} for department in departments}

        # Contar los dispositivos en cada estado por departamento
        for department in departments:
            for status in statuses:
                count = len(df[(df['department'] == department) & (df['status'] == status)])
                health_data[department][status] = count

        # Crear los ejes para el gráfico de radar
        axes = statuses  # Usamos los estados como los ejes

        # Crear la figura para el gráfico de radar
        fig_radar = go.Figure()

        # Agregar los datos de cada departamento como una "traza"
        for department in departments:
            values = [health_data[department][status] for status in statuses]
            fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=axes,
                fill='toself',
                name=department
            ))

        # Configurar el diseño del gráfico de radar
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(max(list(health_data[department].values())) for department in health_data)]
                )
            ),
            showlegend=True,
            title={
                'text': '📊 Distribución de Dispositivos por Estado en cada Departamento',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center',  # Anclar en el centro
                'yanchor': 'top'  # Anclar en la parte superior
            },
        )

        # Mostrar el gráfico de radar en Streamlit
        st.plotly_chart(fig_radar)

        # Crear gráfico de barras con estado de dispositivos
        # Contamos los dispositivos por departamento y estado
        devices_by_department_status = df.groupby(['department', 'status']).size().reset_index(name='Número de Dispositivos')

        # Crear el gráfico de barras
        fig_bar = px.bar(devices_by_department_status, 
                         x='department', 
                         y='Número de Dispositivos', 
                         color='status',  # Usamos el estado como color
                         color_discrete_map={
                             'en uso': 'lightblue', 
                             'en desuso': 'lightgreen', 
                             'en reparación': 'lightcoral'
                         },
                         title= "📊 Número de Dispositivos por Departamento y Estado",
                         labels={'department': 'Departamento', 'Número de Dispositivos': 'Cantidad de Dispositivos'},
                         template="plotly_dark",
                         barmode='stack'  # Usamos un modo apilado para que los estados se apilen por departamento
        )

        # Mejorar la apariencia del gráfico de barras
        fig_bar.update_layout(
            xaxis_tickangle=-45,  # Rotar las etiquetas del eje X
            xaxis_title="Departamento",
            yaxis_title="Número de Dispositivos",
            title={
                    'x': 0.5,  # Centrar el título
                    'xanchor': 'center',  # Anclar en el centro
                    'yanchor': 'top'  # Anclar en la parte superior
                },
        )

        # Mostrar el gráfico de barras debajo del gráfico de radar
        st.plotly_chart(fig_bar)