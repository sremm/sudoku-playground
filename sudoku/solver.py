from typing import Tuple

import numpy as np

from sudoku.board import SudokuBoard


class SudokuSolver:
    @staticmethod
    def solve(board: SudokuBoard) -> Tuple[SudokuBoard, str]:
        """Some kind of solver algorithm"""
        message = ""
        if board.state_is_valid == False:
            result_board = board
            message = "SOLVER ERROR - Board state is invalid, cannot solve an invalid board"
        else:
            # Do the thing
            # find suitable values for all slots with missing values
            valid_values = board._allowed_numbers[1:]
            original_board_state = board.board_state_numpy()
            board_state = original_board_state.copy()

            empty_slots = np.where(board_state == 0)
            if len(empty_slots) > 0:
                row, col = empty_slots[0][0], empty_slots[0][1]
                
                for value in valid_values:
                    new_state = board_state.copy()
                    new_state[row, col] = value
                    new_board = SudokuBoard(new_state)
                    if new_board.state_is_valid == True:
                        new_board, recursion_message = SudokuSolver.solve(new_board)
                        new_state = new_board.board_state_numpy()
                        continue
                    else:
                        new_state[row,col] = 0
                    board_state = new_state
                current_board = SudokuBoard(board_state)
            else:
                current_board = SudokuBoard(board_state)
            if current_board.is_solved:
                result_board = current_board
                message = "Found a solution"
            else:
                result_board = board
                message = "Did not find a solution"

        return (result_board, message)
