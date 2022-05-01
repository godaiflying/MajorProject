from flask import Flask, render_template, redirect, url_for 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', content="cringe")


#using redirect to make sure that only admins can access this url
@app.route("/admin/")
def admin():
    return redirect(url_for("hello_world"))  

def create_app():
    return app 