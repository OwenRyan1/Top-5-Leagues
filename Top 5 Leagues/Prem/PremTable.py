import requests
url = 'https://thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2023-2024'
response = requests.get(url)
data = response.json()

#accessing teams postition in league and adding num
temp = []
for i in range(20):
    temp.append(f"{(str(i+1))} - {(data['table'][i]['strTeam'])}")

#creating a string for html format table
PremTable = ""
for i in temp:
    PremTable += (i+"<br>")
