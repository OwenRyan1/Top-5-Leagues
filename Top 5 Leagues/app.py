from flask import Flask, render_template

from Prem.PremGames import showingPremGames
from Prem.PremTable import PremTable

from LaLiga.LigaGames import showingLaLigaGames
from LaLiga.Teams import LigaTable

from Bundesliga.BundesligaGames import showingBundesligaGames
from Bundesliga.Teams import BundesligaTable

from Ligue1.Ligue1Games import showingLigue1Games
from Ligue1.Teams import Ligue1Table

from SerieA.SerieAGames import showingSerieAGames
from SerieA.Teams import SerieATable

#creating the app
app = Flask(__name__)

#creating end points
#home page
@app.route("/") 
def homepage():
    return render_template("homePage.html")

#prem scores / table
@app.route("/prem") 
def premGames():
    scores = showingPremGames()
    return render_template("premGames.html",scores = scores,table = PremTable)

#laliga scores / table
@app.route("/laliga")
def laLiga():
    scores = showingLaLigaGames()
    return render_template("laLiga.html", scores = scores, table = LigaTable)

#bundesliga scores / table
@app.route("/bundesliga")
def bundesliga():
    scores = showingBundesligaGames()
    return render_template("bundesliga.html", scores = scores, table = BundesligaTable)

#ligue1 scores / table
@app.route("/ligue1")
def ligue1():
    scores = showingLigue1Games()
    return render_template("ligue1.html", scores = scores, table = Ligue1Table)

#SerieA scores / table
@app.route("/serieA")
def serieA():
    scores = showingSerieAGames()
    return render_template("serieA.html", scores = scores, table = SerieATable)

#running the app
if __name__ == "__main__":
    app.run()

