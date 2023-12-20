#!/usr/bin/python3
"""
Module for calculating the perimeter of the island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4  # Every land cell contributes 4 sides to the perimeter

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check bottom neighbor
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check right neighbor
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

