import numpy as np

from sudoku.board import SudokuBoard
from sudoku.solver import SudokuSolver


class TestSudokuSolver:
    def test_state_invalid(self):
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
        assert board.is_solved == False

        result_board, result_message = SudokuSolver.solve(board)
        assert "SOLVER ERROR" in result_message
        assert result_board.is_solved == False

    def test_simple_board_1_missing(self):
        board = SudokuBoard(
            np.array(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                    [9, 1, 2, 3, 4, 5, 6, 7, 0],
                ]
            )
        )
        assert board.is_solved == False

        result_board, result_message = SudokuSolver.solve(board)
        assert result_board.state_is_valid == True
        assert result_board.is_solved == True

    def test_easy_sudoku(self):
        board = SudokuBoard(
            np.array(
                [
                    [0, 0, 6, 8, 7, 1, 0, 0, 3],
                    [0, 7, 3, 0, 5, 6, 1, 9, 9],
                    [0, 0, 0, 3, 4, 9, 0, 2, 7],
                    [3, 4, 2, 0, 0, 0, 0, 8, 0],
                    [0, 6, 0, 0, 2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 3, 0, 5, 2],
                    [0, 1, 0, 7, 0, 4, 8, 0, 0],
                    [7, 0, 0, 5, 9, 8, 2, 6, 1],
                    [0, 0, 5, 0, 0, 0, 9, 0, 0],
                ]
            )
        )
        assert board.is_solved == False

        result_board, result_message = SudokuSolver.solve(board)
        assert result_board.state_is_valid == True
        assert result_board.is_solved == True
