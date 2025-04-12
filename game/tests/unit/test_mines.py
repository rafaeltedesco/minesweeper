from game.src.mechanics.mines import randomly_generate_mines

def should_randomly_generate_mines_positions_given_rows_cols_and_a_number_of_expected_mines():
    expected_positions = {(3, 8), (4, 3), (0, 0), (1, 8), (1, 0), (1, 6), (3, 2), (6, 3), (1, 3), (0, 8)}
    rows = cols = 9
    seed = 42
    mines_positions = randomly_generate_mines(rows, cols, mines_count=10, seed=seed)
    assert mines_positions == expected_positions