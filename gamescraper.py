from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def scrape(gid):
    page = urlopen("http://espn.go.com/college-football/playbyplay?gameId=" + str(gid))
    # page = urlopen("http://espn.go.com/college-football/playbyplay?gameId=400756963")
    soup = bs(page, "lxml")

    title = soup.html.head.title
    titleedit = str(title).replace("<title>", "")
    titleedit = titleedit.replace("</title>", "")
    data = titleedit.split(" - ")
    teams = data[0].split(" vs. ")
    date = data[2]

    awayteam = teams[0]
    hometeam = teams[1]

    data = []
    data.append(hometeam)
    data.append(awayteam)
    data.append(date)

    # print("Home Team: " + hometeam)
    # print("Away Team: " + awayteam)
    # print("Date: " + date + "\n")

    plays = soup.findAll('span')

    # quarters = [[] for _ in range(4)]
    # count = 0

    for play in plays:
        play = str(play)
        if "class=\"post-play\"" in play:
            play = play.replace("<span class=\"post-play\">", "")
            play = play.replace("</span>", "")
            play = play.strip()

    #         if "End of " in play:
    #             count += 1
    #         else:
    #             quarters[count].append(play)

    # for q in quarters:
    #     extractplays(q)

    return (data)

def extractplays(quarter):
    for play in quarter:
        timedata = play[:13]
        comment = play[13:]
        timedata = timedata.replace("(", "")
        timedata = timedata.replace(")", "")
        timedata.strip()
        timedata = timedata.split(" - ")
        time = timedata[0]
        date = timedata[1]