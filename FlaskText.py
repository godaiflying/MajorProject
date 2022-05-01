from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', content="cringe")

#getting user login
#so that the usr can be redirected to their own page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


#using redirect to make sure that only admins can access this url
@app.route("/admin/")
def admin():
    return redirect(url_for("hello_world"))  

def create_app():
    return app 