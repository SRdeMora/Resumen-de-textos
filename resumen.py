import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Descargar datos necesarios para tokenización
nltk.download("punkt")

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes externas

def resumir_texto(texto, num_oraciones=3):
    """Genera un resumen abstractivo usando LSA (Latent Semantic Analysis)."""
    parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
    resumenizador = LsaSummarizer()
    
    resumen = resumenizador(parser.document, num_oraciones)
    resumen_texto = " ".join(str(oracion) for oracion in resumen)
    
    return resumen_texto

@app.route('/resumir', methods=['POST'])
def procesar_resumen():
    datos = request.get_json()
    texto = datos.get("texto", "")

    if not texto:
        return jsonify({"error": "Texto vacío"}), 400

    resumen = resumir_texto(texto, num_oraciones=3)
    return jsonify({"resumen": resumen})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto definido por Render o 5000 por defecto
    app.run(host="0.0.0.0", port=port)
