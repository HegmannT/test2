import os

from flask import Flask, session, render_template        #Imports Flash module
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)   # Create a new web application, be a flash web app, this file represents app

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


#-------------------------------------------------------------------------------


@app.route("/")   #App designed in routes, what page want to request, slash represents default page
                    # When user goes to just / on the web page, run the function below, tie imediate function below (homepage)
def index():
    return render_template("indexstart.html")   #Define index function to return soemthing basic print out



#-------------------------------------------------------------------------------

@app.route("/test2")   #New route at page /test2
def index():
    return "Page Test 2"



#-------------------------------------------------------------------------------

@app.route("/<string:name>")   #Template, slash any string called name, the name gets passed into hello function as argument and runs
                                #Dynamic web application depending on whats passed into the URL
def hello(name):
    return f"<h1>Hello, {name}!</h1>" #Can use html with flask like H1 for a header

                                        #Can also load in through flask html files and render them instead (templates section in video)


































