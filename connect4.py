
BOARD_COLS = 7
BOARD_ROWS = 6


class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] # [r, c]

    def print_board(self):
        print("\n")
        # Numeriranje stupaca
        for r in range(BOARD_COLS):
            print(f"  ({r+1}) ", end="")
        print("\n")

        
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")

        print(f"{'-' * 42}\n")

    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
        #traženje slobodnih poteza
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        
        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    #prestani pretraživati u ovom smjeru
                    d[2] = False

        
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} je pobjednik!")
                return last_letter   

        # nema pobjednika
        return False

def play():
    # inicijalizacija
    game = Board()

    game_over = False
    while not game_over:
        game.print_board()

        # traži unos od korisnika
        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()} je na redu, izaberi stupac (1-{BOARD_COLS}): ")
            try:
                valid_move = game.turn(int(user_move)-1)
            except:
                print(f"Izaberite broj između 1 i 7 {BOARD_COLS}")

        # kraj igre ako ima pobjednik
        game_over = game.check_winner()
        
        # kraj igre ako je neriješeno
        if not any(' ' in x for x in game.board):
            print("Igra je neriješena.")
            return


if __name__ == '__main__':
    play()