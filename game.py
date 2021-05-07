class Game:
    def __init__(self, id):
        self.went = [False, False]
        self.ready = False
        self.id = id
        self.moves = [None, None]

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        self.went[player] = True

    def connected(self):
        return self.ready

    def winner(self):
        p1 = self.moves[0]
        p2 = self.moves[1]
        winner = -1

    def resetWent(self):
        self.went[0] = False
        self.went[1] = False