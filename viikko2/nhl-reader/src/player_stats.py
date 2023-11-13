class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()
        filtered_players = [player for player in players if player.nationality == nationality]
        return sorted(filtered_players, key=lambda player: player.total_points(), reverse=True)
