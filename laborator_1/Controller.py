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
            for board in self._problem.expand(steps[-1]):
                if board not in visited:
                    steps = steps + [board]
                    visited.append(steps[-1])
                queue.append(steps)
                steps = steps[:-1]
        return None

    def gbfs(self):
        pass

