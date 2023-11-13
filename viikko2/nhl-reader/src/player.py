class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.team = player_dict["team"]
        self.goals = player_dict["goals"]
        self.assists = player_dict["assists"]
        self.nationality = player_dict["nationality"]

    def total_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:4} {self.goals:2} + {self.assists:2} = {self.total_points()}"
    

