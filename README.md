# To-Do App con Django

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Esta es una aplicación web de lista de tareas (To-Do list) construida con el framework de Python, Django. El proyecto fue desarrollado como parte de mi ruta de aprendizaje para convertirme en desarrollador Full-Stack, enfocándome en dominar los conceptos fundamentales del desarrollo backend y la interacción con el frontend.

La aplicación permite a los usuarios gestionar sus tareas diarias a través de una interfaz web simple e intuitiva.

## 🚀 Características Principales

*   **CRUD Completo de Tareas:** Los usuarios pueden **C**rear, **L**eer, **A**ctualizar y **B**orrar tareas.
*   **Creación de Tareas:** Formulario para añadir nuevas tareas a la lista.
*   **Listado de Tareas:** Visualización clara de todas las tareas pendientes y completadas.
*   **Actualización de Tareas:** Funcionalidad para editar el título de una tarea existente.
*   **Borrado Seguro:** Sistema de borrado con página de confirmación para evitar eliminaciones accidentales.
*   **Marcar como Completada:** Funcionalidad interactiva para marcar o desmarcar una tarea como completada, utilizando una recarga de página para reflejar el cambio de estado de forma simple.

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python, Django.
*   **Base de Datos:** PostgreSQL.
*   **Frontend:** HTML5, CSS3.

## ⚙️ Instalación y Puesta en Marcha

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

### Prerrequisitos
*   Tener instalado Python 3.x
*   Tener instalado PostgreSQL y un servidor en funcionamiento.
*   Tener `pip` (el gestor de paquetes de Python).

### Pasos
1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/[Tu-Nombre-de-Usuario-GitHub]/[nombre-de-tu-repositorio].git
    cd [nombre-de-tu-repositorio]
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    (Si tienes un archivo `requirements.txt`, este es el comando. Si no, es una buena práctica crearlo con `pip freeze > requirements.txt`)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la base de datos:**
    *   Crea una base de datos en PostgreSQL para el proyecto.
    *   Crea un archivo `.env` en la raíz del proyecto y configura tus variables de entorno, basándote en el archivo `.env.example` (si lo tienes). Deberás incluir:
        ```
        SECRET_KEY='tu_secret_key_aqui'
        DB_NAME='nombre_de_tu_bd'
        DB_USER='usuario_de_tu_bd'
        DB_PASSWORD='password_de_tu_bd'
        DB_HOST='localhost'
        DB_PORT='5432'
        ```

5.  **Aplica las migraciones:**
    ```bash
    python manage.py migrate
    ```

6.  **Crea un superusuario (opcional):**
    Para acceder al panel de administración de Django.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    
    ¡La aplicación estará disponible en `http://127.0.0.1:8000/`! (O en la URL de tu app, por ejemplo `http://127.0.0.1:8000/tareas/`).

## 🧠 Conceptos de Django Aplicados

Este proyecto me permitió aplicar y solidificar mi entendimiento de:
*   La arquitectura **Modelo-Vista-Plantilla (MVT)**.
*   El **ORM de Django** para interactuar con la base de datos de forma segura y eficiente.
*   El sistema de **migraciones** para gestionar la evolución del esquema de la base de datos.
*   **Formularios de Django (`ModelForm`)** para la validación y gestión de la entrada de datos del usuario.
*   El **sistema de ruteo de URLs**, incluyendo URLs dinámicas con parámetros.
*   Vistas basadas en funciones que manejan lógica condicional para peticiones **GET** y **POST**.
*   El **lenguaje de plantillas de Django (DTL)**, incluyendo bucles, condicionales y la etiqueta `{% url %}`.
*   La protección de seguridad integrada de Django, como **CSRF tokens**.

---
Dermis Hamel Zabala Batista