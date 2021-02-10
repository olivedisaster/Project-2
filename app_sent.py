import numpy as np
from flask import render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/hashtag2020.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Counts = Base.classes.tweet_counts
SentAvg = Base.classes.sent_avg
SentCount = Base.classes.sent_count

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# /tweets/<variable_name>
@app.route("/bidenavg")
# change app name for mult routes
def bidenavg():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(SentAvg.city, SentAvg.lat, SentAvg.long, SentAvg.state_code, SentAvg.hashtag, SentAvg.Pol_Avg, SentAvg.analysis).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    biden_avg = []
    for city, lat, long, state_code, hashtag, polarity, analysis in results:

        if hashtag == "Biden":
            biden_dict = {}
            biden_dict["hashtag"] = hashtag
            biden_dict["coordinates"] = [lat, long]
            biden_dict["city"] = city
            biden_dict["state_code"] = state_code
            biden_dict["polarity"] = polarity
            biden_dict["analysis"] = analysis

            biden_avg.append(biden_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(biden_avg)

@app.route("/trumpavg")
# change app name for mult routes
def trumpavg():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(SentAvg.city, SentAvg.lat, SentAvg.long, SentAvg.state_code, SentAvg.hashtag, SentAvg.Pol_Avg, SentAvg.analysis).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    trump_avg = []
    for city, lat, long, state_code, hashtag, polarity, analysis in results:

        if hashtag == "Trump":
            trump_dict = {}
            trump_dict["hashtag"] = hashtag
            trump_dict["coordinates"] = [lat, long]
            trump_dict["city"] = city
            trump_dict["state_code"] = state_code
            trump_dict["polarity"] = polarity
            trump_dict["analysis"] = analysis

            trump_avg.append(trump_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(trump_avg)

# /tweets/<variable_name>
@app.route("/bidencount")
# change app name for mult routes
def bidencount():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(SentCount.analysis, SentCount.hashtag, SentCount.count).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    biden_count = []
    for analysis, hashtag, count in results:

        if hashtag == "Biden":
            bcount_dict = {}
            bcount_dict["analysis"] = analysis
            bcount_dict["hashtag"] = hashtag
            bcount_dict["count"] = count

            biden_count.append(bcount_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(biden_count)

@app.route("/trumpcount")
# change app name for mult routes
def trumpcount():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(SentCount.analysis, SentCount.hashtag, SentCount.count).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    trump_count = []
    for analysis, hashtag, count in results:

        if hashtag == "Trump":
            tcount_dict = {}
            tcount_dict["analysis"] = analysis
            tcount_dict["hashtag"] = hashtag
            tcount_dict["count"] = count

            trump_count.append(tcount_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(trump_count)

if __name__ == '__main__':
    app.run(debug=True)