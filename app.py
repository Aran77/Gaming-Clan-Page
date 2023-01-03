from flask import Flask, render_template
from tinydb import TinyDB

#set the FLASK static folder for our assets
STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,
            static_folder=STATIC_FOLDER)


def loadScores():
    db = TinyDB('data.json')
    table = db.table('scores')
    scores = table.all()
    sortedScores = sorted(scores, key=lambda x: x['seasonAVGWins'], reverse=True)
    return sortedScores

@app.route('/')
def home():
    scoreboard = loadScores()
    return render_template('scoreboard.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run()
