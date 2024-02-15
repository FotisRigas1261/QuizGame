class Player:
    def __init__(self, name, isLeader=False):
        self.name = name
        self.isLeader = isLeader

class Team:
    def __init__(self, leader, players):
        self.leader = leader  # Expecting a Player object with isLeader=True
        self.players = players  # A list of Player objects
        self.points = 0  # Initialize team points to 0

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def update_points(self, points):
        self.points += points