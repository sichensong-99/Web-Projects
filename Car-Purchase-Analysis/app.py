from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_file, abort
import requests
import sqlite3
from model import User, Profile, db, Tables, Employee, Sales
from forms import RegisterForm, LoginForm, UploadForm, ProfileForm, TableForm, EmployeeForm, SalesForm
from sqlalchemy import func #调用sqlalchemy模块中自带的函数
import pandas as pd
from werkzeug.utils import secure_filename #获取文件名
import os #用于查看文件路径
import sys #指明所有查找module，package的路径
import unicodedata #是字符数据库,且为所有Unicode字符定义字符属性
import uuid #给字符产生唯一编码

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
 # pylint: disable=no-member
app.config['UPLOAD_FOLDER'] = './static/uploads'
#这个save file的文件夹一定是不能跟app.py平级，要在子文件夹内
#app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
DATABASE = 'ssc.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
#上边这行是数据库链接的配置，格式为（数据库:///用户名)

#db = SQLAlchemy(app)
# initalize app with database
db.init_app(app)


@app.before_first_request
def before_first_request_func():
    db.create_all()

#这个功能的作用就是在表单进行第一个命令之前，把db先建了；然后U could delete this function after first-run

@app.route('/download/<path:filename>')
def downloadFile(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True)
#为了下载文件，记得在app.py里from flask import send_file

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

@app.route("/")
def sichen():  #function name
    return render_template('sichen.html', title="Sichen") 
'''
@app.route("/tags")
def tags():
    return render_template("Main page.html", title="tags")

@app.route("/register", methods=['Get','Post'])
def register():
    user = None
    if request.method == "POST":
       name = request.form['name']
       email = request.form['email']
       password = request.form['password']
       user = User(name, email, password) #build a model to store data
    return render_template("register.html", tile ="Register", user=user)

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
'''
@app.route("/profile", methods=["Get", "Post"])
#get是首次获取表单的方法，上面数值为空(默认值),获取的URL上也没有数值；
#post是用户提交信息时获取表单的方法，上面有数值，但不会反映在URL上，所以URL始终不变
def profile():
    my_form = ProfileForm() #初始化表单
    my_data = Profile()  #初始化数据，没这行，数据无法放在form中,给该表单提交的数据起名为my_data,即first_name那列数据就叫my_data.first_name
    my_data.remove_none_values() #call the function
    if my_form.validate_on_submit(): #意思是如果表单提交成功
        my_data.first_name = request.form.get('first_name')
        my_data.last_name = request.form.get('last_name')
        #print("first_name", my_data.first_name)
        #print("last_name", my_data.last_name)
        file = request.files.get('file_photo')
        if file:
            orig_filename = secure_filename(file.filename)
            new_filename = str(uuid.uuid1())#生成uuid
            my_data.file_photo_filename = orig_filename #To save the orignal file name
            my_data.file_photo_code = new_filename 
            #上面这行是为了存储uuid，目的是如果不同用户上传的不用文件，起了同一个名，靠uuid来区分

            # save to upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            
            #save to database
            db.session.add(my_data)
            db.session.commit()
            print("my_data", my_data.id)

            #redirect to display page
            return redirect('/profile/' + str(my_data.id)) #这个意思是每个数据的特定URL，比如profile/5...

    return render_template("profile.html", my_form = my_form, my_data = my_data)


@app.route("/profile/<int:id>", methods=["Get"])#即每个上传的数据都产出特定的URL
def profile_by_id(id): #这个function必须叫这个名，不然不能RUN出来
    my_data = Profile.query.filter_by(id=id).first()#只返回出每个id的第一个数据，其实也就一个
    if my_data == None:
        abort(404) #记得要from flask import abort;这个功能是调用错误界面的
    return render_template("profile_view.html", my_data = my_data)


@app.route("/tables")
def tables():
    my_data = Sales.query.all()
    chart_data = []
    chart_data2 = []
    for sal in my_data:
        chart_data.append(sal.to_x_y()) #append()函数是在相应的数组后加上元素，后面sal是定义好的类，to_x_y是在model.py里sal类下面定义的function
        chart_data2.append(sal.to_x_y2())
    return render_template('table_data.html', my_data=my_data, chart_data = chart_data, chart_data2=chart_data2)#pass data,一般会让等号两边的名字一样

