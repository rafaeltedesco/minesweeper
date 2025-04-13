import pytest
from game.src.core.board import Board
from game.src.core.events import Events

def should_create_visible_board_given_fixed_number_of_rows_and_cols():
    n_rows = n_cols = 3
    
    board = Board(rows=n_rows, cols=n_cols, mines_count=3, seed=42)
    
    expected_n_rows = expected_n_cols = 3
    expected_visible_board = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    
    rows, cols = board.size
    assert rows == expected_n_rows, f"expected {expected_n_rows}, but got {rows}"
    assert cols == expected_n_cols, f"expected {expected_n_cols}, but got {cols}"
    assert board.visible_board == expected_visible_board, "visible board is not equal expected visible board"


def should_randomly_generate_mines_positions_given_rows_cols_and_a_number_of_expected_mines():
    expected_positions = {(3, 8), (4, 3), (0, 0), (1, 8), (1, 0), (1, 6), (3, 2), (6, 3), (1, 3), (0, 8)}
    rows = cols = 9
    seed = 42
    board = Board(rows, cols, mines_count=10, seed=seed)
    mines_positions = board._mines_positions
    assert mines_positions == expected_positions

def should_prevent_mines_count_to_be_greather_than_fifty_percent_of_the_board_size_given_mines_count_provided():
    rows = cols = 10
    Board(rows, cols, mines_count=49)
    with pytest.raises(ValueError, match='"mine_counts" cannot be greather than 50% of the board size'):
        Board(rows, cols, mines_count=51)

def should_precompute_adjacent_mines_and_return_real_board_given_a_visible_board():
    board = Board(rows=3, cols=3, mines_count=2, seed=44)
    expected_real_board = [['0', '1', '1'], ['0', '2', 'M'], ['0', '2', 'M']]
    assert board.real_board == expected_real_board, f"expected {expected_real_board}, but got {board.real_board}"
    
def should_reveal_cell_and_dispatch_game_over_event_given_location_selected_contains_mine():
    rows = cols = 3
    board = Board(rows=rows, cols=cols, mines_count=2, seed=42)
    row, col = board.mines_positions.pop()

    event = board.reveal_cell(row, col)
    assert event == Events.GAME_OVER
    assert board.visible_board[row][col] == Board.BoardConsts.MINE