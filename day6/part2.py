def parse_map(filename):
    """Parse the input file and return the grid, guard position, and direction."""
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    guard_pos = None
    guard_dir = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = directions[cell]
                grid[r][c] = '.'  # Clear the guard's position in the grid

    return grid, guard_pos, guard_dir

def move_guard(grid, pos, direction):
    """Move the guard according to the rules and return the new position and direction."""
    rows, cols = len(grid), len(grid[0])
    r, c = pos
    dr, dc = direction

    # Calculate the next position
    new_r, new_c = r + dr, c + dc

    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '.':
        return (new_r, new_c), direction  # Move forward

    # Turn right if there's an obstacle
    turns = {
        (-1, 0): (0, 1),  # ^ -> >
        (1, 0): (0, -1),  # v -> <
        (0, -1): (-1, 0),  # < -> ^
        (0, 1): (1, 0),  # > -> v
    }
    return pos, turns[direction]

def simulate_patrol(grid, guard_pos, guard_dir):
    """Simulate the guard's patrol and return all visited positions."""
    visited = set()
    rows, cols = len(grid), len(grid[0])

    pos, direction = guard_pos, guard_dir
    while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        visited.add(pos)
        pos, direction = move_guard(grid, pos, direction)

    return visited

def find_loop_positions(filename):
    """Find all positions where adding an obstruction causes a loop."""
    grid, guard_pos, guard_dir = parse_map(filename)
    rows, cols = len(grid), len(grid[0])

    loop_positions = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) == guard_pos or grid[r][c] != '.':
                continue  # Skip the guard's starting position and non-empty cells

            # Place a hypothetical obstruction
            grid[r][c] = '#'

            # Check if the guard gets stuck in a loop
            visited = set()
            states = set()
            pos, direction = guard_pos, guard_dir
            is_loop = False

            while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                if (pos, direction) in states:
                    is_loop = True
                    break

                states.add((pos, direction))
                visited.add(pos)
                pos, direction = move_guard(grid, pos, direction)

            if is_loop:
                loop_positions.add((r, c))

            # Remove the hypothetical obstruction
            grid[r][c] = '.'

    return loop_positions

if __name__ == "__main__":
    input_file = "day6/input.txt"  # Replace with the path to your input file
    loop_positions = find_loop_positions(input_file)
    print("Number of loop-causing positions:", len(loop_positions))
