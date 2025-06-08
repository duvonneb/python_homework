# Task 6

# Define a custom exception for invalid game moves
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Define the game board and game logic
class Board:
    # List of valid move names
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        # Create a 3x3 board filled with spaces
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"  # Start with X

    # Print the board nicely
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    # Handle player move
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        cat = True

        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break

        if cat:
            return (True, "Cat's Game.")

        win = False

        for i in range(3):
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break

        if not win:
            for i in range(3):
                if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break

        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                elif self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True

        if win:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
        else:
            return (False, f"{self.turn}'s turn.")


# ========== MAIN GAME LOOP ==========
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("Available moves:")
    for move in Board.valid_moves:
        print(f" - {move}")
    print()

    board = Board()

    # Keep playing until the game is over
    while True:
        print(board)

        # Ask player for a move
        print(f"{board.turn}'s turn.")
        move = input("Enter your move: ").strip().lower()

        try:
            board.move(move)
        except TictactoeException as e:
            print("Error:", e.message)
            continue

        game_over, message = board.whats_next()
        if game_over:
            print(board)
            print(message)
            break