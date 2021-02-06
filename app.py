import numpy as np
from flask import render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# /tweets/<variable_name>
@app.route("/biden")
# change app name for mult routes
def biden2020():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all pizza data
    results = session.query(Counts.hashtag).all()

    session.close()

    # Create a dictionary from row of data and append to a list of dictionaries
    biden_tweets = []
    for hashtag, in results:

        # if hashtag == "Biden":

        biden_dict = {}
        biden_dict["hashtag"] = hashtag
        #     # pizza_dict["pizza"] = str(pizza)
        biden_tweets.append(biden_dict)
        
    # turn the list of dicts into an array of objects
    return jsonify(biden_tweets)


if __name__ == '__main__':
    app.run(debug=True)