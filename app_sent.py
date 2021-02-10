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
@app.route("/sentcounts")
# change app name for mult routes
def sentcounts():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(SentCount.analysis, SentCount.Biden_Count, SentCount.Trump_Count).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    sent_count = []
    for analysis, Biden_Count, Trump_Count in results:

        count_dict = {}
        count_dict["analysis"] = analysis
        count_dict["Biden_Count"] = Biden_Count
        count_dict["Trump_Count"] = Trump_Count

        sent_count.append(count_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(sent_count)


if __name__ == '__main__':
    app.run(debug=True)