import random
import math

class BasePlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, game):
        pass


class SmartComputerPlayer(BasePlayer):
    def __init__(self, mark):
        super().__init__(mark)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.mark)['position']

    def minimax(self, state, player):
        max_marker = self.mark
        opponent = 'O' if player == 'X' else 'X'

        # Check for terminal conditions
        for move in range(9):
            if state.board_state[move] == player:
                if state.check_winner(move, player):
                    return {
                        'position': None,
                        'score': 1 * (state.num_empty_squares() + 1) if player == max_marker else -1 * (state.num_empty_squares() + 1)
                    }

        if not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_marker:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for move in state.available_moves():
            state.board_state[move] = player
            # simulate the move
            sim_score = self.minimax(state, opponent)
            state.board_state[move] = ' '  # undo move
            sim_score['position'] = move

            if player == max_marker:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best