from game.src.core.board import Board

def main():
    rows = cols = 10
    board = Board(rows=rows, cols=cols, mines_count=10, seed=40)

    board.reveal_cell(0, 6)

    print(board.visible_board)
    
if __name__ == "__main__":
    main()
