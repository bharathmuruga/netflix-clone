def display_board(board):
  """Displays the current state of the Tic Tac Toe board."""
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def is_valid_move(board, row, col):
  """Checks if a move is valid (empty cell)."""
  return board[row][col] == ' '

def make_move(board, player, row, col):
  """Places the player's symbol (X or O) on the board."""
  board[row][col] = player

def has_won(board, player):
  """Checks if a player has won (3 in a row)."""
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True
  
  # Check columns
  for col in range(len(board[0])):
    if all(board[row][col] == player for row in range(len(board))):
      return True
  
  # Check diagonals
  if all(board[i][i] == player for i in range(len(board))):
    return True
  if all(board[i][len(board)-i-1] == player for i in range(len(board))):
    return True
  
  # No winner yet
  return False

def is_board_full(board):
  """Checks if all cells on the board are occupied."""
  for row in board:
    for cell in row:
      if cell == ' ':
        return False
  return True

def main():
  """Main function to run the Tic Tac Toe game."""
  board = [[' ' for _ in range(3)] for _ in range(3)]  # Create a 3x3 board
  current_player = 'X'  # X starts first

  while True:
    display_board(board)
    
    # Get player input
    row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
    col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
    
    # Validate move
    if not is_valid_move(board, row, col):
      print("Invalid move. Please choose an empty cell.")
      continue

    # Make the move
    make_move(board, current_player, row, col)

    # Check for winner or tie
    if has_won(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      break
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  main()
