import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from funciones_comunes import count_pending_requests

def page7():
    st.title("📱 Estado de Petición de Nuevos Dispositivos")
    st.markdown("Gráfico y tabla del estado (Administrada) de la petición de los nuevos dispositivos")

    #Mensaje de aviso de Peticiones pendientes
    pending_requests = count_pending_requests()
    if pending_requests > 0:
        st.warning(f"🔔 Tienes {pending_requests} solicitudes pendientes de dispositivos.")
    else: 
        st.write("No tienes ninguna")
    st.divider()
    
    # Conectar y cargar las solicitudes de dispositivos
    conn = sqlite3.connect('DatabasesDB/device_requests.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM device_requests WHERE status = "En Espera"')
    requests = cursor.fetchall()

    if requests:
        # Convertir las solicitudes en un DataFrame para su manipulación
        requests_df = pd.DataFrame(requests, columns=["request_id", "device_name", "device_type", "department", "status", "request_date", "justification", "quantity"])

        # Contar el número de solicitudes por departamento
        department_counts = requests_df['department'].value_counts().reset_index()
        department_counts.columns = ['department', 'number_of_requests']

        # Crear el gráfico de barras con Plotly
        fig = px.bar(department_counts, 
                     x='department', 
                     y='number_of_requests', 
                     title='Número de Solicitudes por Departamento',
                     labels={'department': 'Departamento', 'number_of_requests': 'Número de Solicitudes'},
                     color='department',  # Agrega colores según el departamento
                     color_discrete_sequence=px.colors.qualitative.Set2)

        # Ajustar el tamaño del gráfico (más pequeño)
        fig.update_layout(
            width=600,  # Ancho del gráfico
            height=400,  # Alto del gráfico
            title={
                'text': '📊 Número de Solicitudes por Departamento',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center',  # Anclar en el centro
                'yanchor': 'top'  # Anclar en la parte superior
            },
            title_font=dict(size=14, color='darkblue', family='Arial'),
            xaxis_title_font=dict(size=12, color='darkslategray'),
            yaxis_title_font=dict(size=12, color='darkslategray'),
            xaxis_tickangle=-45,  # Rotar etiquetas de x para mejor visibilidad
            template='plotly_white'  # Estilo más limpio
        )

        # Mostrar el gráfico de barras interactivo
        st.plotly_chart(fig)

        # Mostrar la tabla con las solicitudes
        st.subheader("💼 Solicitudes Pendientes")

        # Crear una lista de solicitudes pendientes para mostrarlas
        if 'processed_requests' not in st.session_state:
            st.session_state.processed_requests = []

        # Mostrar la tabla de solicitudes y los botones de acción
        for index, row in requests_df.iterrows():
            request_id = row['request_id']
            device_name = row['device_name']
            device_type = row['device_type']
            department = row['department']
            request_date = row['request_date']
            justification = row['justification']
            quantity = row['quantity']
            
            # Mostrar los datos de la solicitud
            st.markdown(f"### Dispositivo: {device_name}")
            st.write(f"**Tipo:** {device_type}")
            st.write(f"**Departamento:** {department}")
            st.write(f"**Fecha de Solicitud:** {request_date}")
            st.write(f"**Justificación:** {justification}")
            st.write(f"**Cantidad Solicitada:** {quantity}")

            # Verificar si la solicitud ya ha sido procesada
            if request_id not in st.session_state.processed_requests:
                # Botón "Ya Administrada"
                button_key = f"administered_{request_id}_{index}"
                if st.button(f"✅ Ya Administrada: {device_name}", key=button_key):
                    try:
                        # Actualizar el estado de la solicitud a "Administrada"
                        cursor.execute('UPDATE device_requests SET status = "Administrada" WHERE request_id = ?', (request_id,))
                        conn.commit()

                        # Marcar como administrada en el estado de sesión
                        st.session_state.processed_requests.append(request_id)

                        # Desplegar un mensaje de éxito
                        st.success(f"✅ La solicitud de '{device_name}' ha sido marcada como 'Administrada'.")
                    except Exception as e:
                        st.error(f"❌ Error al administrar la solicitud: {e}", icon="❌")
            else:
                st.markdown(f"**✅ Ya Administrada**: La solicitud de '{device_name}' ya ha sido procesada.")
            st.write("---")

    else:
        st.write("🔴 No hay solicitudes pendientes.")