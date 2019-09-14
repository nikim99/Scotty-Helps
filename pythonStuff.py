from flask import Flask, render_template, url_for, request
#style = "background-image: url({{ url_for('static', filename='background.png') }})"
app = Flask(__name__)
from rank_course import get_new_table
from graphs import makeGraph
from matplotlib import pyplot as plt
import seaborn as sns
import string

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/graph")
def makeGraphs():
    course = request.args.get("course")
    makeGraph(str(course))
    return render_template("graph.html", courseNum=course)

@app.route("/courses")
def getInputs():
    department = request.args.get("department")
    units = request.args.get("units")
    year = request.args.get("year")
    sems = request.args.get("sems")
    types = request.args.get("type")
    #query = open_file("static/queried.csv")
    get_new_table(department, units, year, sems, types)
    return render_template("table.html")

# @app.route("queried.csv")
# def read_file(file):
#     data = read_file(file)
#     return data

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(port = 6500)