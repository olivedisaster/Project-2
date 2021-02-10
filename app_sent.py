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
StateAvg = Base.classes.state_avg
TimeAvg = Base.classes.time_avg
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
@app.route("/statesent")
# change app name for mult routes
def statesent():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(StateAvg.state_code, StateAvg.BidenAvg, StateAvg.TrumpAvg).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    state_avg = []
    for state_code, BidenAvg, TrumpAvg in results:

        state_dict = {}
        state_dict["state_code"] = state_code
        state_dict["BidenAvg"] = BidenAvg
        state_dict["TrumpAvg"] = TrumpAvg
        state_avg.append(state_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(state_avg)

@app.route("/timesent")
# change app name for mult routes
def timesent():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(TimeAvg.Date, TimeAvg.BidenAvg, TimeAvg.TrumpAvg).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    time_avg = []
    for Date, BidenAvg, TrumpAvg in results:

        time_dict = {}
        time_dict["date"] = Date
        time_dict["BidenAvg"] = BidenAvg
        time_dict["TrumpAvg"] = TrumpAvg
        time_avg.append(time_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(time_avg)

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