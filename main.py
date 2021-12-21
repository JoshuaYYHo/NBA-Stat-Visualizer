from nba_api.stats.static import players

# list of all nba players
nba_players = players.get_players()
# trying to use a loop to get all active players in the nba
currentplayers = []
for player in nba_players:
    if player.get("is_active") != False:
        currentplayers.append(player)

print(len(currentplayers))
