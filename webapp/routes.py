#This file is purposed to define all of the route endpoints returning
#static webpages to the end user from the server.

#importing the render template function, allowing HTML documents
#in the templates file to easily be served
from flask import render_template, redirect, url_for

#app object needs to be imported for decorators
from webapp import app

#redirects people who goto the website to the homepage first
@app.route("/")
def main():
    return redirect(url_for("home"))

#defines the homepage route, returning the home.html document
@app.route("/home")
def home():
    return render_template("home.html")
