from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
        POINTS = 1
        GOALS = 2
        ASSISTS = 3


class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, criteria="points"):
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals

        def sort_by_assists(player):
            return player.assists

        if criteria == "points":
            sort_key = sort_by_points
        elif criteria == "goals":
            sort_key = sort_by_goals
        elif criteria == "assists":  
            sort_key = sort_by_assists
        else:
            raise ValueError("Invalid criteria. Use 'points', 'goals', or 'assists'.")

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key
        )
        #testimuutos
        result = []
        i = 0
        while i < how_many and i < len(sorted_players):
            result.append(sorted_players[i])
            i += 1

        return result
