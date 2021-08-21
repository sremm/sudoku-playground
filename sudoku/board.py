""" Includes the definition for the game board """
import numpy as np


class BoardShapeError(Exception):
    pass


class SudokuBoard:
    def __init__(self, board_state: np.ndarray):
        if board_state.shape != (9, 9):
            raise BoardShapeError(f"Board should be of shape (9, 9), but was {board_state.shape}")
        self._board_state = board_state

    def __str__(self) -> str:
        pass
