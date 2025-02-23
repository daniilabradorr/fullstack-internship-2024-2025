import streamlit as st
import sqlite3
import datetime
from funciones_comunes import connect_device_requests_db

def page6():
    st.title("Petición de Nuevos Dispositivos")
    st.markdown("Formulario para la petición de nuevos dispositivos")

    with st.form(key='newDevice_form'):
        nombreDispositivo = st.text_input("Nombre del dispositivo")
        tipoDispositivo = st.selectbox("Selecciona el tipo de dispositivo", ["Scanner", "Tablet", "Camera", "Printer", "Otro Distinto"])
        DepartamentoQueLoRequiere = st.selectbox("Selecciona el departamento que lo requiere", ["Producción", "Calidad", "Logística", "Mantenimiento"])
        cantidad = st.number_input("Cantidad deseada")
        justificacion = st.text_area("Justificación para la solicitud", "", help="Escribe una breve justificación sobre la solicitud.")
        submit_button = st.form_submit_button(label="Enviar solicitud")

        if submit_button:
            if not nombreDispositivo or not tipoDispositivo or not DepartamentoQueLoRequiere or cantidad <= 0:
                st.error("Por favor, completa todos los campos antes de proceder.")
            else:
                conn = connect_device_requests_db()
                if conn:
                    try:
                        cursor = conn.cursor()
                        fecha_solicitud = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        cursor.execute('''
                            INSERT INTO device_requests (device_name, device_type, department, status, request_date, justification, quantity)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', (nombreDispositivo, tipoDispositivo, DepartamentoQueLoRequiere, "En Espera", fecha_solicitud, justificacion, cantidad))

                        conn.commit()
                        conn.close()
                        st.success(f"Solicitud de '{nombreDispositivo}' enviada exitosamente. Estado: 'En Espera'.")

                    except sqlite3.Error as e:
                        st.error(f"Hubo un problema al procesar la solicitud: {e}")