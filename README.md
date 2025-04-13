# Minesweeper

Minesweeper is a Python implementation of the classic Minesweeper game. This project provides a programmatic way to create and interact with a Minesweeper board, including features like revealing cells, handling mines, and computing adjacent mine counts.

## Features

- Create a Minesweeper board with customizable dimensions and mine count.
- Reveal cells and handle game-over scenarios when a mine is revealed.
- Automatically reveal empty cells and their neighbors.
- Precompute adjacent mine counts for efficient gameplay.
- Unit tests to ensure the correctness of the implementation.

## Requirements

- Python 3.11 or higher
- [uv](https://github.com/tonybaloney/uv) package manager

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/minesweeper.git
   cd minesweeper
   ```

2. Install dependencies using `uv`:
   ```sh
   uv install
   ```

3. (Optional) Install development dependencies for testing and linting:
   ```sh
   uv install --dev
   ```

## Usage Example

Run the game by executing the `main.py` file:
```sh
python main.py
```

This will create a 10x10 Minesweeper board with 10 mines and reveal a sample cell.

## Project Structure

```
.
├── main.py                # Entry point for the game
├── game/
│   ├── src/
│   │   ├── core/
│   │   │   ├── board.py   # Core logic for the Minesweeper board
│   │   │   ├── events.py  # Event definitions
│   ├── tests/
│   │   ├── unit/          # Unit tests for the game logic
├── pyproject.toml         # Project configuration
├── README.md              # Project documentation
├── uv.lock                # Dependency lock file
```

## Running Tests

To run the unit tests, use the following command:
```sh
uv run pytest
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.