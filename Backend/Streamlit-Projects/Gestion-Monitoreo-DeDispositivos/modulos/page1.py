import streamlit as st
from funciones_comunes import connect_and_load_data, style_dataframe

def page1():
    st.title("Tablas Monitoreo")
    st.markdown("Monitoreo de dispositivos")
    
    # Cargar los datos más recientes
    df = connect_and_load_data()
    
    if df is not None:
        styled_df = style_dataframe(df)
        st.dataframe(styled_df, hide_index=True,
                     column_config={
                         "id": "ID_Dispositivos",
                         "port": "Puerto_Dispositivo",
                         "department": "Departamento"
                     })
        st.divider()
        st.markdown("### Consulta a la Base de Datos")
        st.code(''' 
query = 'SELECT * FROM devices'
df = pd.read_sql(query, conn)
        ''', language='python')