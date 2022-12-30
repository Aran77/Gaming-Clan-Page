from flask import Flask, render_template
import requests
import json
import pandas as pd

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

api_url = "https://nykloo.com/api/PlayerStats/Stats/"

STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,
            static_folder=STATIC_FOLDER)

def getdata():
    d=[]
    members = ['74858C942F89E7CD','2C46189ECA58F6E9','D737372B153287B6','35D271462D9D51C9','DAB84E33EF1FB7A3','353294D952B83FE5','9C407141D884E344','AD04C0C21AACF21B','515FE93B4DD376F0','CC97CACB108F523C']
    for member in members:
        params = member
        response = requests.get(api_url + params)
        if response.status_code == 200:
            data = response.json()
            for statistic in data['playerStatistics']:
                if statistic['statisticName'] == 'SeasonKills':
                    season_kills = statistic['value']
                elif statistic['statisticName'] == 'SeasonGamesPlayed':
                    season_games_played = statistic['value']
                elif statistic['statisticName'] == 'SeasonDamage':
                    season_damage = statistic['value']
                elif statistic['statisticName'] == 'SeasonWins':
                    season_wins = statistic['value']
            d.append(
                {"playerName": data['accountInfo']['titleInfo']['displayName'],
                "playerAvatar": data['accountInfo']['titleInfo']['avatarUrl'],
                "seasonGamesPlayed": season_games_played,
                "seasonKills" : season_kills,
                "seasonDamage": season_damage,
                "seasonWins" : season_wins,
                "seasonAVGKills" : season_kills / season_games_played,
                "seasonAVGDamage" : season_damage /season_games_played,
                "seasonAVGWins" : (season_wins / season_games_played)*100
                }
            )

        else:
            print('shit')

    return(d)

@app.route('/')
def home():
    scoreboard = getdata()
    return render_template('scoreboard.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run()
