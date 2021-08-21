import numpy as np
import pytest
from sudoku.board import BoardShapeError, SudokuBoard


class TestSudokuBoard:
    def test_wrong_shape_raises_error(self):
        with pytest.raises(BoardShapeError):
            SudokuBoard(np.ones((3, 3)))

    def test_correct_shape_raises_no_error(self):
        SudokuBoard(np.ones((9, 9)))

    def test_board_state_is_valid(self):
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
                    [9, 1, 2, 3, 4, 5, 6, 7, 8],
                ]
            )
        )
        assert board.state_is_valid == True

    def test_board_state_is_invalid(self):
        board = SudokuBoard(np.ones((9, 9)))
        assert board.state_is_valid == False
