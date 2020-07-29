# Consumers-analysis-for-Hotel
Step 1: In this case, we upload the hotel data file, which is CSV file, at first.

@app.route("/employee", methods=["Get", "Post"])
def employee():
    my_form = EmployeeForm()
    if my_form.validate_on_submit():
       file_csv = request.files.get('file_csv')
       if file_csv:
          file_full_path = (os.path.join(app.config['UPLOAD_FOLDER'], file_csv.filename))
          file_csv.save(file_full_path) #save to the upload folder
    return render_template("Employee.html", my_form=my_form)

 We upload the data in the table using pandas.
 
    df = pd.read_csv(file_full_path) #read the file through pd(pandas)
    '''To check how many columns and rows in the file
    
Step 2: Creating form.py to define the form.

class EmployeeForm(FlaskForm):
    file_csv = FileField()
    
Step 3: Creating model.py to define the table.

class Employee (db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    ...
    
@classmethod
    def from_dict(cls, in_dict):#in_dict refers to the data passing in
        cls = Employee() 
        cls.employee_id = in_dict['EMPLOYEE_ID']#cls refers to class Employee
        cls.first_name = in_dict['FIRST_NAME']
        cls.last_name = in_dict['LAST_NAME']
        ...
        
Step 4: Create the web page that users could upload the CSV data file.
<div class="row">
               <div class="col-sm-12">
                   <div class="form-group">
                       <label for="exampleInputFile">CSV File</label>
                       <div class="input-group">
                           <div class="custom-file">
                               <input type="file" class="custom-file-input" name="file_csv"  wtx-context="A8F69635-7B4C-4206-9EF2-B47AC8BE1122">
                               <label class="custom-file-label" for="exampleInputFile">Choose file</label>
                           </div></div></div></div></div>
