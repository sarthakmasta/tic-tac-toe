import tkinter as tk
from player import SmartComputerPlayer


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board_state = [' ' for _ in range(9)]
        self.buttons = []
        self.current_player = 'X'
        self.ai = SmartComputerPlayer('O')
        self.game_active = True

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        self.create_board()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.restart_button = tk.Button(self.control_frame, text="Restart", font=("Arial", 12), command=self.restart_game)
        self.restart_button.grid(row=0, column=0, padx=10)

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.button_frame, text=' ', font=('Arial', 32), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board_state[index] == ' ' and self.game_active:
            self.board_state[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(index, self.current_player):
                self.show_result(f"{self.current_player} wins!")
                return
            elif ' ' not in self.board_state:
                self.show_result("It's a draw!")
                return
            self.current_player = 'O'
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        move = self.ai.get_move(self)
        self.board_state[move] = 'O'
        self.buttons[move].config(text='O')
        if self.check_winner(move, 'O'):
            self.show_result("O wins!")
        elif ' ' not in self.board_state:
            self.show_result("It's a draw!")
        else:
            self.current_player = 'X'

    def available_moves(self):
        return [i for i, cell in enumerate(self.board_state) if cell == ' ']

    def empty_squares(self):
        return ' ' in self.board_state

    def num_empty_squares(self):
        return self.board_state.count(' ')

    def check_winner(self, idx, mark):
        row = idx // 3
        col = idx % 3
        row_cells = self.board_state[row * 3:(row + 1) * 3]
        col_cells = [self.board_state[col + i * 3] for i in range(3)]
        diag1 = [self.board_state[i] for i in [0, 4, 8]]
        diag2 = [self.board_state[i] for i in [2, 4, 6]]

        if all(cell == mark for cell in row_cells): return True
        if all(cell == mark for cell in col_cells): return True
        if idx % 2 == 0:
            if all(cell == mark for cell in diag1): return True
            if all(cell == mark for cell in diag2): return True
        return False

    def show_result(self, message):
        self.game_active = False
        self.result_label.config(text=message)

    def restart_game(self):
        self.board_state = [' ' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=' ', state=tk.NORMAL)
        self.current_player = 'X'
        self.game_active = True
        self.result_label.config(text="")


if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()