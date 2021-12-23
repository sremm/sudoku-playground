from typing import Tuple

from sudoku.board import SudokuBoard


class SudokuSolver:
    @staticmethod
    def solve(board: SudokuBoard) -> Tuple[SudokuBoard, str]:

        return (board, "message from solver")
