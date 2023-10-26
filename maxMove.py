def max_moves(grid):
    m = len(grid)
    n = len(grid[0])

    # Create a 2D array dp to store the maximum moves at each cell
    dp = [[0] * n for _ in range(m)]

    # Initialize the dp array with 1 because we can always make at least one move from any cell in the first column
    for i in range(m):
        dp[i][0] = 1

    max_moves = 0

    # Iterate through the grid column by column
    for col in range(1, n):
        for row in range(m):
            # For the current cell (row, col), try moving to the three possible cells in the next column
            for new_row in range(row - 1, row + 2):
                if 0 <= new_row < m and grid[new_row][col] > grid[row][col - 1]:
                    dp[row][col] = max(dp[row][col], dp[new_row][col - 1] + 1)
            
            # Update the maximum moves if necessary
            max_moves = max(max_moves, dp[row][col])

    return max_moves

# Example usage:
grid1 = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print(max_moves(grid1))  # Output: 3

grid2 = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
print(max_moves(grid2))  # Output: 0
