from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json
import sqlite3
from model import User
from forms import RegisterForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
 # pylint: disable=no-member
DATABASE = 'ssc.db'
'''
@app.route("/upload", methods=['Get', 'Post'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        print(form.data.photo)
'''

@app.route("/register", methods=['Get', 'Post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User(form.name.data, form.email.data, form.password.data, form.age.data,form.gender.data,form.feedback.data,
            form.experience.data,form.checkbox.data)

            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user1 (name,email,password,age,gender,feedback,experience,checkbox) VALUES (?,?,?,?,?,?,?,?)",
                            (user.name, user.email, user.password, user.age,user.gender,user.feedback,user.experience,user.checkbox))
                con.commit()
                flash('Registered Successfully!', 'success')
                return redirect(url_for('login'))
        except Exception as e:
            con.rollback()
            flash(f'Unknow error!\n{str(e)}', 'danger')
    return render_template('assignment7.html', title='Register', form=form)

@app.route("/login", methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user1 WHERE email = ? and password = ?",
                            [form.email.data, form.password.data])
                rows = cur.fetchall()
                print(rows)
                
                if rows:
                    flash('Login Successfully!', 'success')
                    return render_template('display.html', rows=rows)
                else:
                    flash(
                        'Login Unsuccessful. Please check email and password', 'danger')
        except Exception as e:
            con.rollback()
            flash(f'Unknow error!\n{str(e)}', 'danger')
    return render_template('loginn.html', title='Login', form=form)

@app.route("/display")
def display():
    
    with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user1")
            rows = cur.fetchall()
            print(rows)
            return render_template('display.html', title='Login', rows=rows)

@app.route("/web_article")
def web_article():  #function name
    return render_template('web_article.html', title="Web Article") 

@app.route("/")
def sichen():  #function name
    return render_template('sichen.html', title="Sichen") 

@app.route("/tags")
def tags():
    return render_template("Main page.html", title="tags")
'''
@app.route("/register", methods=['Get','Post'])
def register():
    user = None
    if request.method == "POST":
       name = request.form['name']
       email = request.form['email']
       password = request.form['password']
       user = User(name, email, password) #build a model to store data
    return render_template("register.html", tile ="Register", user=user)
'''
@app.route("/sorting")
def sorting():
    return render_template("sorting.html", title="Sorting")

@app.route("/link")
def link():
    return render_template("Link.html", title="7.LINK")

@app.route("/reload")
def reload():
    return render_template("Reload.html", title="1.Reload")

@app.route("/css_style")
def css_style():
    return render_template("CSS Style.html", title="3.CSS STYLE")

@app.route("/calculater")
def calculater():
    return render_template("Working_Calculater.html", title="Calculater")

@app.route("/Swap_numbers")
def Swap_numbers():
    return render_template("Swap_numbers.html", title="Swap_numbers")

@app.route("/onlineshop")
def onlineshop():
    return render_template("OnlineShop.html", title="OnlineShop")

@app.route("/dress")
def dress():
    return render_template("Dress.html", title="$100-$800")

@app.route("/coat")
def coat():
    return render_template("Coat.html", title="$1200-$3000")

@app.route("/trousers")
def trousers():
    return render_template("Trousers.html", title="$150-$1800")

@app.route("/suit")
def suit():
    return render_template("suit.html", title="$1200-$5000")

@app.route("/windbreaker")
def windbreaker():
    return render_template("Windbreaker.html", title="$2500-$9000")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
'''
@app.route("/login")
def login():
    return render_template("login.html")
'''
@app.route("/linear_regression")
def linear_regression():
    return render_template("Linear_regression.html")

@app.route("/forums")
def forums():
    return render_template("Forums.html")

@app.route("/profile", methods=["Get", "Post"])
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)



