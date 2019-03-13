from flask import Flask, render_template, request
app = Flask(__name__)

bd={"usuario":"alexandre.c.andreani@gmail.com","senha":"12345"}

def usuario_existe(usuario):
	return  usuario == bd["usuario"]

def verifica_senha(usuario,senha):
	return usuario == bd["usuario"] and senha==bd["senha"]
	
	

@app.route("/")
def student():
	return render_template("aluno.html")
	

@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/loginresult",methods=['POST'])
def login_result():

	if request.method == "POST":
		result = request.form
		print("result")
		print(result)
		
		if usuario_existe(result["email"]):
		
			if verifica_senha(result["email"],result["senha"]):
				return render_template("loginresult.html")
			else:
				return render_template("loginresult_senha_incorreta.html")
		else:
			
			return render_template("loginresult_usuario_incorreto.html")
			
		
	
@app.route("/result",methods=['POST'])
def result():
	if request.method == "POST":
		result = request.form
		print("result")
		print(result)
		return render_template("result.html")
	
		
	
if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)
	