import random

from collections import deque
from copy import deepcopy
from typing import Optional
from .events import Events

class Board:

    class BoardConsts:
        NON_VISIBLE = '.'
        EMPTY_CELL = '0'
        MINE = 'M'
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

    def __init__(self, rows: int, cols: int, mines_count: int = 10, seed: Optional[int] = None):
        self._rows = rows
        self._cols = cols
        self._mines_count = mines_count
        self._visible_board = self._create_visible_board()
        self._mines_positions = self._randomly_generate_mines(seed=seed)
        self._real_board = self._precompute_adjacent_mines()

    @property
    def mines_positions(self) -> set[tuple[int, int]]:
        return self._mines_positions.copy()
    
    @property
    def visible_board(self) -> list[list[str]]:
        return self._visible_board[:]
    
    @property
    def real_board(self) -> list[list[str]]:
        return self._real_board[:]

    @property
    def size(self) -> tuple[int, int]:
        return (self._rows, self._cols)

    def _create_visible_board(self) -> list[list[str]]:
        visible_board = [[Board.BoardConsts.NON_VISIBLE for _ in range(self._cols)] for _ in range(self._rows)]
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
        
        for row in range(self._rows):
            for col in range(self._cols):
                adjacent_mines = 0
                if (row, col) in self._mines_positions:
                    real_board[row][col] = Board.BoardConsts.MINE
                    continue
                for dr, dc in Board.BoardConsts.DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self._rows and 0 <= nc < self._cols and (nr, nc) in self._mines_positions:
                        adjacent_mines += 1
                real_board[row][col] = str(adjacent_mines)
        return real_board

    def _reveal(self, row: int, col: int) -> None:
        self._visible_board[row][col] = self._real_board[row][col]

    def reveal_cell(self, row: int, col: int) -> Events | None:
        self._reveal(row, col)

        if self._real_board[row][col] == Board.BoardConsts.MINE: 
            return Events.GAME_OVER
        
        if self._real_board[row][col] != Board.BoardConsts.EMPTY_CELL:
            return None

        current_position = (row, col)
        queue = deque([current_position])
        visited = set()
        visited.add(current_position)

        while queue:
            r, c = queue.popleft()

            for dr, dc in Board.BoardConsts.DIRECTIONS:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < self._rows and 0 <= nc < self._cols \
                    and self._real_board[nr][nc] == Board.BoardConsts.EMPTY_CELL \
                    and (nr, nc) not in visited:
                    self._reveal(nr, nc)
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return None