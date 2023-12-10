from flask import Flask, render_template,flash,request,redirect,url_for,session,jsonify,render_template_string # For flask implementation
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
from bson.errors import InvalidId # For catching InvalidId exception for ObjectId
import os
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bcrypt = Bcrypt(app) 

mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
client = MongoClient(mongodb_host, mongodb_port)    #Configure the connection to the database
db = client.camp2023    #Select the database
todos = db.movies #Select the collection
movies_collection = db.movie_list
users = db.users

title = "Movie List"
heading = "Welcome to Sia's Movie Rating System"
#modify=ObjectId()

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route("/")
def movies():
    # Display all movies
    movies = todos.find()
    a1 = "active" if request.path == "/list" else ""
    return render_template('main.html', movies=movies, a1=a1, t=title)

@app.route("/default-page")
def default_page():
    # Render your default page here
    return render_template("default_page.html")

@app.route("/action", methods=['POST'])
def action():
    # Adding a Task
    name = request.values.get("name")
    comment = request.values.get("comment")
    date = request.values.get("date")
    rate = request.values.get("rate")

    # Get the username from the session
    username = session.get('username')

    # Check if the user is not logged in
    if username is None:
        # Redirect to the login page
        return redirect(url_for('login'))

    # Insert the comment with the username into the database
    todos.insert_one({"name": name, "comment": comment, "date": date, "rate": rate, "username": username})

    return redirect(url_for('dashboard'))  # Redirect to the movies list page

@app.route("/list")
def movie_list():
    # Fetch data from MongoDB
    movies = list(movies_collection.find())
    a1 = "active"
    username = get_current_username()
    # Render the template with MongoDB data
    return render_template('list.html',a1=a1, username=username,movies=movies)

def get_current_username():
    # Assuming you store the username in the session during login
    return session.get('username')
	
@app.route("/comment")
def movies_lists():
    # Display all Tasks
    todos_l = todos.find()
    username = get_current_username()
    a1 = "active"
    return render_template('comment.html', a1=a1, todos=todos_l, username=username,t=title, h=heading)
def get_current_username():
    # Assuming you store the username in the session during login
    return session.get('username')
#	if(str(redir)=="http://localhost:5000/search"):
#		redir+="?key="+id+"&refer="+refer

@app.route("/add")
def add():
    username = get_current_username()

    # Check if the user is not logged in
    if username is None:
        # Redirect to the login page
        return redirect(url_for('login'))

    # Render the add.html template with the username
    return render_template('add.html', username=username, h=heading, t=title)
def get_current_username():
    # Assuming you store the username in the session during login
    return session.get('username')

@app.route("/search")
def search():
    # For now, let's just redirect to the movie list page
    return redirect(url_for('movie_list'))

@app.route("/remove")
def remove():
    # Deleting a Task with various references
    key = request.values.get("_id")

    # Delete the comment from the 'todos' collection
    todos.delete_one({"_id": ObjectId(key)})

    # Delete the comment from the 'movies_collection' collection
    movies_collection.delete_one({"_id": ObjectId(key)})

    # Flash a success message
    flash("Comment removed successfully!", "success")

    # Redirect to the referring page (or the home page if no referrer is present)
    return redirect(request.referrer or "/")

@app.route("/update/<comment_id>", methods=["GET", "POST"])
def update(comment_id):
    if request.method == "POST":
        # Retrieve the updated data from the form
        updated_name = request.form.get("name")
        updated_comment = request.form.get("comment")
        updated_date = request.form.get("date")
        updated_rate = request.form.get("rate")

        # Update the comment in the database
        todos.update_one({"_id": ObjectId(comment_id)}, {"$set": {
            "name": updated_name,
            "comment": updated_comment,
            "date": updated_date,
            "rate": updated_rate
        }})

        # Redirect to comment.html after updating
        return redirect(url_for('movies_lists'))
    else:
        # Retrieve the existing comment data
        comment_data = todos.find_one({"_id": ObjectId(comment_id)})

        # Check if the user is logged in
        if "username" in session:
            username = session["username"]
        else:
            username = None

        # Pass the comment data and username to the update.html template
        return render_template('update.html', comment=comment_data, username=username, title="Update Comment", a1="active")


@app.route("/about")
def about():
	return render_template('about.html',t=title,h=heading)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Check if the username already exists
        existing_user = users.find_one({"username": username})
        if existing_user:
            return render_template("register.html", error="Username already exists", sign_in_url="/login")

        # Store the user in the database
        users.insert_one({"username": username, "password": hashed_password})

        return redirect("/login")

    return render_template("register.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username exists
        user = users.find_one({"username": username})

        if user and bcrypt.check_password_hash(user["password"], password):
            # Successfully logged in, set session variable
            session["username"] = username
            
            # Retrieve the previously stored URL from session
            previous_page = session.pop('currentPage', None)

            # Redirect to the previous page or a default page if none is stored
            return redirect(previous_page or url_for('dashboard'))

        else:
            return render_template("login.html", error="Invalid username or password", show_options=True)

    return render_template("login.html", show_options=False)

@app.route("/dashboard")
def dashboard():
    # Check if the user is logged in
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    else:
        # Redirect to the login page if not logged in
        return redirect("/login")
    
@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        username = request.form.get("username")
        new_password = request.form.get("new_password")

        # Check if the username exists
        user = users.find_one({"username": username})

        if user:
            # Update the user's password in the database
            hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
            users.update_one({"_id": user["_id"]}, {"$set": {"password": hashed_password}})
            return redirect("/login")
        else:
            flash("Username not found. Please check your username and try again.", "error")

    return render_template("reset_password.html")

@app.route("/search-json", methods=["GET"])
def search_json():
    refer = request.args.get("refer")
    key = request.args.get("key")

    # Query MongoDB to find movies matching the user input
    query = {refer: {"$regex": key, "$options": "i"}}
    movies = todos.find(query)

    # Render the template with the search results
    search_results_html = render_template(
        "search_results_fragment.html",
        todos=movies
    )
    # Return JSON with the HTML content for the search results
    return jsonify(html=search_results_html)

# Logout route
@app.route("/logout")
def logout():
    # Clear the session variable
    session.pop("username", None)
    return redirect(url_for("main_page"))

if __name__ == "__main__":
    env = os.environ.get('FLASK_ENV', 'development')
    port = int(os.environ.get('PORT', 5000))
    debug = False if env == 'production' else True
    app.run(port=port, debug=debug)
