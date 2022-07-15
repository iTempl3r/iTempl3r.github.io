from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home ():
    return render_template("index.html")

@views.route("/Junghans.html")
def Junghans ():
    return render_template("Junghans.html")

@views.route("/Dominik.html")
def Dominik ():
    return render_template("Dominik.html")
