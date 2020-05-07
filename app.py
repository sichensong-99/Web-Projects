# from the flask package, import the Flask class
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file, abort
import requests
import json
import sqlite3
from werkzeug.utils import secure_filename
import os
import sys
import unicodedata
from sqlalchemy import func

import uuid
import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)



from forms import UploadForm
from model import Hotel,db
# instantiate Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
#app.config['UPLOAD_FOLDER'] = './static/uploads'
app.config['UPLOAD_FOLDER'] = 'static' + os.path.sep + "uploads"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://MASY_XD556:MASY_XD556@localhost:1522/app12c'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['TOASTR_TIMEOUT'] = 1000

db.init_app(app)

@app.before_first_request
def before_first_request_func():
    db.create_all()


@app.route("/")
def index():
     return render_template("home.html", title="Home")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/hotel", methods=['Get', 'Post'])
def hotel():
    my_form = UploadForm()
    if my_form.validate_on_submit():  

    # file we are importing
        file_csv = request.files.get('file_csv')

        if file_csv:
            file_full_path = os.path.join(
                app.config['UPLOAD_FOLDER'], file_csv.filename)
        
            file_csv.save(file_full_path)


            df = pd.read_csv(file_full_path)

            hotel_list_raw = df.to_dict('records')

            hotel_list = []
            for curr_htl in hotel_list_raw:
                htl = Hotel.from_dict(curr_htl)
                hotel_list.append(htl)
                # db.session.add(emp)
                # db.session.commit()

            # save t0 DB
            db.session.bulk_save_objects(hotel_list)
            db.session.commit()

            # test query
            chart_data=list(db.session.query(Hotel.reservation_status, func.count(Hotel.id)).group_by(Hotel.reservation_status).all())
            print("*******")
            print(chart_data)
            print("*******")  


    return render_template('upload.html',my_form=my_form)

@app.route("/table", methods=['Get', 'Post'])
def table(): 
    my_data = Hotel.query.all()

    return render_template('table.html', my_data=my_data)



@app.route("/chart")
def chart():
    my_data = Hotel.query.all()
    pie_data=list(db.session.query(Hotel.reservation_status, func.count(Hotel.id)).group_by(Hotel.reservation_status).all())
    bar_data=list(db.session.query(Hotel.market_segment, func.count(Hotel.market_segment)).group_by(Hotel.market_segment).all())
    chart_data=[]
    chart_data2=[]
    for htl in my_data:
        chart_data.append(htl.to_x_y())
        chart_data2.append(htl.to_x_y2())
    print(bar_data)
    return render_template('chart.html', my_data=my_data, pie_data=pie_data,bar_data=bar_data, chart_data = chart_data, chart_data2 = chart_data2)
   

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)