from flask import Flask, render_template,request,session,redirect,jsonify
from models import *
import pymysql

def sql_connector():
    conn = pymysql.connect(user='root', password='Tyson@05', db='azure_db', host= '127.0.0.1')
    c = conn.cursor()

    return  c,conn


app=Flask(__name__)
app.secret_key = "your_secret_key_here"

#USER REGISTER
@app.route("/signN")
def sign():
    return render_template('homePg.html')

@app.route('/signing', methods=['POST'])
def signing():
    if request.method == "POST":
        Fsname = request.form['Fsname']
        Lsname = request.form['Lsname']
        EmailID = request.form['EmailID']
        PassW = request.form['PassW']
        add_signup(Fsname,Lsname,EmailID,PassW)
        return render_template('homePg.html')
    else:
        return "Method Not Allowed", 405


@app.route('/UserL')
def UserL():
    cursor.execute("select * from signup")
    cus=cursor.fetchall()
    return render_template("/admin/UM.html",cus=cus)


#User Login
@app.route('/loging', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'EmailID' in request.form and 'PassW' in request.form:
        EmailID = request.form['EmailID']
        PassW = request.form['PassW']
        conn = pymysql.connect(user='root', password='Tyson@05', db='azure_db', host='127.0.0.1')
        c = conn.cursor()
        c.execute('SELECT * FROM signup WHERE EmailID = %s AND PassW = %s', (EmailID, PassW))
        user = c.fetchone()
        conn.commit()
        conn.close()
        c.close()

        if user:
            session['loggedin'] = True
            session['EmailID'] = user[2] 
            session['PassW'] = user[3]  
            return render_template('ABOUT1.html')
        else:
            return render_template('homePg.html')
    
    return render_template('homePg.html')    

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('Uname', None)
    session.pop('emailID', None)
    return redirect('/signN')

#Contact Info
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == "POST":
        Cname = request.form['Cname']
        em_ID = request.form['em_ID']
        MsgC = request.form['MsgC']
        add_contc(Cname,em_ID,MsgC)
        return render_template('CONTACT1.html')
    else:
        return "Method Not Allowed", 405


@app.route('/NCntc')
def NCntc():
    cursor.execute("select * from contc")
    cusq=cursor.fetchall()
    return render_template("/admin/Help.html",cusq=cusq)

@app.route('/about')
def about():
    return render_template("ABOUT1.html")

@app.route('/shop')
def shop():
    return render_template("SHOP1.html")

@app.route('/Cnt')
def Cnt():
    return render_template("CONTACT1.html")

@app.route('/cart')
def cart():
    return render_template("CART1.html")

@app.route('/bike')
def bike():
    return render_template("BIKE.html")

@app.route('/car')
def car():
    return render_template("CAR.html")






@app.route('/adminL')
def adminL():
    return render_template("/admin/ad.html")

@app.route('/PrdAdd', methods=['POST','GET'])
def PrdAdd():

    if request.method == "POST":
        prd_img = request.form['prd_img']
        prd_name = request.form['prd_name']
        prd_des = request.form['prd_des']
        prd_prc = request.form['prd_prc']
        add_Products(prd_img,prd_name,prd_des,prd_prc)
        return render_template("/admin/AP.html")
    else:
        return "Method Not Allowed", 405
    
@app.route('/prdd')
def prdd():
    return render_template("/admin/AP.html")

@app.route('/PrdDetl')
def PrdDetl():
     cursor.execute("select * from Products")
     PrdAd=cursor.fetchall()
     return render_template("/admin/PrdDet.html",PrdAd = PrdAd)


@app.route('/Ords')
def Ords():
    return render_template("/admin/Orders.html")

@app.route('/AdLogt')
def AdLogt():
    return render_template("/admin/ADlogin.html")

if __name__ =="__main__":
    app.run(debug=True)