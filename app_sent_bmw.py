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

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# insp = inspect(engine)
# print(insp.get_columns("tweet_counts"))


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# /tweets/<variable_name>
@app.route("/sentiment")
# change app name for mult routes
def sentiment():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all sentiment data
    results = session.query(Counts.lat, Counts.long, Counts.city, Counts.state_code, Counts.hashtag, Counts.polarity, Counts.analysis).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    sent_tweets = []
    for lat, long, city, state_code, hashtag, polarity, analysis in results:

        # if hashtag == "Biden":
        sent_dict = {}
        sent_dict["hashtag"] = hashtag
        sent_dict["coordinates"] = [lat, long]
        sent_dict["city"] = city
        sent_dict["state_code"] = state_code
        sent_dict["polarity"] = polarity
        sent_dict["analysis"] = analysis

        sent_tweets.append(sent_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(sent_tweets)

# Buckley's time app.route
@app.route("/time")
# change app name for mult routes
def time():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all sentiment data
    results = session.query(Counts.created_at, Counts.trump, Counts.biden).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    time_tweets = []
    for created_at, trump, biden in results:

        # if hashtag == "Biden":
        time_dict = {}
        time_dict["created_at"] = created_at
        time_dict["trump"] = trump
        time_dict["biden"] = biden
        

        time_tweets.append(time_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(time_tweets)



if __name__ == '__main__':
    app.run(debug=True)