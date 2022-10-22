class TicTacToe:
    SIZE = 3
    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.last_player = ''


    def play(self, x, y) -> str:
        self.check_axis(x)
        self.check_axis(y)
        self.last_player = self.next_player()
        self.set_box(x, y)
        if self.is_win():
            return f"{self.last_player} is the winner"
        return "No winner"
    def check_axis(self, value):
        if value < 1 or value > 3:
            raise RuntimeError("Value is outside board")


    def set_box(self, x, y):
        if self.board[x - 1][y - 1] != '':
            raise RuntimeError("Box is occupied")
        else:
            self.board[x - 1][y - 1] = self.last_player


    def next_player(self) -> str:
        if self.last_player == 'X':
            return 'O'
        return 'X'


    def is_win(self) -> bool:
        player_total = self.last_player * self.SIZE
        diagonal_1=''
        diagonal_2=''
        for index in range(self.SIZE):
            diagonal_1+=self.board[index][index]
            diagonal_2+=self.board[index][self.SIZE- index - 1]
            if self.board[0][index] + self.board[1][index] + self.board[2][index]==player_total:
                 return True
            elif self.board[index][0] + self.board[index][1] + self.board[index][2]==player_total:
                 return True
            if diagonal_1 == player_total or diagonal_2 == player_total:
                return True
        return False
    def is_draw(self):
        for x in range (self.SIZE):
            for y in range(self.SIZE):
                if self.board[x][y]=='':
                    return False
                return True
