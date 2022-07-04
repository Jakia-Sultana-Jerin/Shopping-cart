from calendar import month_name
import flask
from  flask import Flask, redirect,render_template,request
import sqlite3
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def register():
   if request.method == 'GET':
    return render_template('register.html')
   else:
   
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        connection=sqlite3.connect('register.db')
        cursor=connection.cursor()
        cursor.execute('INSERT INTO register(Username,password,Email) VALUES(?,?,?)', (username, password, email))
        connection.commit()
        connection.close()
         
        return "You have successfully registered !"
    
   
   