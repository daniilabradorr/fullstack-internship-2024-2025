import streamlit as st
import sqlite3
from funciones_comunes import authenticate_user

# Configuración de la página
st.set_page_config(
    page_title="Monitoreo de los Dispositivos",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
        'About': 'https://www.example.com/about'
    }
)

# Sidebar - Solo se muestra el título y el icono antes de autenticarse
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Monitoreo de Dispositivos</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>📱</h1>", unsafe_allow_html=True)  # Emoji grande

# Función para la autenticación de usuarios
def user_authentication():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if not st.session_state['authenticated']:
        with st.form(key='auth_form'):
            st.title("Autenticación de Usuarios")
            username = st.text_input("Nombre de usuario")
            password = st.text_input("Contraseña", type="password")
            submit_button = st.form_submit_button(label='Iniciar sesión')
            st.info("🔹 **Usuario de Escritura y Admin**: `admin` \n🔹 **Contraseña**: `admin123`")
            st.info("🔹 **Usuario de lectura**: `tecnico1` \n🔹 **Contraseña**: `tecnico123`")

        if submit_button:
            role = authenticate_user(username, password)
            if role:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username
                st.session_state['role'] = role
                st.success(f"Bienvenido de nuevo, {username}!")
            else:
                st.error("Nombre de usuario o contraseña incorrectos.")
    else:
        st.success(f"Ya estás autenticado como {st.session_state['username']}")

# Verificar si el usuario está autenticado antes de mostrar las páginas
if 'authenticated' in st.session_state and st.session_state['authenticated']:
    # Importar después de autenticación para evitar detección automática de Streamlit
    from modulos import page1, page2, page3, page4, page5, page6, page7, page8

    user = st.session_state['username']
    role = st.session_state['role']

    # Definir las páginas según el rol del usuario
    navigation_config = {
        "Home": [st.Page(page8.page8, title="Ayuda", icon="🌠")],
        "Data": [st.Page(page1.page1, title="Tablas", icon="💻")],
        "Plots & Visualizations": [
            st.Page(page3.page3, title="Dispositivos x Departamento", icon="🏭"),
            st.Page(page4.page4, title="Dispositivos x Puertos", icon="📟"),
            st.Page(page5.page5, title="Dispositivos x Estado", icon="🧍‍♂️"),
        ]
    }

    if role == 'administrador':
        navigation_config["Data"].extend([
            st.Page(page2.page2, title="Insertar Dispositivos", icon="💾"),
            st.Page(page6.page6, title="Petición Dispositivos", icon="🥇"),
            st.Page(page7.page7, title="Estado Petición", icon="🗽")
        ])
    elif role == 'tecnico':
        navigation_config["Data"].append(st.Page(page6.page6, title="Petición Dispositivos", icon="🥇"))

    # Ejecutar navegación
    pg = st.navigation(navigation_config)
    pg.run()
else:
    user_authentication()
