import requests

#accessing API 
url = 'https://thesportsdb.com/api/v1/json/3/lookuptable.php?l=4334&s=2023-2024'
response = requests.get(url)
data = response.json()

teams = []
temp = []
for i in range(18):     #num teams in league
    #adding all team names
    teams.append(data["table"][i]["idTeam"])

    #adding name plus standing position
    temp.append(f"{(str(i+1))} - {(data['table'][i]['strTeam'])}")

#creating a string for html format table
Ligue1Table = ""
for i in temp:
    Ligue1Table += (i+"<br>")