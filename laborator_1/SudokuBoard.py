
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

    def get_board(self):
        return self._board

    def get_size(self):
        return self._n

    def next_empty_cell(self):
        for row in range(0, self._n):
            for col in range(0, self._n):
                if self._board[row][col] != 0:
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
        pass

    def is_allowed(self, row, col, value):
        if self.is_present_row(row, value) is True and self.is_present_column(col, value) is True and self.is_present_box(row, col, value) is True:
            return True
        return False

    def __eq__(self, other):
        if self.get_size() != other.get_size():
            return False
        for row in range(0, self._n):
            for col in range(0, self._n):
                if self._board[row][col] != other.get_board[row][col]:
                    return False
        return True

    def __str__(self):
        pass


b = SudokuBoard("board1.txt")
print(b.is_present_row(3, 2))

