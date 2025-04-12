import pytest
from game.src.mechanics.mines import randomly_generate_mines, precompute_adjacent_mines

def should_randomly_generate_mines_positions_given_rows_cols_and_a_number_of_expected_mines():
    expected_positions = {(3, 8), (4, 3), (0, 0), (1, 8), (1, 0), (1, 6), (3, 2), (6, 3), (1, 3), (0, 8)}
    rows = cols = 9
    seed = 42
    mines_positions = randomly_generate_mines(rows, cols, mines_count=10, seed=seed)
    assert mines_positions == expected_positions

def should_prevent_mines_count_to_be_greather_than_fifty_percent_of_the_board_size_given_mines_count_provided():
    rows = cols = 10
    randomly_generate_mines(rows, cols, 49)
    with pytest.raises(ValueError, match='"mine_counts" cannot be greather than 50% of the board size'):
        randomly_generate_mines(rows, cols, mines_count=51)

def should_precompute_adjacent_mines_and_return_real_board_given_a_visible_board():
    visible_board = [
        ['.', 'M', '.'],
        ['.', '.', '.'],
        ['.', '.', 'M']
    ]
    mines_positions = set([(0, 1), (2, 2)])
    real_board = precompute_adjacent_mines(visible_board, mines_positions)

    expected_real_board = [['1', 'M', '1'], ['1', '2', '2'], ['0', '1', 'M']]
    
    assert real_board == expected_real_board, f"expected {expected_real_board}, but got {real_board}"
