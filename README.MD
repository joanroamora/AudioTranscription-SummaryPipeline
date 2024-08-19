# AudioTranscription-SummaryPipeline
## English 🇺🇸
###  1. Overview
AudioTranscription-SummaryPipeline is a Python-based project that processes YouTube videos by extracting their audio, converting the audio to mono PCM format, transcribing the speech using Vosk, and generating a summarized text suitable for social media sharing. The project is built with Flask for web-based interaction and integrates various libraries such as MoviePy, PyDub, and Transformers for efficient processing.

###  2. Prerequisites
Before you start, make sure you have the following installed:

Python 3.10 or higher
pip (Python package manager)
ffmpeg: This is required for audio processing. Install it by running:
sudo apt-get install ffmpeg
		
Vosk Model: You need to download the Spanish language model for Vosk. Download it from here and extract it into the models/ directory of the project.
###  3. Installation
Clone the repository and install the required Python packages:

git clone https://github.com/yourusername/AudioTranscription-SummaryPipeline.git
cd AudioTranscription-SummaryPipeline
pip install -r requirements.txt
		
###  4. Project Structure

AudioTranscription-SummaryPipeline/
├── app.py
├── logic.py
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   └── index.html
├── audio/
├── transcriptions/
├── resumes/
└── models/
    └── vosk-model-es-0.42/ 
    ```

### 5. Usage
Run the Flask Application:
Start the Flask development server by running:

python3 app.py
		
The application will be accessible at <http://127.0.0.1:5000>.

Upload a Video:
On the web interface, upload a YouTube video file. The pipeline will:

Extract the audio
Convert it to mono PCM format
Transcribe the speech
Generate a summarized text
View the Output:
The summarized text will be displayed on the web interface.

### 6. Contributing
Feel free to fork this repository, make your changes, and submit a pull request. We welcome contributions that enhance functionality or improve the documentation.

### 7. License
This project is licensed under the MIT License. See the LICENSE file for details.

## Español 🇨🇴
### 1. Resumen
AudioTranscription-SummaryPipeline es un proyecto en Python que procesa videos de YouTube extrayendo su audio, convirtiéndolo a formato PCM mono, transcribiendo el discurso usando Vosk, y generando un texto resumido apto para compartir en redes sociales. El proyecto está construido con Flask para la interacción web e integra varias librerías como MoviePy, PyDub, y Transformers para un procesamiento eficiente.

### 2. Requisitos Previos
Antes de comenzar, asegúrate de tener instalados los siguientes elementos:

Python 3.10 o superior
pip (administrador de paquetes de Python)
ffmpeg: Esto es necesario para el procesamiento de audio. Instálalo ejecutando:
sudo apt-get install ffmpeg
		
Modelo Vosk: Necesitas descargar el modelo de idioma español para Vosk. Descárgalo desde aquí y extráelo en el directorio models/ del proyecto.
### 3. Instalación
Clona el repositorio e instala los paquetes de Python necesarios:

git clone https://github.com/tuusuario/AudioTranscription-SummaryPipeline.git
cd AudioTranscription-SummaryPipeline
pip install -r requirements.txt
		
### 4. Estructura del Proyecto
AudioTranscription-SummaryPipeline/
├── app.py
├── logic.py
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   └── index.html
├── audio/
├── transcriptions/
├── resumes/
└── models/
    └── vosk-model-es-0.42/
		
### 5. Uso
Ejecutar la Aplicación Flask:
Inicia el servidor de desarrollo Flask ejecutando:

python3 app.py
		
La aplicación será accesible en <http://127.0.0.1:5000>.

Subir un Video:
En la interfaz web, sube un archivo de video de YouTube. El pipeline realizará:

La extracción del audio
La conversión a formato PCM mono
La transcripción del discurso
La generación de un texto resumido
Ver el Resultado:
El texto resumido se mostrará en la interfaz web.

### 6. Contribuir
Siéntete libre de bifurcar este repositorio, hacer tus cambios y enviar una solicitud de extracción. Agradecemos las contribuciones que mejoren la funcionalidad o la documentación.

### 7. Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.