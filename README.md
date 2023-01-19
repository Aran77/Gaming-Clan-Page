# POULATION ONE VR Gaming Clan Website

Requires Flask, TinyDB, Requests

## A simple one page website for a gaming clan. 
Pulls member details and scores from a TinyDB Database.
A separate script is to be establish on a hourly chron job to pull in API player stats from the Population One servers and saved into TinyDB.

Clan members list stored in db.json.
Scores list stored in data.json

Small utility program (editdb.py) to maintain members list.

### TO DO:
- Put the get_api_data.py script on a chronjob to run hourly
- Create flask based member management
- Locate 
~~- Separate the API call into a separate program to be run on chron once every hour and store resulting data in TinyDB~~

~~- Remove API call from main program and include DB lookup instead.~~

~~- Load members list from DB~


