from Player import Player

class Game():
    def __init__(self):
        self.players = [Player(), Player()]
        self.turn = 0
        
    def makeMove(self):
        for i, player in enumerate(self.players):
            print("Player {}: {}".format(i + 1, player))
            
        move = input("Player {} enter move: ".format(self.turn + 1))
        move = move.split()
        
        if len(move) != 3:
            raise Exception("Invalid move")
        
        move[1] = int(move[1])
        move[2] = int(move[2])
        
        other = (self.turn + 1) % len(self.players)
        if move[0] == "swap":
            self.players[self.turn].swap(move[1:])
        elif move[0] == "tap":
            finished = self.players[self.turn].tap(self.players[other], move[1], move[2])
            if finished:
                print("Player {} wins!".format(self.turn + 1))
                return True
        else:
            raise Exception("Invalid move")
        
        self.turn = other
        return False
    
if __name__ == "__main__":
    game = Game()
    while True:
        try:
            finished = game.makeMove()
            if finished:
                break
        except Exception as e:
            print(e)
        