@app.route("/tables2")
def tables2():
    my_data = Sales.query.all()
    chart_data = []
    chart_data2 = []
    for sal in my_data:
        chart_data.append(sal.to_x_y()) #append()函数是在相应的数组后加上元素，后面sal是定义好的类，to_x_y是在model.py里sal类下面定义的function
        chart_data2.append(sal.to_x_y2())
    return render_template('table2_data.html', my_data=my_data, chart_data = chart_data, chart_data2=chart_data2)#pass data,一般会让等号两边的名字一样

@app.route("/tables/<int:id>")
def tables_by_id(id): 
    my_data = Tables.query.filter_by(id=id).first()
    if my_data == None:
        abort(404)
    return render_template("table_data.html", my_data=my_data)
'''
@app.route("/employee", methods=["Get", "Post"])
def employee():
    my_form = EmployeeForm()
    if my_form.validate_on_submit():
       file_csv = request.files.get('file_csv')
    if file_csv:
           file_full_path = (os.path.join(app.config['UPLOAD_FOLDER'], file_csv.filename))
           file_csv.save(file_full_path) #save to the upload folder
        #load the data in the table using pandas
           df = pd.read_csv(file_full_path) #read the file through pd(pandas)
    employee_list_raw = df.to_dict('records')#意为整体构成一个列表，内层是将原始数据的每行提取出来形成字典
    employee_list = []
    for curr_emp in employee_list_raw:
            emp = Employee.from_dict(curr_emp)
     #emp.employee_id = curr_emp['EMPLOYEE_ID'] 这行里前面小写的是match model的Employee,后面大写的是match file里列名
            employee_list.append(emp) #()方法向列表末尾添加新的对象（元素）
            db.session.bulk_save_objects(employee_list)#批量save to db
       # db.session.add(emp) 
       # 上面是数据添加到db里的employee table
            db.session.commit() #提交保存到数据库
    return render_template('employee.html', my_form=my_form)
    '''
@app.route("/employee", methods=['Get', 'Post'])
def employee():
    my_form = EmployeeForm()
    # convert to list

    if my_form.validate_on_submit():  # my_form.submitted()
        # file we are importing
        file_csv = request.files.get('file_csv')

        if file_csv:
            file_full_path = os.path.join(
                app.config['UPLOAD_FOLDER'], file_csv.filename)
            # print("file_full_path", file_full_path)

            # save to upload folder
            file_csv.save(file_full_path)

            # load the data in the table using pandas
            df = pd.read_csv(file_full_path)

            # print("raw_data", df.iloc[0])

            # print("shape", df.shape)
            employee_list_raw = df.to_dict('records')

            # print("dictionary", employee_list_raw)

            employee_list = []
            for curr_emp in employee_list_raw:
                emp = Employee.from_dict(curr_emp)
                employee_list.append(emp)
                # db.session.add(emp)
                # db.session.commit()

            print("employee_list_count", len(employee_list))

            # save t0 DB
            db.session.bulk_save_objects(employee_list)
            db.session.commit()

            # test query
            e_list = Employee.query.limit(5).all()
            print("*******")
            print(e_list)
            print("*******")

        # send us to the display page
        # return redirect("/employee/" + str(my_data.id))

    return render_template('employee.html', my_form=my_form)


@app.route("/sales", methods=['Get', 'Post'])
def sales():
    my_form = SalesForm()

    if my_form.validate_on_submit():  
        file_csv = request.files.get('file_csv')
        if file_csv:
            file_full_path = os.path.join(
                app.config['UPLOAD_FOLDER'], file_csv.filename)
            file_csv.save(file_full_path)

            # load the data in the table using pandas
            df = pd.read_csv(file_full_path)

            sales_list_raw = df.to_dict('records')

            sales_list = []
            for curr_sal in sales_list_raw:
                sal = Sales.from_dict(curr_sal)
                sales_list.append(sal)
            print("sales_list_count", len(sales_list))

            db.session.bulk_save_objects(sales_list)
            db.session.commit()

    return render_template('Sales.html', my_form=my_form)


if __name__ == '__main__':
    app.run(debug=True)
