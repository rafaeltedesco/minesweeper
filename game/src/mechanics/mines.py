import random
from copy import deepcopy
from typing import Optional


def randomly_generate_mines(rows: int, cols: int, mines_count = 10, seed: Optional[int] = None) -> set[tuple[int, int]]:
    if mines_count > (rows * cols) // 2:
        raise ValueError('"mines_count" cannot be greater than 50% of the board size')

    if seed is not None:
        random.seed(seed)

    mines_positions = set()
    while len(mines_positions) < mines_count:
        row, col = random.randint(0, rows - 1), random.randint(0, cols -1)
        if (row, col) not in mines_positions:
            mines_positions.add((row, col))

    return mines_positions

def precompute_adjacent_mines(visible_board: list[list[str]], mines_positions: set[tuple[int, int]]) -> list[list[str]]:
    """
        Given a visible board, it will precompute all adjacent mines and returns the real board
    """
    rows, cols = len(visible_board), len(visible_board[0])
    real_board = deepcopy(visible_board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
    for row in range(rows):
        for col in range(cols):
            adjacent_mines = 0
            if (row, col) in mines_positions:
                real_board[row][col] = "M"
                continue
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) in mines_positions:
                    adjacent_mines += 1
            real_board[row][col] = str(adjacent_mines)
    return real_board
