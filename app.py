from flask import Flask, render_template, request, redirect, url_for
from logic import audio_converter, audio_to_text, text_transformers_resume, print_screen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    if 'video_file' not in request.files:
        return redirect(url_for('index'))
    
    video_file = request.files['video_file']
    if video_file.filename == '':
        return redirect(url_for('index'))
    
    # Guardar el video en la carpeta 'video'
    video_path = f"./video/{video_file.filename}"
    video_file.save(video_path)
    
    # Ejecución del pipeline
    audio_path = audio_converter(video_path)
    transcription_path = audio_to_text(audio_path)
    summary_path = text_transformers_resume(transcription_path)
    
    # Imprimir el resultado en pantalla
    output = print_screen(summary_path)
    
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
