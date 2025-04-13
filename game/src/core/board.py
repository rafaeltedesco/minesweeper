def create_visible_board(rows: int, cols: int) -> list[list[str]]:
    visible_board = [['.' for _ in range(cols)] for _ in range(rows)]
    return visible_board