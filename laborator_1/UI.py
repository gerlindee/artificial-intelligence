from SudokuBoard import SudokuBoard
from Problem import Problem
from Controller import Controller


class UI:
    def __init__(self, controller):
        self._controller = controller

    @staticmethod
    def mainMenu():
        print("0. exit;")
        print("1. select game board;")
        print("2. solve using an uninformed search method (bfs);")
        print("\t" + "2.5. display the step-by-step solution;")
        print("3. solve using an informed search method (gbfs);")

    def run(self):
        running = True
        selected_board = SudokuBoard("board1.txt")
        while running:
            self.mainMenu()
            command = input(">> ")
            if command == "0":
                running = False
            elif command == "1":
                board1 = SudokuBoard("board1.txt")
                print("board 1: ")
                print(board1)
                # TODO: add more boards
                selection = input("select a board: ")
                if selection == "1" or selection == "board 1":
                    selected_board = board1
            elif command == "2":
                prbl = Problem(selected_board)
                self._controller.set_problem(prbl)
                result = self._controller.bfs()
                if result is None:
                    print("There is no solution for this Sudoku game!")
                else:
                    print(result[-1])
            elif command == "2.5":
                prbl = Problem(selected_board)
                self._controller.set_problem(prbl)
                result = self._controller.bfs()
                if result is None:
                    print("There is no solution for this Sudoku game!")
                else:
                    for step in result:
                        print(step)
            elif command == "3":
                pass
            else:
                print("Invalid command!")


ctrl = Controller()
ui = UI(ctrl)
ui.run()
