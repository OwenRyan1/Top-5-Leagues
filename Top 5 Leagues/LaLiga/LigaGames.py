from LaLiga.Teams import teams
from Date import CheckingDate
import requests

def LaLigaGames(url):
    #access API
    response = requests.get(url)
    data = response.json()

    games = []
    #check for last 2 home games just incase 2 home in a row
    for i in range(2):
        #game
        games.append(data['results'][i]['strEvent'])
        #home team : goals
        games.append(data['results'][i]['strHomeTeam'])
        games.append(data['results'][i]['intHomeScore'])
        #away team : goals
        games.append(data['results'][i]['strAwayTeam'])
        games.append(data['results'][i]['intAwayScore'])
        #date
        games.append(data['results'][i]['dateEvent'])
        #making sure its the proper league (API shows all games for each team)
        games.append(data['results'][i]['strLeague'])
    return games

#base url to add id to end
#gives last 5 home games of each team(by ID)
base = ("https://thesportsdb.com/api/v1/json/3/eventslast.php?id=")

#list of most recent home games for each team
allGames = []
for i in teams:
    url = base + i
    allGames.append(LaLigaGames(url))

#recent games within # on Date file
recentGames = []
for i in allGames:
    #make sure its not passing non league games
    if i[6] != "Spanish La Liga":
        continue
    day = i[5]
    if CheckingDate(day) == True:
        recentGames.append(i)

#outputting all recent scores
def showingLaLigaGames():
    string = ''
    for i in recentGames:
        #if game is canceled dont show score
        if str(i[2]) == "None":
            continue
        #adding <br> = \n for html format
        string += f"{i[0]}<br>{i[2]} : {i[4]}<br>"

    #incase no games were played in last 5 days
    if string == "":
        string = "No Recent Games"
    return string
