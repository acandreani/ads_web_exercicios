from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/ws/score",methods=["POST"])
def ws_score():
	if request.method == "POST":
		print("teste- dado recebido")
		print(request.get_json())
		
		return json.dumps({"status":"ok"})



@app.route("/",methods=["GET"])
def home():
	if request.method == "GET":
		return render_template("home.html")

if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)
	