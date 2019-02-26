from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def student():
	return render_template("student.html")
	
@app.route("/result",methods=['POST'])
def result():
	if request.method == "POST":
		result = request.form
		print("result")
		print(result)
		return render_template("result.html",result)
	
		
	
if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)
	