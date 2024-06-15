def max_mushrooms(F):
  """Returns the maximum number of mushrooms that Princess Sara can pick up along any quick path in the forest F."""
  # Initialize a table to store the maximum number of mushrooms that can be picked up from each grid square.
  table = [[0 for _ in range(n)] for _ in range(n)]

  # Iterate over all grid squares.
  for i in range(n):
    for j in range(n):
      # If the current grid square is empty, then the maximum number of mushrooms that can be picked up from it is 0.
      if F[i][j] == "":
        table[i][j] = 0
      # Otherwise, the maximum number of mushrooms that can be picked up from it is the maximum of the following:
      #   - The maximum number of mushrooms that can be picked up from the current grid square if it is not included in the quick path.
      #   - The maximum number of mushrooms that can be picked up from the current grid square if it is included in the quick path, plus the maximum number of mushrooms that can be picked up from any of the grid squares that can be reached from the current grid square in one step.
      else:
        table[i][j] = max(
            0,
            table[i][j],
            1 + max(table[i - 1][j], table[i][j - 1], table[i + 1][j], table[i][j + 1]))

  # Return the maximum number of mushrooms that can be picked up from the start grid square.
  return table[0][0]
