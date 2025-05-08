from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir consultas desde GitHub Pages

# Cargar el modelo de resumen
resumidor = pipeline("summarization", model="facebook/mbart-large-50")

@app.route('/resumir', methods=['POST'])
def resumir_texto():
    datos = request.get_json()
    texto = datos.get("texto", "")

    if not texto:
        return jsonify({"error": "Texto vacío"}), 400

    resumen = resumidor(texto, max_length=150, min_length=50, do_sample=False)
    return jsonify({"resumen": resumen[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
