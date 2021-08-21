import numpy as np
import pytest
from sudoku.board import BoardShapeError, SudokuBoard


class TestSudokuBoard:
    def test_wrong_shape_raises_error(self):
        with pytest.raises(BoardShapeError):
            SudokuBoard(np.ones((3, 3)))

    def test_correct_shape_raises_no_error(self):
        SudokuBoard(np.ones((9, 9)))
