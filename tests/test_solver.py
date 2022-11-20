import numpy as np

from sudoku.board import SudokuBoard
from sudoku.solver import SudokuSolver


class TestSudokuSolver:
    def test_simple_board_1_missing(self):
        board = SudokuBoard(
            np.array(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [9, 1, 2, 3, 4, 5, 6, 7, 0],
                ]
            )
        )
        result_board, result_message = SudokuSolver.solve(board)
        assert result_board.state_is_valid == True
        assert result_board.is_solved == True
