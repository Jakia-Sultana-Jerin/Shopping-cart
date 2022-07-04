from calendar import month_name
import flask
from  flask import Flask, redirect,render_template,request
import sqlite3
app = Flask(__name__)
@app.route('/')
@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    name=request.form.get('Name')
    phone=request.form.get('password')

    connection=sqlite3.connect('login.db')
    cursor=connection.cursor()
    cursor.execute('INSERT INTO jerin1(Name,password) VALUES(?,?)',(name,phone))
    connection.commit()
    connection.close()
    
    return "information stored successfully"
@app.route('/register', methods =['GET', 'POST'])
def register():
   if request.method == 'GET':
    return render_template('register.html')
   else:
   
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        connection=sqlite3.connect('register.db')
        cursor=connection.cursor()
        cursor.execute('INSERT INTO register(Username,password,Email) VALUES(?,?,?)', (username, password, email ))
        connection.commit()
        connection.close()
         
        return "You have successfully registered !"
    
headings=("Name","Category","Rating","price","Quantity")
Data=(
    ("professional hair  dryer","haircare","3","12.4$","10"),
    ("professional hair straighners","haircare","7","15.4$","10"),
    ("professional hair  dryer","haircare","4","12.4$","19"),
    ("professional hair  dryer","haircare","2","16.4$","13"),
    ("professional hair  dryer","haircare","5","11.4$","2"),
)
    
@app.route('/table', methods =['GET', 'POST'])
def table():
       return render_template('table.html',headings=headings,Data=Data)
    
 
      
     
    
   

   