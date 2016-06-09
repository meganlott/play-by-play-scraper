from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def scrape(year, team):

    # TODO: get teamid to make it work for all teams

    page = urlopen("http://espn.go.com/college-football/team/schedule/_/id/59/year/" + str(year) + "/" + str(team))
    soup = bs(page, "lxml")

    title = soup.html.head.title

    games = soup.findAll('li')
    g = []

    for game in games:
        if "class=\"score\"" in str(game):
            game = str(game)
            game = game[27:]
            game = game.split("\">")[0]
            gameid = game.split("id=")[1]
            g.append(str(gameid))

    return(g)