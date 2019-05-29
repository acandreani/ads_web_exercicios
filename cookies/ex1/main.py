from flask import Flask, render_template, request, session,redirect, url_for, escape, request
app = Flask(__name__)

# configure a chave secreta
app.secret_key = "segredo"

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove o username 
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)

