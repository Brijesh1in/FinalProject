from flask import Flask,render_template,request
import pymysql
app=Flask(__name__)
@app.route('/')
def my_form():
    return render_template('login.html')
@app.route('/',methods=['POST'])
def Authenticate():
    username=request.form['u']
    password=request.form['p']
    con = pymysql.connect(host='localhost', user='root', password='')
    cursor=con.cursor()
    cursor.execute("use login")
    cursor.execute("SELECT *from auth where username='"+username+"'and password='"+password+"'")
    data=cursor.fetchone()
    if data is None:
        return "Username or pasword is wrong"
    else:
        return "logged in successfully"
if __name__=="__main__":
    app.run()


