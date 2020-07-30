from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/web_article")
def web_article():  #function name
    return render_template('web_article.html', title="Web Article") 

@app.route("/")
def sichen():  #function name
    return render_template('sichen.html', title="Sichen") 

@app.route("/tags")
def tags():
    return render_template("Main page.html", title="tags")

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/linear_regression")
def linear_regression():
    return render_template("Linear_regression.html")

@app.route("/forums")
def forums():
    return render_template("Forums.html")

if __name__ == '__main__':
    app.run(debug=True)



