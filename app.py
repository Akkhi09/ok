from flask import Flask, request, jsonify, render_template_string
import sqlite3 as sql

app = Flask(__name__)

def connect():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row # Retornar resultados como dicionário.
    return conn
  
connect()

# Criar tabela se não existir
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Celulares(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        versao TEXT NOT NULL,
        so TEXT NOT NULL,
        interface TEXT NOT NULL,
        processador TEXT NOT NULL,
        raM TEXT NOT NULL,
        armazenamento TEXT NOT NULL,
        expansivel TEXT NOT NULL,
        gpu TEXT NOT NULL,
        tela TEXT NOT NULL,
        tamanho REAL NOT NULL,
        resolucao TEXT NOT NULL,
        taxa_update TEXT NOT NULL,
        cam_frontal TEXT NOT NULL,
        cam_traseira TEXT NOT NULL,
        video TEXT NOT NULL,
        cap_bateria TEXT NOT NULL,
        carregamento TEXT NOT NULL,
        _5g BOOLEAN NOT NULL,
        wifi TEXT NOT NULL,
        bluetooth TEXT NOT NULL,
        nfc BOOLEAN NOT NULL,
        material TEXT NOT NULL,
        peso REAL NOT NULL,
        resistencia TEXT NOT NULL,
        preco REAL NOT NULL,
        moeda TEXT NOT NULL,
        disponivel BOOLEAN NOT NULL,
        lancamento TEXT NOT NULL,
        suporte_caneta BOOLEAN NOT NULL,
        dual_sim BOOLEAN NOT NULL
        )''')
    conn.commit()
    conn.close()
create_table()

#criando todas as endpoints/rotas

@app.route('/')
def index():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Celulares')
    celulares = cursor.fetchall()
    html = '''<h2>Lista de Celulares disponiveis</h2>
                <ul>
                    {% for c in celulares %}
                        <li><strong>{{ c["marca"] }}</strong> 
                        —{{ c["modelo"] }}</li>
                    {% endfor %}
                </ul>'''
    return render_template_string(html, celulares=celulares)

@app.route('/celulares', methods=['GET'])
def listar_celulares():
    conn= connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Celulares')
    celulares = cursor.fetchall()
    conn.close()
    if celulares:
        return jsonify([dict(c) for c in celulares]), 200
    return jsonify({"message": "Nenhum celular encontrado"}), 404

@app.route('/celulares', methods = ['POST'])
def create_celular():
    dados = request.json
    conn = connect()
    cursor= conn.cursor()
    cursor.execute('''INSERT INTO Celulares (marca, modelo, versao, so, interface, processador, ram, armazenamento, expansivel, gpu, tela, tamanho, resolucao, taxa_update, cam_frontal, cam_traseira, video, cap_bateria, carregamento, _5g, wifi, bluetooth, nfc, material, peso, resistencia, preco, moeda, disponivel, lancamento, suporte_caneta, dual_sim) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (dados['marca'],dados['modelo'], dados['versao'], dados['so'], dados['interface'], dados['processador'], dados['ram'], dados['armazenamento'], dados['expansivel'], dados['gpu'],dados['tela'],dados['tamanho'], dados['resolucao'],dados['taxa_update'],dados['cam_frontal'],dados['cam_traseira'],dados['video'],dados['cap_bateria'],dados['carregamento'],dados['_5g'],dados['wifi'],dados['bluetooth'],dados['nfc'],dados['material'],dados['peso'],dados['resistencia'],dados['preco'],dados['moeda'],dados['disponivel'],dados['lancamento'],dados['suporte_caneta'],dados['dual_sim']))
    
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'id': new_id, 'message': 'Celular Criado com sucesso!'}), 201
import os

if __name__ == "__main__":
    # Apenas para testes locais
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))