"""

Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.

__repr__() Returns a pretty string representation of the game board

move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.

calc_winner() What token character string has won or None if no one has.

is_full() Returns true if the game board is full.

is_game_over() Returns true if the game board is full or a player has won.
"""


class Game():
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __repr__(self):
        boardDisplay = "+" + '-'*5 + "+\n"
        for i in range(len(self.board)):
            for x in range(len(self.board[i])):
                boardDisplay += "|" + str(self.board[i][x])
            boardDisplay += "|\n"
        boardDisplay += "+" + '-'*5 + "+\n"
        return boardDisplay

    def move(self, y, x, token):
        """Place a player's token character string at a given coordinate
        (top-left is 0, 0), x is horizontal position, y is vertical position.
        """
        self.x = x
        self.y = y
        self.token = token
        self.board[self.x][self.y] = self.token

    def calc_winner(self, token):
        """
        What token character string has won or None if no one has.
        """
        self.token = token
        hasWon = False
        lineString = ""
        for i in range(len(self.board)):
            horizontalString = self.board[i][0] + self.board[i][1] + self.board[i][2]
            verticalString = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if (horizontalString == self.token*3) or (verticalString == self.token*3):
                return self.token + " has won."
        leftLine = self.board[0][0] + self.board[1][1] + self.board[2][2]
        rightLine = self.board[2][0] + self.board[1][1] + self.board[0][2]
        

class Player():
    def __init__(self, playerName, token):
        self.playerName = playerName
        self.token = token


    def __repr__(self):
        return self.playerName + ": " + self.token


def main():
    players = []
    numPlayers = int(input("How many players are there?\n> "))
    for i in range(numPlayers):
        print(f"\nPlayer {i+1}\n")
        playerName = input("What is the player's name?\n> ")
        token = str(input("What token will this player use?\n> "))
        players.append(Player(playerName, token))
    game = Game(1)
    game.move(0, 1, "O")
    print(game)
    print(players)

if __name__ == '__main__':
    main()
