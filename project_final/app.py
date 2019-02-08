import sqlite3
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)



num = 2
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('bike.db')
        c = conn.cursor()
        c.execute("""SELECT id, name, password from INFO""")
        rows = c.fetchall()
        conn.commit()
        conn.close()
        for row in rows:
              if username == row[1] and password == row[2]:
                      return render_template('home.html', name=username)  
              elif username == 'admin' and password == 'deerwalk':
                      return render_template('insert.html')
             

              
@app.route('/insertauth',methods=['POST'])
def insertauth():
        reg=request.form['reg']
        cc=request.form['cc']
        engine =request.form['eng']
        battery =request.form['bat']
        milage =request.form['mil']
        maxp =request.form['pow']
        maxt =request.form['tor']
        maxf =request.form['cap']
        conn = sqlite3.connect('bike.db')
        c = conn.cursor()
        c.execute("""INSERT INTO bike_info values (  
        '{}',{},'{}','{}','{}','{}','{}','{}'
        )""".format(reg , cc, engine,battery,milage,maxp,maxt,maxf))
        conn.commit()
        conn.close()
        return render_template('insert.html')


@app.route('/register')
def direct():
        return render_template('register.html')  

@app.route('/registerauth', methods=['POST'])        
def registerauth():
    reg=request.form['reg']
    name=request.form['name']
    password =request.form['password']
    email = request.form['email']
    age = request.form['age']
    phone_no = request.form['pnum']
    gender = request.form['gender']
    interest = request.form['interest']
    conn = sqlite3.connect('bike.db')
    c = conn.cursor()
    c.execute("""INSERT INTO INFO VALUES (  
    {},'{}', '{}', '{}', {},{},'{}','{}'
    )""".format(reg , name, password , email , age, phone_no, gender , interest))
    conn.commit()

    conn.close()
    return render_template('registerauth.html') 
   

@app.route('/yamaha')
def yamaha():
        return render_template('yamaha.html')

@app.route('/honda')
def honda():
        return render_template('honda.html')

@app.route('/suzuki')
def suzuki():
        return render_template('suzuki.html')

@app.route('/bajaj')
def bajaj():
        return render_template('bajaj.html')

@app.route('/main',methods=['POST'])
def main():
        val = request.form['all']
        conn = sqlite3.connect('bike.db')
        c = conn.cursor()
        c.execute("""SELECT * from bike_info""")
        rows = c.fetchall()
        conn.commit()
        conn.close()
        for row in rows:
                if row[0] == val:
                        return render_template('main.html',name=row)





