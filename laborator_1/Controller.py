import time


class Controller:
    def __init__(self):
        self._problem = None

    def set_problem(self, problem):
        self._problem = problem

    def bfs(self):
        visited = [self._problem.sudoku_board()]
        queue = [[self._problem.sudoku_board()]]
        while len(queue) > 0:
            steps = queue.pop(0)
            if self._problem.is_solution(steps[-1]):
                return steps
            row, column = steps[-1].next_empty_cell()
            for board in self._problem.expand(steps[-1], row, column):
                if board not in visited:
                    steps = steps + [board]
                    visited.append(steps[-1])
                queue.append(steps)
                steps = steps[:-1]
        return None

    def gbfs(self):
        visited = []
        queue = [self._problem.sudoku_board()]
        while len(queue) > 0:
            steps = queue.pop(0)
            visited = visited + [steps]
            if self._problem.is_solution(steps):
                return steps
            empty_positions = steps.all_empty_cells()
            aux = [[x, self._problem.heuristic(steps, x[0], x[1])] for x in empty_positions]
            aux.sort(key=lambda v: v[1])
            empty_positions = [x[0] for x in aux]
            for [i, j] in empty_positions:
                for board in self._problem.expand(steps, i, j):
                    if board not in visited:
                        queue.append(board)
        return None



