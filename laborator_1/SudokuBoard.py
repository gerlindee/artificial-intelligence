from math import sqrt


class SudokuBoard:

    def __init__(self, filename):
        self._filename = filename
        self._board = self.read_table()
        self._n = len(self._board)

    def read_table(self):
        file = open(self._filename, 'r')
        board = []
        for r_line in file:
            line = []
            for num in r_line.split(' '):
                line.append(int(num))
            board.append(line)
        return board

    def get_sum(self):
        sum = 0
        for num in range(1, self._n + 1):
            sum = sum + num
        return sum

    def get_board(self):
        return self._board

    def get_size(self):
        return self._n

    def next_empty_cell(self):
        for row in range(0, self._n):
            for col in range(0, self._n):
                if self._board[row][col] == 0:
                    return row, col
        return -1, -1

    def is_present_row(self, row, val):
        return val in self._board[row]

    def is_present_column(self, col, val):
        for row in range(0, self._n):
            if self._board[row][col] == val:
                return True
        return False

    def is_present_box(self, row, col, value):
        sqrt_n = int(sqrt(self._n))
        box_row = row - row % sqrt_n
        box_col = col - col % sqrt_n
        for i in range(box_row, box_row + sqrt_n):
            for j in range(box_col, box_col + sqrt_n):
                if self._board[i][j] == value:
                    return True
        return False



    def is_allowed(self, row, col, value):
        if self.is_present_row(row, value) is True:
            return False
        if self.is_present_column(col, value) is True:
            return False
        if self.is_present_box(row, col, value) is True:
            return False
        return True

    def __eq__(self, other):
        if self.get_size() != other.get_size():
            return False
        for row in range(0, self._n):
            for col in range(0, self._n):
                if self._board[row][col] != other.get_board()[row][col]:
                    return False
        return True

    def __str__(self):
        result = ""
        for row in range(0, self._n):
            for col in range(0, self._n):
                result = result + str(self._board[row][col]) + " "
            result = result + "\n"
        return result

