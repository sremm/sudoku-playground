""" Includes the definition for the game board """
import numpy as np


class BoardShapeError(Exception):
    pass


class SudokuBoard:
    _allowed_board_shape = (9, 9)
    _allowed_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # 0 represents empty box

    def __init__(self, board_state: np.ndarray):
        if board_state.shape != self._allowed_board_shape:
            raise BoardShapeError(f"Board should be of shape {self._allowed_board_shape}, but was {board_state.shape}")
        self._board_state = board_state

    def __str__(self) -> str:
        return str(self._board_state)

    @property
    def state_is_valid(self) -> bool:
        result = False
        max_sum = np.sum(self._allowed_numbers)
        # # check rows are valid

        rows_sum_within_range = np.sum(self._board_state, axis=0) <= max_sum
        rows_have_no_duplicates = []
        rows_have_only_allowed_values = []
        for idx in range(9):
            only_allowed_values = True
            no_duplicates = True
            row = self._board_state[idx, :]
            values, counts = np.unique(row, return_counts=True)
            for val in values:
                if val not in self._allowed_numbers:
                    only_allowed_values == False
                    break
            if np.all(counts == 1) == False:
                no_duplicates = False
            rows_have_only_allowed_values.append(only_allowed_values)
            rows_have_no_duplicates.append(no_duplicates)

        # # check columns are valid
        cols_sum_within_range = np.sum(self._board_state, axis=1) <= max_sum
        cols_have_no_duplicates = []
        cols_have_only_allowed_values = []
        for idx in range(9):
            only_allowed_values = True
            no_duplicates = True
            col = self._board_state[:, idx]
            values, counts = np.unique(col, return_counts=True)
            for val in values:
                if val not in self._allowed_numbers:
                    only_allowed_values == False
                    break
            if np.all(counts == 1) == False:
                no_duplicates = False
            cols_have_only_allowed_values.append(only_allowed_values)
            cols_have_no_duplicates.append(no_duplicates)

        result = bool(
            np.all(
                [
                    rows_sum_within_range,
                    rows_have_only_allowed_values,
                    rows_have_no_duplicates,
                    cols_sum_within_range,
                    cols_have_only_allowed_values,
                    cols_have_no_duplicates,
                ],
            )
        )

        return result
