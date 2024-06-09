# =============================================================================
import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=' ', font=('Helvetica', 60), width=3, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j, sticky='news')
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(
            self.master, text=f"Player {self.current_player}'s turn", font=('Helvetica', 14))
        self.status_label.grid(row=3, column=0, columnspan=3, sticky='news')

        self.restart_button = tk.Button(self.master, text='Restart', font=(
            'Helvetica', 14), command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky='news')

    def handle_click(self, row, col):
        if self.board[row][col] == ' ' and not self.game_over:
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_win():
                self.status_label.config(
                    text=f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                self.status_label.config(text="Draw!")
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(
                    text=f"Player {self.current_player}'s turn")

    def check_win(self):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for val in row:
                if val == ' ':
                    return False
        return True

    def restart_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        for row in self.buttons:
            for button in row:
                button.config(text=' ')
        self.status_label.config(text=f"Player {self.current_player}'s turn")


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
# =============================================================================