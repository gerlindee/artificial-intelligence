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
        global board1
        global board2
        running = True
        selected_board = SudokuBoard("board1.txt")
        while running:
            self.mainMenu()
            command = input(">> ")
            if command == "0":
                running = False
            elif command == "1":
                msg_size = "\t" + "- 4x4;" + "\n"
                msg_size = msg_size + "\t" + "- 9x9;" + "\n"
                size = input("board size: " + "\n" + msg_size)

                msg_diff = "\t" + "- very easy;" + "\n"
                msg_diff = msg_diff + "\t" + "- easy;" + "\n"
                msg_diff = msg_diff + "\t" + "- medium;" + "\n"
                msg_diff = msg_diff + "\t" + "- hard;" + "\n"
                difficulty = input("difficulty: " + "\n" + msg_diff)

                if size == "4" or size == "4x4":
                    if difficulty == "very easy":
                        selected_board = SudokuBoard("board6.txt")
                    elif difficulty == "easy":
                        selected_board = SudokuBoard("board1.txt")
                    elif difficulty == "medium":
                        selected_board = SudokuBoard("board7.txt")
                    elif difficulty == "hard":
                        selected_board = SudokuBoard("board8.txt")
                    else:
                        print("Invalid input!")
                elif size == "9" or size == "9x9":
                    if difficulty == "very easy":
                        selected_board = SudokuBoard("board2.txt")
                    elif difficulty == "easy":
                        selected_board = SudokuBoard("board3.txt")
                    elif difficulty == "medium":
                        selected_board = SudokuBoard("board4.txt")
                    elif difficulty == "hard":
                        selected_board = SudokuBoard("board5.txt")
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
                pass
            else:
                print("Invalid command!")


ctrl = Controller()
ui = UI(ctrl)
ui.run()
