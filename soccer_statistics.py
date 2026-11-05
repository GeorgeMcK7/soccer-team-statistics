# Soccer Team Tracker
# George McKenzie

def get_contributions(players):
    total={}
    

    for player in players:
        addition=player["goals"]+player["assists"]

        
        total[player["name"]]=addition

    return total

def get_top_performer(players):
    current=-1
    top_scorer=None

    for player in players:
        addition=player["goals"]+player["assists"]

        if addition>current:
            current=addition
            top_scorer=player["name"]

    return top_scorer

def get_team_statistics(players):
    statistics= {
        "total_goals": 0,
        "total_assists":0,
        "total_contributions":0,
        "average_goals":0
    }


    for player in players:
        statistics["total_goals"] += player["goals"]
        statistics["total_assists"] += player["assists"]

    statistics["total_contributions"]=(
        statistics["total_goals"]+statistics["total_assists"]
    )

    if len(players) > 0:
        statistics["average_goals"] = round(
            statistics["total_goals"] / len(players), 2
        )

    return statistics
        
















players = [
    {"name": "George", "position": "CM", "goals": 4, "assists": 6},
    {"name": "Lewis", "position": "ST", "goals": 9, "assists": 2},
    {"name": "Ryan", "position": "LW", "goals": 5, "assists": 7},
    {"name": "Jack", "position": "CB", "goals": 2, "assists": 1},
    {"name": "Daniel", "position": "CM", "goals": 3, "assists": 4}
]

print("Team Statistics:")
print(get_team_statistics(players))

print("\nPlayer Contributions:")
print(get_contributions(players))

print("\nTop Performer:")
print(get_top_performer(players))
