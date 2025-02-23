📡 Sistema de Gestión y Monitoreo de Dispositivos
🚨 ⚠️ IMPORTANTE: Este proyecto es una versión simplificada y creada desde cero con datos irreales y ficticios. No representa información real ni confidencial de ninguna empresa.

🏢 Sobre el Proyecto
Este programa ha sido desarrollado como parte de mis prácticas como Full Stack Developer en la empresa donde he trabajado. Dado que no puedo compartir el código original por razones de confidencialidad, esta es una versión simplificada y "barata" con datos ficticios, pero manteniendo la esencia del sistema que diseñé.

El objetivo del proyecto es gestionar dispositivos en una empresa, permitiendo a los empleados solicitar nuevos dispositivos y a los administradores gestionar su asignación.

🚀 Características
✅ Autenticación de usuarios con roles (admin, usuario).
✅ Gestión de dispositivos en la base de datos.
✅ Registro y visualización de solicitudes de nuevos dispositivos.
✅ Persistencia de datos con SQLite.
✅ Interfaz en Streamlit para fácil interacción.

📂 Estructura del Proyecto
Copiar
Editar
📦 Proyecto
 ┣ 📂 DatabasesDB
 ┃ ┣ 📄 users.db
 ┃ ┣ 📄 devices_large.db
 ┃ ┗ 📄 device_requests.db
 ┣ 📂 pages
 ┃ ┣ 📄 page1.py
 ┃ ┗ 📄 ...
 ┣ 📄 funciones_comunes.py
 ┣ 📄 app.py
 ┣ 📄 README.md
 ┗ 📄 .gitignore

🛠 Instalación
1️⃣ Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/tuusuario/proyecto.git
cd proyecto

2️⃣ Crear un entorno virtual y activarlo
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3️⃣ Instalar dependencias
bash
Copiar
Editar
pip install -r requirements.txt

4️⃣ Ejecutar la aplicación
bash
Copiar
Editar
streamlit run app.py

📜 Notas
⚠️ Datos Ficticios: Todos los datos usados en la base de datos son generados aleatoriamente y no pertenecen a ninguna empresa real.
⚠️ Proyecto Basado en mi Experiencia: Esta es una versión simplificada del sistema que desarrollé en la empresa donde hice mis prácticas como Full Stack Developer.