import streamlit as st
import datetime
from funciones_comunes import connect_and_load_data, insert_device

def page2():
    st.title("Inserción de nuevos dispositivos")
    st.markdown("Creación de nuevos dispositivos")

    # Listas predefinidas
    departamentos = ["Producción", "Calidad", "Logística", "Mantenimiento"]
    puertos = [i for i in range(8001, 8100)]
    devices_types = ["Scanner", "Tablet", "Camera", "Printer", "Otro Distinto"]
    devices_status = ['en uso', 'en desuso', 'en reparación']

    # Resetear mensajes de sesión
    if 'insert_success' in st.session_state:
        del st.session_state['insert_success']
    if 'last_insert' in st.session_state:
        del st.session_state['last_insert']

    with st.form(key='insert_form'):
        nombre_dispositivo = st.text_input("Nombre del dispositivo", "Device99")
        tipoDel_dispositivo = st.selectbox("Selecciona el tipo de dispositivo nuevo a insertar", devices_types)
        PuertoDel_dispositivo = st.selectbox("Selecciona el puerto del dispositivo", puertos)
        DepartamentoDel_dispositivo = st.selectbox("Selecciona el departamento del dispositivo", departamentos)
        EstatusDel_dispositivo = st.selectbox("Selecciona el estado del Dispositivo", devices_status)
        submit_button = st.form_submit_button(label='Insertar dispositivo')

        if submit_button:
            if not nombre_dispositivo or not tipoDel_dispositivo or not DepartamentoDel_dispositivo or not PuertoDel_dispositivo or not EstatusDel_dispositivo:
                st.error("Por favor, completa todos los campos antes de proceder.")
            else:
                st.markdown("### Datos a insertar")
                st.table({
                    "Nombre del dispositivo": [nombre_dispositivo],
                    "Tipo de dispositivo": [tipoDel_dispositivo],
                    "Departamento": [DepartamentoDel_dispositivo],
                    "Puerto": [PuertoDel_dispositivo]
                })

                # Intentar insertar el dispositivo usando la función centralizada
                success, message = insert_device(nombre_dispositivo, tipoDel_dispositivo, DepartamentoDel_dispositivo, PuertoDel_dispositivo, EstatusDel_dispositivo)
                
                if success:
                    st.session_state['insert_success'] = True
                    st.session_state['last_insert'] = nombre_dispositivo
                    st.success(message, icon="✅")
                else:
                    st.session_state['insert_success'] = False
                    st.error(message, icon="❌")

    # Mostrar mensaje final basado en session_state
    if 'insert_success' in st.session_state:
        if st.session_state['insert_success']:
            st.success(f"Dispositivo {st.session_state['last_insert']} insertado exitosamente!")
        else:
            st.error("Hubo un problema al intentar insertar el dispositivo.")
