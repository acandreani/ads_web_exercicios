from flask import Flask, render_template, request, session,redirect, url_for, escape, request, make_response 
app = Flask(__name__)

# configure a chave secreta
app.secret_key = "segredo"

@app.route('/')
def index():
    c = request.cookies.get('cookieexemplo')
    return "cookieexemplo:"+str(c)
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

@app.route('/setcookie')
def setcookie():
    resp = make_response()
    resp.set_cookie('cookieexemplo', 'oi')
    return resp



if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)

