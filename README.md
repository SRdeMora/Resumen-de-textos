<div align="center">
  <h1 align="center">
    📝 Resumidor de Texto con Flask y NLP
  </h1>
  <p align="center">
    <strong>Una aplicación web simple para resumir texto en español, con un backend de Flask para el procesamiento del lenguaje natural y un frontend en HTML/JavaScript.</strong>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

---

## 📜 Descripción del Proyecto

Este es un proyecto de una aplicación web diseñada para **resumir textos largos en español**. La aplicación cuenta con una API de backend construida en **Flask** que contiene la lógica de resumen y una interfaz de usuario web simple, desarrollada con **HTML y JavaScript**, para interactuar con ella.

El usuario puede pegar un texto extenso en la interfaz, y la aplicación devolverá una versión concisa y resumida del mismo.

---

## 🔌 API Endpoint

La aplicación expone un único endpoint para manejar la lógica de resumen.

### Resumir Texto

-   **Endpoint:** `/resumir`
-   **Método:** `POST`
-   **Cuerpo de la Petición (Request Body):**
    ```json
    {
        "texto": "Aquí va el texto largo que se desea resumir..."
    }
    ```
-   **Respuesta Exitosa (200 OK):**
    ```json
    {
        "resumen": "Aquí se devolverá el texto ya resumido."
    }
    ```

---

## 🛠️ Stack Tecnológico

-   **Backend:** Python, Flask
-   **Procesamiento de Lenguaje Natural (NLP):** [Menciona la librería que usas, ej: `spaCy`, `NLTK`, `Transformers`, etc.]
-   **Frontend:** HTML5, JavaScript
-   **Dependencias:** Todas las dependencias están listadas en `requirements.txt`.

---

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1. Prerrequisitos

-   Python 3.x
-   pip (manejador de paquetes de Python)

### 2. Instalación

1.  **Clona el repositorio** (o descarga y descomprime los archivos).

2.  **Navega al directorio del proyecto** en tu terminal:
    ```bash
    cd resumidortexto
    ```

3.  **Crea y activa un entorno virtual** (recomendado):
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

4.  **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Ejecución

1.  **Inicia el servidor de Flask:**
    ```bash
    python resumidor.py
    ```
    El servidor se iniciará en `http://127.0.0.1:10000`.

2.  **Abre la aplicación en tu navegador:**
    Abre el archivo `index.html` directamente en tu navegador web para comenzar a usar la aplicación.
