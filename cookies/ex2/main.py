from flask import Flask, render_template, request, session,redirect, url_for, escape, request, make_response 
app = Flask(__name__)

# configure a chave secreta
app.secret_key = "segredo"

@app.route('/')
def index():
    return render_template("index.html")
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.





if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)

