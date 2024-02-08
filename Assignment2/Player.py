import numpy as np
import math

ROW_COUNT = 6
COL_COUNT = 7
MAX_DEPTH = 3

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        # raise NotImplementedError('Whoops I don\'t know what to do')
        moves = dict()

        valid_cols = self.get_valid_cols(board)
        
        for move in valid_cols:
            tmp_board = np.copy(board)
            # tmp_board[self.get_next_open_row(tmp_board, j), j] = self.player_number
            moves[move] = {'move': move, 'score': self.alphabeta(-math.inf, math.inf, tmp_board, 0, True)}
        
        return max(moves)
        
        # return 0

    def alphabeta(self, alpha, beta, board, depth, maxPlay):
        opponent_number = 2 if self.player_number == 1 else 1
        winning_move = self.game_completed(board)
        if depth == MAX_DEPTH or winning_move:
            return int(self.evaluation_function(board))

        if maxPlay:
            value = -math.inf
            for move in range(0, COL_COUNT):
                valid_cols = self.get_valid_cols(board)
                for col in valid_cols:
                    b_copy = board.copy()
                    row = self.get_next_open_row(b_copy, col)
                    b_copy[row, col] = int(self.player_number)
                    new_score = self.alphabeta(alpha, beta, b_copy, depth+1, False)
                    # print("New score maxPlay {} depth {}".format(new_score, depth))
                    if new_score > value:
                        value = new_score
                        column = col
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
                return value
        else:
            value = math.inf
            for move in range(0, COL_COUNT):
                valid_cols = self.get_valid_cols(board)
                for col in valid_cols:
                    b_copy = board.copy()
                    row = self.get_next_open_row(b_copy, col)
                    b_copy[row, col] = int(opponent_number)
                    new_score = self.alphabeta(alpha, beta, b_copy, depth+1, True)
                    # print("New score minPlay {} depth {}".format(new_score, depth))
                    if new_score < value:
                        value = new_score
                        column = col
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
                return value


    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        raise NotImplementedError('Whoops I don\'t know what to do')


    def evaluation_function(self, board):
        """
        Given the current stat of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """
        opponent_number = 2 if self.player_number == 1 else 1

        possibilities = {
            "{0}{0}{0}{0}".format(self.player_number): 100,
            "{0}{0}{0}{1}".format(self.player_number, opponent_number): 4,
            "{0}{0}{1}{0}".format(self.player_number, opponent_number): 4,
            "{0}{0}{1}{1}".format(self.player_number, opponent_number): 2,
            "{0}{1}{0}{0}".format(self.player_number, opponent_number): 4,
            "{0}{1}{0}{1}".format(self.player_number, opponent_number): 2,
            "{0}{1}{1}{0}".format(self.player_number, opponent_number): -4,
            "{0}{1}{1}{1}".format(self.player_number, opponent_number): -5,
            "{1}{0}{0}{0}".format(self.player_number, opponent_number): 4,
            "{1}{0}{0}{1}".format(self.player_number, opponent_number): -2,
            "{1}{0}{1}{0}".format(self.player_number, opponent_number): -2,
            "{1}{0}{1}{1}".format(self.player_number, opponent_number): -4,
            "{1}{1}{0}{0}".format(self.player_number, opponent_number): 2,
            "{1}{1}{0}{1}".format(self.player_number, opponent_number): 90,
            "{1}{1}{1}{0}".format(self.player_number, opponent_number): 90,
            "{1}{1}{1}{1}".format(self.player_number, opponent_number): -100,
            "{0}{0}{0}0".format(self.player_number): 5,
            "{0}{0}0{0}".format(self.player_number): 5,
            "{0}{0}00".format(self.player_number): 2,
            "{0}0{0}{0}".format(self.player_number): 5,
            "{0}0{0}0".format(self.player_number): 2,
            "{0}00{0}".format(self.player_number): 2,
            "{0}000".format(self.player_number): 1,
            "0{0}{0}{0}".format(self.player_number): 5,
            "0{0}{0}0".format(self.player_number): 2,
            "0{0}0{0}".format(self.player_number): 2,
            "0{0}00".format(self.player_number): 1,
            "00{0}{0}".format(self.player_number): 2,
            "00{0}0".format(self.player_number): 1,
            "000{0}".format(self.player_number): 1
        }

        score = 0
        for p in possibilities:
            if self.check_horizontal(p, board):
                score += possibilities[p]
            
            if self.check_verticle(p, board):
                score += possibilities[p]

            if self.check_diagonal(p, board):
                score += possibilities[p]
       
        return score

    def score_board(self, board):
        return np.random.randint(1, 11)
    
    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT-1, -1, -1):
            if board[r][col] == 0:
                return r

    def get_valid_cols(self, board):
        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)
        
        return valid_cols

    def game_completed(self, board):
        player_win_str = '{0}{0}{0}{0}'.format(self.player_number)
        # print(player_win_str)

        return (self.check_horizontal(player_win_str, board) or
                self.check_verticle(player_win_str, board) or
                self.check_diagonal(player_win_str, board))
        
    def check_horizontal(self, player_win_str, b):
        to_str = lambda a: ''.join(a.astype(str))
        for row in b:
            # print(to_str(row))
            if player_win_str in to_str(row):
                return True
        return False

    def check_verticle(self, player_win_str, b):
        return self.check_horizontal(player_win_str, b.T)

    def check_diagonal(self, player_win_str, b):
        to_str = lambda a: ''.join(a.astype(str))
        for op in [None, np.fliplr]:
            op_board = op(b) if op else b
            
            root_diag = np.diagonal(op_board, offset=0).astype(int)
            if player_win_str in to_str(root_diag):
                return True

            for i in range(1, b.shape[1]-3):
                for offset in [i, -i]:
                    diag = np.diagonal(op_board, offset=offset)
                    diag = to_str(diag.astype(int))
                    if player_win_str in diag:
                        return True

        return False


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move

