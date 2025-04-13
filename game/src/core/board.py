import random
from copy import deepcopy
from typing import Optional


class Board:

    def __init__(self, rows: int, cols: int, mines_count: int = 10, seed: Optional[int] = None):
        self._rows = rows
        self._cols = cols
        self._mines_count = mines_count
        self._visible_board = self._create_visible_board()
        self._mines_positions = self._randomly_generate_mines(seed=seed)
        self._real_board = self._precompute_adjacent_mines()

    @property
    def mines_positions(self) -> set[tuple[int, int]]:
        return self._mines_positions
    
    @property
    def visible_board(self) -> list[list[str]]:
        return self._visible_board[:]
    
    @property
    def real_board(self) -> list[list[str]]:
        return self._real_board

    @property
    def size(self) -> tuple[int, int]:
        return (self._rows, self._cols)

    def _create_visible_board(self) -> list[list[str]]:
        visible_board = [['.' for _ in range(self._cols)] for _ in range(self._rows)]
        return visible_board
    
    def _randomly_generate_mines(self, seed: Optional[int] = None) -> set[tuple[int, int]]:
        if self._mines_count > (self._rows * self._cols) // 2:
            raise ValueError('"mine_counts" cannot be greather than 50% of the board size')

        if seed is not None:
            random.seed(seed)

        mines_positions = set()
        while len(mines_positions) < self._mines_count:
            row, col = random.randint(0, self._rows - 1), random.randint(0, self._cols -1)
            if (row, col) not in mines_positions:
                mines_positions.add((row, col))

        return mines_positions

    def _precompute_adjacent_mines(self) -> list[list[str]]:
        """
            Given a visible board, it will precompute all adjacent mines and returns the real board
        """
        real_board = deepcopy(self._visible_board)
        directions = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
        for row in range(self._rows):
            for col in range(self._cols):
                adjacent_mines = 0
                if (row, col) in self._mines_positions:
                    real_board[row][col] = "M"
                    continue
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self._rows and 0 <= nc < self._cols and (nr, nc) in self._mines_positions:
                        adjacent_mines += 1
                real_board[row][col] = str(adjacent_mines)
        return real_board
