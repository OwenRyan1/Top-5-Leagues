import requests

#accessing API 
url = 'https://thesportsdb.com/api/v1/json/3/lookuptable.php?l=4335&s=2023-2024'
response = requests.get(url)
data = response.json()

teams = []
temp = []
for i in range(20):     #num teams in league
    #adding all team names in league
    teams.append(data["table"][i]["idTeam"])

    #adding all teams plus standing position
    temp.append(f"{(str(i+1))} - {(data['table'][i]['strTeam'])}")


#creating a string for html format table
LigaTable = ""
for i in temp:
    LigaTable += (i+"<br>")

