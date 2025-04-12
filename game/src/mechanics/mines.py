import random


def randomly_generate_mines(rows: int, cols: int, mines_count = 10) -> set[tuple[int, int]]:
    mines_positions = set()
    while len(mines_positions) < mines_count:
        row, col = random.randint(0, rows - 1), random.randint(0, cols -1)
        if (row, col) not in mines_positions:
            mines_positions.add((row, col))

    return mines_positions

