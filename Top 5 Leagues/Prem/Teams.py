import requests

#accessing API 
url = 'https://thesportsdb.com/api/v1/json/3/search_all_teams.php?l=English%20Premier%20League'
response = requests.get(url)
data = response.json()

PremTeams = []
for i in range(len(data["teams"])):
    #adding all team names in prem
    PremTeams.append(data["teams"][i]["idTeam"])
