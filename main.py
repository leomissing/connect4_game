class Game:

    def __init__(self):
        self.board = [["_"] * 6 for _ in range(7)]
        self.turn = 0
        self.win = False

    def get_board(self):
        print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
        for x in range(5, -1, -1):
            print("|", self.board[0][x], "|", self.board[1][x], "|", self.board[2][x], "|", self.board[3][x], "|",
                  self.board[4][x], "|", self.board[5][x], "|", self.board[6][x], "|")

    def add_token(self, column):
        i = self.board[column].index("_")
        self.board[column][i] = self.turn % 2

    def check_win_cond(self):
        def check_line(line):
            for i in range(len(line) - 3):
                if (
                        line[i] == line[i + 1] == line[i + 2] == line[i + 3]
                        and line[i] != "_"
                ):
                    return True

        # Check horizontal
        for row in self.board:
            if self.win:
                return
            check_line(row)

        # Check vertical
        for i in range(len(self.board) - 3):
            for j in range(3):
                if self.win:
                    return
                if (
                        self.board[i][j]
                        == self.board[i][j + 1]
                        == self.board[i][j + 2]
                        == self.board[i][j + 3]
                        and self.board[i][j] != "_"
                ):
                    self.win = True
                    return

        # Check diagonal (top-left to bottom-right)
        for i in range(len(self.board) - 3):
            for j in range(len(self.board[i]) - 3):
                if self.win:
                    return
                if (
                        self.board[i][j]
                        == self.board[i + 1][j + 1]
                        == self.board[i + 2][j + 2]
                        == self.board[i + 3][j + 3]
                        and self.board[i][j] != "_"
                ):
                    self.win = True
                    return

        # Check diagonal (top-right to bottom-left)
        for i in range(len(self.board) - 3):
            for j in range(3, len(self.board[i])):
                if self.win:
                    return
                if (
                        self.board[i][j]
                        == self.board[i + 1][j - 1]
                        == self.board[i + 2][j - 2]
                        == self.board[i + 3][j - 3]
                        and self.board[i][j] != "_"
                ):
                    self.win = True
                    return

    def clear(self):
        self.__init__()

    def start(self):
        while not self.win:
            print("Player № ", self.turn % 2 + 1, " move")
            self.get_board()

            try:
                column = int(input("Enter number of column: "))
                if 0>column or 8<column:
                    raise ValueError()
            except ValueError:
                print("That was no valid number.  Try again...")
                continue
            self.add_token(column=(column - 1))
            self.check_win_cond()
            self.turn += 1
        print("The winner is Player №", self.turn % 2 + 1)
        self.get_board()


# Create an instance of the game and start it
if __name__ == "__main__":
    connect4 = Game()
    connect4.start()
