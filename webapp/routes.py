from flask import render_template, redirect, url_for
from webapp import app

@app.route("/")
def main():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")