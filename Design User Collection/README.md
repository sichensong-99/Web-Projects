# User-information-collection

## Step 1: Create a model through 'class' in Python file. 

## Step 2: Create registration web page and import the model 

Meanwhile, at the top of the registration page, we have to import the model named User. So we write down [from model import User]

## Step 3：Define the value
In register.html, we define the value as user.name/ user.email/user.password. The reason we use 'if... else' is that if users don't imput any value, the imputbox will not show none instead of keeping blank.

## Step 4: Define the table
In order to display the registered information on web page, we create model.py to define the table, which is used to save information.

## Step 5: Define data type
Then we create form.py to define data type. 

Importing datatype from wtforms.

## Step 6: Define a database

Create a db.py to define a database that saving registered information.

## Step 7：Import model and form

Importing model and form that we've already created in previous steps.

from flask import Flask, render_template, request, redirect, url_for, flash

import requests

import sqlite3 

from model import User 

from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

def register():

    form = RegisterForm() 
    
    if form.validate_on_submit():
    
        try: 
        
            user = User(form.name.data, form.email.data, form.password.data, form.age.data,form.gender.data,
            
            form.feedback.data, form.experience.data,form.checkbox.data) 
           
## Step 8: Connect the database
Connecting the database that we created in previous step.

 with sqlite3.connect(DATABASE) as con: 
 
                cur = con.cursor() 
                
                cur.execute("INSERT INTO user1 (name,email,password,age,gender,feedback,experience,checkbox) VALUES (?,?,?,?,?,?,?,?)",
...


Above all, the user collection page will be like this.

![assignment7-1](https://github.com/sichensong-99/Web-Application-Projects/blob/master/pics/assignment7-1.png)
![assignment7-2](https://github.com/sichensong-99/Web-Application-Projects/blob/master/pics/Assignment7-2.png)
