#    Main Author(s): Sukhman Hara
#    Main Reviewer(s): Preet Dineshkumar patel, Madhav Rajpal

from a1_partc import Queue

def get_number_of_neighbors(grid, row, col):
    """
    Get the number of valid neighboring cells for a given cell in the grid.

    Parameters:
    grid (list of list of int): A 2D list representing the grid.
    row (int): The row index of the cell in the grid.
    col (int): The column index of the cell in the grid.

    Returns:
    int: The number of valid neighboring cells around the specified cell.
    """
    rows, cols = len(grid), len(grid[0])
    neighbors = 0
    if row > 0:
        neighbors += 1
    if row < rows - 1:
        neighbors += 1
    if col > 0:
        neighbors += 1
    if col < cols - 1:
        neighbors += 1
    return neighbors

def get_overflow_list(grid):
    """
    Identify cells that overflow based on their values and number of neighbors.

    Parameters:
    grid (list of list of int): A 2D list representing the grid.

    Returns:
    list of tuple of int: A list of (row, col) tuples representing the overflow cells,
                          or None if no overflow cells are found.
    """
    if not grid or not grid[0]:
        return None
    overflow_cells = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if abs(grid[row][col]) >= get_number_of_neighbors(grid, row, col):
                overflow_cells.append((row, col))
    return overflow_cells if overflow_cells else None

def check_all_same_sign(grid):
    """
    Check if all non-zero cells in the grid have the same sign.

    Parameters:
    grid (list of list of int): A 2D list representing the grid.

    Returns:
    bool: True if all non-zero cells have the same sign, otherwise False.
    """
    first_nonzero = None
    for row in grid:
        for cell in row:
            if cell != 0:
                if first_nonzero is None:
                    first_nonzero = cell
                elif (cell > 0) != (first_nonzero > 0):
                    return False
    return True

def create_next_grid(grid, overflow_cells):
    """
    Create the next state of the grid after handling overflow cells.

    Parameters:
    grid (list of list of int): A 2D list representing the current grid.
    overflow_cells (list of tuple of int): A list of (row, col) tuples representing overflow cells.

    Returns:
    list of list of int: A new 2D list representing the next state of the grid after processing overflows.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]
    if not overflow_cells:
        return new_grid
    overflow_sign = 1 if grid[overflow_cells[0][0]][overflow_cells[0][1]] > 0 else -1
    neighbors_to_update = set()

    for row, col in overflow_cells:
        if row > 0: neighbors_to_update.add((row-1, col))
        if row < rows-1: neighbors_to_update.add((row+1, col))
        if col > 0: neighbors_to_update.add((row, col-1))
        if col < cols-1: neighbors_to_update.add((row, col+1))

    for row, col in overflow_cells:
        new_grid[row][col] = 0

    for row, col in neighbors_to_update:
        overflow_count = sum([(row-1, col) in overflow_cells, (row+1, col) in overflow_cells,
                              (row, col-1) in overflow_cells, (row, col+1) in overflow_cells])
        new_grid[row][col] = (abs(new_grid[row][col]) + overflow_count) * overflow_sign
    return new_grid

def overflow(grid, a_queue):
    """
    Process the grid for overflow events recursively.

    Parameters:
    grid (list of list of int): A 2D list representing the current grid.
    a_queue (Queue): A Queue instance to manage the states of the grids.

    Returns:
    int: The total number of overflow iterations that occurred during the process.
    """
    overflow_cells = get_overflow_list(grid)
    if overflow_cells is None or check_all_same_sign(grid):
        return 0
    next_grid = create_next_grid(grid, overflow_cells)
    a_queue.enqueue(next_grid)
    return 1 + overflow(next_grid, a_queue)
