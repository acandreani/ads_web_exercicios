from flask import Flask, render_template, request, json
app = Flask(__name__)

import sqlite3


@app.route("/ws/cadastro",methods=["POST"])
def ws_score():
	if request.method == "POST":
		print("teste- dado recebido")
		cadastro=request.get_json()
		print(cadastro)
		
		
		conn = sqlite3.connect('game.db')
		cursor = conn.cursor()
		# criando a tabela (schema)
		cursor.execute("""
		CREATE TABLE clientes (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				nome TEXT NOT NULL,
				idade INTEGER,
				cpf     VARCHAR(11) NOT NULL,
				email TEXT NOT NULL,
				fone TEXT,
				cidade TEXT,
				uf VARCHAR(2) NOT NULL,
				criado_em DATE NOT NULL
		);
		""")
		
		
		
		return json.dumps({"status":"ok"})



@app.route("/",methods=["GET"])
def home():
	if request.method == "GET":
		return render_template("home.html")

if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)
	