from copy import deepcopy


class Problem:
    def __init__(self, board):
        self._state = board

    def sudoku_board(self):
        return self._state

    @staticmethod
    def expand(board, row, column):
        children = []
        n = board.get_size()
        for candidate in range(1, n+1):
            if board.is_allowed(row, column, candidate):
                candidate_sol = deepcopy(board)
                candidate_sol.get_board()[row][column] = candidate
                children.append(candidate_sol)
        return children

    @staticmethod
    def expand_no_checks(board):
        children = []
        n = board.get_size()
        row, column = board.next_empty_cell()
        for candidate in range(1, n + 1):
            candidate_sol = deepcopy(board)
            candidate_sol.get_board()[row][column] = candidate
            children.append(candidate_sol)
        return children

    @staticmethod
    def is_solution_rows(board):
        for row in range(0, board.get_size()):
            sum_row = 0
            for col in range(0, board.get_size()):
                sum_row = sum_row + board.get_board()[row][col]
            if sum_row != board.get_sum():
                return False
        return True

    @staticmethod
    def is_solution_cols(board):
        for col in range(0, board.get_size()):
            sum_col = 0
            for row in range(0, board.get_size()):
                sum_col = sum_col + board.get_board()[row][col]
            if sum_col != board.get_sum():
                return False
        return True

    def is_solution(self, board):
        return self.is_solution_rows(board) and self.is_solution_cols(board)

    @staticmethod
    def heuristic(board, row, column):
        values_row = []
        for i in range(0, board.get_size()):
            if board.get_board()[row][i] != 0:
                values_row.append(board.get_board()[row][i])

        values_col = []
        for i in range(0, board.get_size()):
            if board.get_board()[i][column] != 0:
                values_col.append(board.get_board()[i][column])

        options = 0
        for candidate in range(1, board.get_size()+1):
            if candidate not in values_row and candidate not in values_col:
                options = options + 1

        return options









