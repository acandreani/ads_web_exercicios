from flask import Flask, render_template, request, session,redirect, url_for, escape, request, make_response 
app = Flask(__name__)


import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users


@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		insertUser(username, password)
		users = retrieveUsers()
		return render_template('index.html', users=users)
	else:
		return render_template('index.html')







if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)

