import requests
import json
import pandas as pd
from tinydb import TinyDB, Query, where

#Load a list of members from db.json a TinyDB
def loadMembers():
    #members list stored in db.json, load it into DB object
    db = TinyDB('db.json')
    #parse the table into a list
    members = [r['userid'] for r in db]
    #clean up DB
    db.close()
    #send the loaded data back
    return members

#;function to save the API results to another DB called data.json
#I should have created a DB with Mulitple tables!
def writetoDB(d):
    db = TinyDB('data.json')
    #set the table name
    table = db.table('scores')
    #loop the list object and save the dictionaries to the db
    for obj in d:
        table.insert(obj)
    #clean up db
    db.close()

#get the data from the API!
def getdata(members):
    d=[]
    # loop the members list and get API reponse for each
    for member in members:
        #form the URL and Querystring and get API response
        response = requests.get(api_url + member)
        #try the API and test the response
        if response.status_code == 200:
            #parse the resu
            data = response.json()
            #loop the dictionary to find the data we want and save the data to a variable
            for statistic in data['playerStatistics']:
                if statistic['statisticName'] == 'SeasonKills':
                    season_kills = statistic['value']
                elif statistic['statisticName'] == 'SeasonGamesPlayed':
                    season_games_played = statistic['value']
                elif statistic['statisticName'] == 'SeasonDamage':
                    season_damage = statistic['value']
                elif statistic['statisticName'] == 'SeasonWins':
                    season_wins = statistic['value']
            #append tyhe data to a dictionary
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
            #catch the response errors
            print('API CALL FAILED: ' + api_url + member)
    #call the save to db function
    writetoDB(d)

#call the load members function and save it in a members variable.
members = loadMembers()
#load scores and save to scoreboard ready to pass to FLASK
scoreboard = getData(members)
