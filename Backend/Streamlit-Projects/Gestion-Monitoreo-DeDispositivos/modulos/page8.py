import streamlit as st
from PIL import Image

img_path = "static/img/logo.jpg"

def page8():
    # Ajustar el tamaño de la imagen en la cabecera
    try:
        image = Image.open(img_path)
        st.image(image, width=300)
    except Exception as e:
        st.error(f"No se pudo cargar la imagen: {e}")  # Ajusta el tamaño a 300px de ancho, puedes cambiar el valor si quieres un tamaño diferente
    
    # Título de la página
    st.title("Descripción USO App")
    
    # Descripción general de la APP
    st.markdown("""
    ### Bienvenido a la aplicación para el monitoreo y gestión de dispositivos.
    
    Esta aplicación tiene como objetivo principal facilitar el seguimiento y la administración de los dispositivos de la empresa, asegurando una gestión eficiente de los recursos tecnológicos y permitiendo a los usuarios realizar tareas específicas, como:
    
    - **Monitoreo de Dispositivos**: Visualiza todos los dispositivos disponibles, su estado y su ubicación actual.
    - **Inserción de Nuevos Dispositivos**: Agrega nuevos dispositivos a la base de datos para su gestión.
    - **Gráficos de Análisis**: Consulta los gráficos interactivos sobre el número de dispositivos por departamento o puerto, y otras métricas relevantes.
    - **Mantenimiento y Reportes**: Permite generar informes de la actividad y estado de los dispositivos, además de gestionar tareas de mantenimiento si es necesario.

    ### Funcionalidades principales
    - **Monitoreo en tiempo real**: Los dispositivos registrados pueden ser visualizados en tiempo real, con filtros por tipo, estado, y departamento.
    - **Interfaz fácil de usar**: Se proporciona una interfaz amigable para que el usuario pueda agregar, editar o eliminar dispositivos sin dificultad.
    - **Generación de informes y visualizaciones**: La aplicación genera gráficos interactivos y reportes que permiten tomar decisiones informadas sobre el uso y mantenimiento de los dispositivos.

    ### ¿Cómo utilizar la APP?
    1. **Inicio de sesión**: Inicia sesión con tus credenciales para tener acceso a la interfaz de monitoreo.
    2. **Agregar un dispositivo**: Dirígete a la sección "Inserción de nuevos dispositivos" y completa los campos del formulario para registrar un nuevo dispositivo.
    3. **Consultar información**: En la sección "Monitoreo de dispositivos", podrás ver todos los dispositivos registrados y sus detalles. 
    4. **Ver Gráficos**: Usa las secciones de "Gráficos de Dispositivos por Departamento" o "Dispositivos por Puerto" para consultar los datos de manera visual.

    Si necesitas más ayuda, puedes consultar la sección de **Soporte** o enviar un correo a nuestro equipo.
    """)

    # Información adicional o preguntas frecuentes (FAQ)
    st.markdown("""
    ### Preguntas Frecuentes (FAQ)
    
    **1. ¿Cómo puedo agregar un dispositivo?**  
    Simplemente dirígete a la sección de "Inserción de nuevos dispositivos" y completa el formulario con los datos correspondientes (nombre, tipo, departamento, puerto y estado).

    **2. ¿Qué hago si un dispositivo no aparece en el monitoreo?**  
    Asegúrate de que el dispositivo esté correctamente registrado en la base de datos. Si el problema persiste, contáctanos a través de nuestro soporte técnico.

    **3. ¿Cómo puedo generar un informe sobre el estado de los dispositivos?**  
    Dirígete a la sección de "Generación de Reportes" para obtener un informe detallado sobre los dispositivos activos y su estado.

    **4. ¿Cómo puedo mejorar la visibilidad de los dispositivos?**  
    Utiliza los filtros y gráficos interactivos para obtener información detallada sobre los dispositivos por tipo, estado o ubicación.
    """)

    # Enlace a soporte técnico
    st.markdown("Para más ayuda, contacta a nuestro equipo de soporte técnico en [soporte@empresa.com](mailto:soporte@empresa.com)")