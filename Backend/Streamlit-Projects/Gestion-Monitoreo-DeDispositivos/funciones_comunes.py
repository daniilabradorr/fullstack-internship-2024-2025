import streamlit as st
import sqlite3
import pandas as pd
import datetime

# Función para autenticar usuarios
def authenticate_user(username, password):
    try:
        conn = sqlite3.connect('DatabasesDB/users.db', check_same_thread=False)  # Evita problemas con múltiples hilos
        cursor = conn.cursor()
        cursor.execute('SELECT role FROM users WHERE username = ? AND password = ?', (username, password))
        result = cursor.fetchone()
        conn.close()  # Cerrar la conexión después de cada uso
        return result[0] if result else None
    except sqlite3.Error as e:
        st.error(f"Error al autenticar usuario: {e}")
        return None

# Función para conectar y cargar datos
def connect_and_load_data():
    try:
        conn = sqlite3.connect('DatabasesDB/devices_large.db', check_same_thread=False)  # Evita problemas de hilos
        query = 'SELECT * FROM devices'
        df = pd.read_sql(query, conn)
        conn.close()  # Cerrar la conexión después de cada uso
        return df
    except Exception as e:
        st.error(f"Error al conectar a la base de datos o cargar datos: {e}")
        return None

# Función para aplicar estilos al DataFrame
def style_dataframe(df):
    def color_departments(val):
        colors = {
            'Producción': 'lightblue',
            'Calidad': 'lightgreen',
            'Logística': 'lightcoral',
            'Mantenimiento': 'lightyellow'
        }
        return f'background-color: {colors.get(val, "white")}'  # Si no coincide, usa blanco

    return df.style.map(color_departments, subset=['department'])

# Función para insertar un nuevo dispositivo en la base de datos
def insert_device(nombre, tipo, departamento, puerto, estatus):
    try:
        conn = sqlite3.connect('DatabasesDB/devices_large.db', check_same_thread=False)
        cursor = conn.cursor()

        # Generar ID automáticamente
        cursor.execute('SELECT MAX(id) FROM devices')
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id else 1

        # Obtener la fecha y hora actuales
        fecha_ultima_actividad = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insertar el nuevo dispositivo
        cursor.execute('INSERT INTO devices (id, device_name, device_type, department, port, last_activity, status) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                       (new_id, nombre, tipo, departamento, puerto, fecha_ultima_actividad, estatus))
        conn.commit()
        conn.close()

        return True, f"Dispositivo {nombre} insertado exitosamente!"
    except sqlite3.Error as e:
        return False, f"Error en la inserción: {e}"


# Función para conectar a la base de datos de peticiones
def connect_device_requests_db():
    try:
        conn = sqlite3.connect('DatabasesDB/device_requests.db', check_same_thread=False)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error al conectar con la base de datos de peticiones: {e}")
        return None

# Función para contar solicitudes pendientes
def count_pending_requests():
    try:
        conn = sqlite3.connect('DatabasesDB/device_requests.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM device_requests WHERE status = 'En Espera'")
        pending_count = cursor.fetchone()[0]
        conn.close()
        return pending_count
    except sqlite3.Error as e:
        st.error(f"Error al obtener el número de solicitudes pendientes: {e}")
        return 0
