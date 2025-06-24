from flask_cors import CORS
from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS risultati (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cognome TEXT,
            professione TEXT,
            anni_servizio TEXT,
            email TEXT,
            punteggio INTEGER,
            risposte TEXT,
            data_submit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/salva', methods=['POST'])
def salva():
    data = request.get_json(force=True)
    print("Ricevuto:", data)
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO risultati (nome, cognome, professione, anni_servizio, email, punteggio, risposte)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['nome'],
        data['cognome'],
        data['professione'],
        data['anniServizio'],
        data['email'],
        data['punteggio'],
        json.dumps(data['risposte'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Dati salvati con successo!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
