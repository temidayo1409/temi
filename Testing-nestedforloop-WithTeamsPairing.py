import random
PL_Teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley", "Brentford", "Chelsea", "Crystal Palace", "Everton", "Leeds", "Leicester", "Liverpool", "Manchester City", "Manchester United", "Newcastle", "Norwich", "Southampton", "Tottenham", "Watford", "WestHam", "Wolves"]

#Now we have to select the teams randomly

num = 1
while num<=5:
    random.shuffle(PL_Teams)
    num+=1


#Next is to write the code that will pair the teams for home and away matches

for home_team in PL_Teams:
    for away_team in PL_Teams:
        if home_team != away_team:
            Pairings = (home_team + " VS " + away_team)
print(Pairings)



