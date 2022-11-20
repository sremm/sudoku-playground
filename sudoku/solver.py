from typing import Tuple

from sudoku.board import SudokuBoard


class SudokuSolver:
    @staticmethod
    def solve(board: SudokuBoard) -> Tuple[SudokuBoard, str]:
        """Recursion brute force"""
        message = ""
        if board.state_is_valid == False:
            message = "SOLVER ERROR - Board state is invalid, cannot solve an invalid board"

        return (board, message)
