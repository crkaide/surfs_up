############################################# MODULE TRAINING #############################################

# # Import Flask dependency
# from flask import Flask

# # Create a new Flask app instance
# app = Flask(__name__)

# # Create root
# @app.route('/')

# @app.route('/')
# def hello_world():
#     return 'Hello world (take 3)'

############################################# FLASK WEATHER APP #############################################

########## Dependencies ##########

# Standard
import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask
from flask import Flask, jsonify


########## Set up the database ##########

# Set up database engine for the Flask application
# (allows us to access and query our SQLite database file)
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect the tables/database
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)


########## Define app for Flask application ##########

# To define our Flask app, add the following line of code. 
# This will create a Flask application called "app."
app = Flask(__name__)


########## Build Flask routes ##########

# Define the root / welcome route
@app.route("/")

# Add routing information for each of the other routes

# First, create a function welcome() with a return statement:
def welcome():
    return(
    # Next, add the precipitation, stations, tobs, and temp 
    # routes that we'll need for this module into our return 
    # statement. We'll use f-strings to display them for our 
    # investors:
    '''
    Welcome to the Climate Analysis API! - 
    Available Routes: - 
    /api/v1.0/precipitation - 
    /api/v1.0/stations - 
    /api/v1.0/tobs - 
    /api/v1.0/temp/start/end - 
    ''')

# Create the precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Create the stations route
@app.route("/api/v1.0/stations")

# Create the stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# Define the temperature route
@app.route("/api/v1.0/tobs")

# Create temperature function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Create the statistics route.
# This route is different from the previous ones in 
# that we will have to provide both a starting and 
# ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the statistics function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# After running this code, you'll be able to copy and paste 
# the web address provided by Flask into a web browser. 
# Open /api/v1.0/temp/start/end route and check to make 
# sure you get the correct result, which is:

# [null,null,null]

# This code tells us that we have not specified a start and 
# end date for our range. Fix this by entering any date in 
# the dataset as a start and end date. The code will output 
# the minimum, maximum, and average temperatures. For 
# example, let's say we want to find the minimum, maximum, 
# and average temperatures for June 2017. You would add the 
# following path to the address in your web browser:

# /api/v1.0/temp/2017-06-01/2017-06-30
