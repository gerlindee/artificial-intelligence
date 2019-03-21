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
        print("\t" + "3.5. display the step-by-step solution;")
        print("4. solve using the brutest of methods;")

    def run(self):
        running = True
        selected_board = SudokuBoard("data/board-3x3-1.txt")
        while running:
            self.mainMenu()
            command = input(">> ")
            if command == "0":
                running = False
            elif command == "1":
                msg_size = "\t" + "- 3x3" + "\n"
                msg_size = msg_size + "\t" + "- 4x4;" + "\n"
                msg_size = msg_size + "\t" + "- 9x9;" + "\n"
                size = input("board size: " + "\n" + msg_size)

                msg_diff = "\t" + "- very easy;" + "\n"
                msg_diff = msg_diff + "\t" + "- easy;" + "\n"
                msg_diff = msg_diff + "\t" + "- medium;" + "\n"
                msg_diff = msg_diff + "\t" + "- hard;" + "\n"
                difficulty = input("difficulty: " + "\n" + msg_diff)

                if size == "3" or size == "3x3":
                    if difficulty == "easy" or difficulty == "very easy":
                        selected_board = SudokuBoard("data/board-3x3-1.txt")
                    elif difficulty == "medium":
                        selected_board = SudokuBoard("data/board-3x3-2.txt")
                    elif difficulty == "hard":
                        selected_board = SudokuBoard("data/board-3x3-3.txt")
                elif size == "4" or size == "4x4":
                    if difficulty == "very easy":
                        selected_board = SudokuBoard("data/board-4x4-1.txt")
                    elif difficulty == "easy":
                        selected_board = SudokuBoard("data/board-4x4-2.txt")
                    elif difficulty == "medium":
                        selected_board = SudokuBoard("data/board-4x4-3.txt")
                    elif difficulty == "hard":
                        selected_board = SudokuBoard("data/board-4x4-4.txt")
                    else:
                        print("Invalid input!")
                elif size == "9" or size == "9x9":
                    if difficulty == "very easy":
                        selected_board = SudokuBoard("data/board-9x9-1.txt")
                    elif difficulty == "easy":
                        selected_board = SudokuBoard("data/board-9x9-2.txt")
                    elif difficulty == "medium":
                        selected_board = SudokuBoard("data/board-9x9-3.txt")
                    elif difficulty == "hard":
                        selected_board = SudokuBoard("data/board-9x9-4.txt")
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")

                print("You have selected: ")
                print(selected_board)
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
                prbl = Problem(selected_board)
                self._controller.set_problem(prbl)
                result = self._controller.gbfs()
                if result is None:
                    print("There is no solution for this Sudoku game!")
                else:
                    print(result)
            else:
                print("Invalid command!")


ctrl = Controller()
ui = UI(ctrl)
ui.run()