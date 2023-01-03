from flask import Flask, render_template
import requests
import json
import pandas as pd
from tinydb import TinyDB, Query, where

#set headers for json
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

#set the URL for the API
api_url = "https://nykloo.com/api/PlayerStats/Stats/"

#set the FLASK static folder for our assets
STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,
            static_folder=STATIC_FOLDER)


def loadScores():
    db = TinyDB('data.json')
    table = db.table('scores')
    query = Query()
    scores = table.all()
    print(scores)
    sortedScores = sorted(scores, key=lambda x: x['seasonAVGWins'], reverse=True)
    return sortedScores

@app.route('/')
def home():
    scoreboard = loadScores()
    return render_template('scoreboard.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run()
