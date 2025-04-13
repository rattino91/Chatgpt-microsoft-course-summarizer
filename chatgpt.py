from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Database dei corsi
CORSI_MICROSOFT = {
    "AZ-900": {
        "nome": "AZ-900: Microsoft Azure Fundamentals",
        "url": "https://learn.microsoft.com/it-it/certifications/exams/az-900/"
    },
    "AI-900": {
        "nome": "AI-900: Microsoft Azure AI Fundamentals",
        "url": "https://learn.microsoft.com/it-it/certifications/exams/ai-900/"
    }
}

TIPI_RIASSUNTO = [
    {"id": "bullet", "nome": "Punti elenco"},
    {"id": "diagram", "nome": "Diagrammi"},
    {"id": "essential", "nome": "Sommario essenziale"},
    {"id": "detailed", "nome": "Sommario ampio"},
    {"id": "cheatsheet", "nome": "Cheat Sheet"}
]

@app.route('/')
def home():
    return render_template('index.html', corsi=CORSI_MICROSOFT, tipi_riassunto=TIPI_RIASSUNTO)

@app.route('/genera_riassunto', methods=['POST'])
def genera_riassunto():
    data = request.json
    corso_id = data.get('corso_id')
    tipo_riassunto = data.get('tipo_riassunto')
    
    if not corso_id or not tipo_riassunto:
        return jsonify({"errore": "Seleziona sia il corso che il tipo di riassunto"}), 400
    
    corso = CORSI_MICROSOFT.get(corso_id)
    if not corso:
        return jsonify({"errore": "Corso non trovato"}), 404
    
    prompt = f"Crea un riassunto del corso '{corso['nome']}' ({corso['url']}) in formato {tipo_riassunto}."
    
    riassunto = chiamata_api_openai(prompt)
    
    return jsonify({
        "prompt": prompt,
        "riassunto": riassunto,
        "nome_file": f"Riassunto_{corso_id}_{tipo_riassunto}.txt"
    })

def chiamata_api_openai(prompt):
    try:
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        
        if not OPENAI_API_KEY:
            raise ValueError("API key di OpenAI non configurata")

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 2000
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        print(f"Errore API OpenAI: {str(e)}")
        return f"Errore durante la generazione: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)