import seasonscraper
import gamescraper

masterdata = []

TEAM = "byu-cougars"

for year in range(2012, 2016):
    gameids = seasonscraper.scrape(year, TEAM)
    for gid in gameids:
        data = gamescraper.scrape(gid)
        masterdata.append(data)

print("Home Team, Away Team, Date")
# print(masterdata)
for game in range(len(masterdata)):
    data = masterdata[game]
    print(data[0] + ", " + data[1] + ", " + data[2])
