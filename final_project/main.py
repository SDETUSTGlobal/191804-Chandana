from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL
import MySQLdb
from werkzeug.utils import redirect

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "project"

db = MySQL(app)





@app.route('/', methods=['GET', 'POST'])
def profile():
    if request.method == "POST":
        if "username" in request.form and "uid" in request.form and "company_name" in request.form and "email" in request.form:
            global username
            username = request.form['username']
            global uid
            uid = request.form['uid']
            global company_name
            company_name = request.form['company_name']
            global email
            email = request.form['email']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO project.inform(name1,uid,company_name,email) values(%s, %s ,%s, %s)",
                        (username, uid, company_name, email))
            db.connection.commit()
            return redirect(url_for('home'))
    return render_template("index.html")

@app.route('/home', methods=['GET'])
def home():

    return render_template("home.html", name1=username,id=uid,cname=company_name,e1=email )

if __name__ == '__main__':
    app.run(debug=True)
