#download flask!
#download waitress
#use this to run waitress-serve --port=5000 --call FlaskText:create_app
#finished lesson 4 tech with tim flask tutorial
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
#secret key to decrypt session data
app.secret_key = "hat"


@app.route('/')
def hello_world():
    return render_template('index.html')

#getting user login
#so that the usr can be redirected to their own page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        #creating session for user
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

#using redirect to make sure that only admins can access this url
@app.route("/admin/")
def admin():
    return redirect(url_for("hello_world"))  

def create_app():
    return app 