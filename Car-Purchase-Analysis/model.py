import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # 通过类SQLALchemy连接数据库


class User():

    def __init__(self, name="", email="", password="",age="",gender="", feedback="",experience="",checkbox=""):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.feedback = feedback
        self.experience = experience
        self.checkbox =checkbox

class Profile(db.Model): 
#因为profile的表单里，所有user上传的数据要储存在db里，所以要db要用这里定义的model；同时还要在app.py里from model import db
    __tablename__ = 'Profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #Primary key
    first_name = db.Column(db.String(80), nullable=True) #first_name column
    last_name = db.Column(db.String(80), nullable=True) #last_name column
    
    file_photo_filename = db.Column(db.String(80), nullable=True) 
    file_photo_code = db.Column(db.String(80), nullable=True) 
      
    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""

        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""

class Tables(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #primary key
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True) 
    dob = db.Column(db.String(80), nullable=True)
    file_photo_filename = db.Column(db.String(80), nullable=True) 
    file_photo_code = db.Column(db.String(80), nullable=True) 
    file_data_filename = db.Column(db.String(80), nullable=True) 
    file_data_code = db.Column(db.String(80), nullable=True) 
        
    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""
        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""
        self.file_data_filename = self.file_data_filename if self.file_data_filename else ""
        self.file_data_code = self.file_data_code if self.file_data_code else ""
        self.email = self.email if self.email else ""
        self.dob = self.dob if self.dob else ""
        
class Employee (db.Model):
    __tablename__ = 'py_employee'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    hire_date = db.Column(db.Date)
    job_id = db.Column(db.String(100))
    salary = db.Column(db.Float)
    commission_pct = db.Column(db.Float)
    department_id =db.Column(db.Integer)
    department_name = db.Column(db.String(100))

    @classmethod
    def from_dict(cls, in_dict):#in_dict refers to the data passing in
        cls = Employee() 
        cls.employee_id = in_dict['EMPLOYEE_ID']#cls refers to class Employee
        cls.first_name = in_dict['FIRST_NAME']
        cls.last_name = in_dict['LAST_NAME']
        cls.email = in_dict['EMAIL']
        cls.phone_number = in_dict['PHONE_NUMBER']
        cls.hire_date = in_dict['HIRE_DATE']
        if in_dict['HIRE_DATE']: #时间转换
            cls.hire_date = datetime.datetime.strptime(
                in_dict['HIRE_DATE'], "%m/%d/%Y")#转为格式某月某天某年
        cls.job_id = in_dict['JOB_ID']
        cls.salary = in_dict['SALARY']
        cls.commission_pct = in_dict['COMMISSION_PCT']
        cls.department_id = in_dict['DEPARTMENT_ID']
        cls.department_name = in_dict['DEPARTMENT_NAME']
        return cls

class Sales (db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    order_date = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    discount = db.Column(db.Float)
    profit = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    shipping_cost = db.Column(db.Float)
    customer_name = db.Column(db.String(100))
    ship_date = db.Column(db.Date)

    def to_x_y(self):
        return {'x': self.unit_price, 'y': self.profit}

    def to_x_y2(self):
        return {'x': self.unit_price, 'y': self.profit - self.shipping_cost*self.quantity}


    @classmethod
    def from_dict(cls, in_dict):
        cls = Sales() 
        cls.order_id = in_dict['ORDER_ID']
        cls.order_date = in_dict['ORDER_DATE']
        if in_dict['ORDER_DATE']:
            cls.order_date = datetime.datetime.strptime(
                in_dict['ORDER_DATE'], "%m/%d/%Y")
        cls.quantity = in_dict['QUANTITY']
        cls.discount = in_dict['DISCOUNT']
        cls.profit = in_dict['PROFIT']
        cls.unit_price = in_dict['UNIT_PRICE']
        cls.shipping_cost = in_dict['SHIPPING_COST']
        cls.customer_name = in_dict['CUSTOMER_NAME']
        cls.ship_date = in_dict['SHIP_DATE']
        if in_dict['SHIP_DATE']:
            cls.ship_date = datetime.datetime.strptime(
                in_dict['SHIP_DATE'], "%m/%d/%Y")
        return cls




