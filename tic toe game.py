import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')

        self.current_player = 'X'
        self.board = [' ']*9  # Represents the 3x3 board as a list

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('Helvetica', 20), width=8, height=4,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(button)

        # Configure rows and columns to expand with window resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index]['text'] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo('Congratulations!', f'Player {self.current_player} wins!')
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo('Tied!', 'It\'s a tie!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        self.current_player = 'X'
        self.board = [' ']*9
        for i in range(9):
            self.buttons[i]['text'] = ' '

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == '__main__':
    main()
