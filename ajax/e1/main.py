from flask import Flask, render_template, request
app = Flask(__name__)

def converte_romanos(numero):
	#coloque seu codigo aqui, exemplo 
	romanos="MCM"	
	return romanos
	
@app.route("/",methods=["GET","POST"])
def home():
	if request.method == "POST":
		response = request.form
		print("response")
		print(response)
		numero=response["valor"]
		romano=converte_romanos(numero)
					
		return romano	
	elif request.method == "GET":
		return render_template("recebe_numero.html")

if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)
	