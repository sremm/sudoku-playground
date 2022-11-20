""" Includes the definition for the game board """
from typing import Dict

import numpy as np


class BoardShapeError(Exception):
    pass


class SudokuBoard:
    _allowed_board_shape = (9, 9)
    _allowed_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # 0 represents empty box
    _empty_field_value = 0

    def __init__(self, board_state: np.ndarray):
        if board_state.shape != self._allowed_board_shape:
            raise BoardShapeError(f"Board should be of shape {self._allowed_board_shape}, but was {board_state.shape}")
        self._board_state = board_state
        self._board_validity = self._check_board_validity()

    def __str__(self) -> str:
        return str(self._board_state)

    @property
    def num_rows(self):
        return self._allowed_board_shape[0]

    @property
    def num_cols(self):
        return self._allowed_board_shape[1]

    @property
    def _max_row_sum(self) -> int:
        return np.sum(self._allowed_numbers)

    def _check_board_validity(self) -> Dict:
        """Perform a variety of checks and update board_validity variable"""
        max_sum = self._max_row_sum
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

        ## check that all boxes are valid
        boxes_sum_within_range = []
        boxes_have_no_duplicates = []
        boxes_have_only_allowed_values = []

        num_box_rows = 3  # NOTE these are not dynamically set
        num_box_cols = 3
        for box_row_id in range(num_box_rows):
            for box_col_id in range(num_box_cols):
                only_allowed_values = True
                no_duplicates = True

                box_values = self._board_state[
                    box_row_id * num_box_rows : (box_row_id + 1) * num_box_rows,
                    box_col_id * num_box_cols : (box_col_id + 1) * num_box_cols,
                ]
                box_sum_within_range = np.sum(box_values) <= max_sum

                values, counts = np.unique(box_values, return_counts=True)
                for val in values:
                    if val not in self._allowed_numbers:
                        only_allowed_values == False
                        break
                if np.all(counts == 1) == False:
                    no_duplicates = False

                boxes_sum_within_range.append(box_sum_within_range)
                boxes_have_no_duplicates.append(no_duplicates)
                boxes_have_only_allowed_values.append(only_allowed_values)

        return {
            "rows_sum_within_range": rows_sum_within_range,
            "rows_have_no_duplicates": rows_have_no_duplicates,
            "rows_have_only_allowed_values": rows_have_only_allowed_values,
            "cols_sum_within_range": cols_sum_within_range,
            "cols_have_no_duplicates": cols_have_no_duplicates,
            "cols_have_only_allowed_values": cols_have_only_allowed_values,
            "boxes_sum_within_range": boxes_sum_within_range,
            "boxes_have_no_duplicates": boxes_have_no_duplicates,
            "boxes_have_only_allowed_values": boxes_have_only_allowed_values,
        }

    @property
    def state_is_valid(self) -> bool:
        self._board_validity = self._check_board_validity()

        result = bool(np.all(list(self._board_validity.values())))

        return result

    @property
    def is_solved(self) -> bool:
        values_sum_is_correct = np.sum(self._board_state) == (self._max_row_sum * self.num_rows)
        result = values_sum_is_correct and self.state_is_valid
        return result

    def board_state_numpy(self) -> np.ndarray:
        return self._board_state.copy()
