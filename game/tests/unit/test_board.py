from game.src.mechanics.board import create_visible_board

def should_create_visible_board_given_fixed_number_of_rows_and_cols():
    n_rows = n_cols = 3
    
    visible_board = create_visible_board(rows=n_rows, cols=n_cols)
    
    expected_n_rows = expected_n_cols = 3
    expected_visible_board = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]

    rows, cols = len(visible_board), len(visible_board[0])
    
    assert rows == expected_n_rows, f"expected {expected_n_rows}, but got {rows}"
    assert cols == expected_n_cols, f"expected {expected_n_cols}, but got {cols}"
    assert visible_board == expected_visible_board, "visible board is not equal expected visible board"