# import symbols from config.json so we don't get bugs checking different symbol values
from config.config import config
unexplored_symbol = config["unexplored_symbol"]
goal_symbol = config["goal_symbol"]
wall_symbol = config["wall_symbol"]


class Grid:
  def __init__(self, grid):
    self.grid = grid
    self.width = len(grid[0])
    self.height = len(grid)

  def set(self, pos, value):
    self.grid[pos.y][pos.x] = value

  def get(self, pos):
    return self.grid[pos.y][pos.x]

  ####
  # STUDENTS TO IMPLEMENT THIS FUNCTION
  ####
  def get_children(self, pos):
    children = []

    # Get child to the right
    if pos.x < self.width - 1:
      child = pos.clone().move(1, 0)
      children.append(child)

    # Get child to the left
    if pos.x > 0:
      child = pos.clone().move(-1, 0)
      children.append(child)

    # Get child above us
    if pos.y < self.height - 1:
      child = pos.clone().move(0, +1)
      children.append(child)

    # Get child below us
    if pos.y > 0:
      child = pos.clone().move(0, -1)
      children.append(child)
    
    return children

  # Overload for printing
  def __str__(self):
    result = ''.join([f"{row}\n" for row in self.grid])
    result += "\n" * 14
    return result

####
# STUDENTS TO IMPLEMENT THIS FUNCTION
####
def get_path(start, end, parents):
  path = []
  
  current_square = end
  while (current_square != start):
    parent_square = parents[current_square]
    path.insert(0, parent_square)
    current_square = parent_square
    
  return path


# Builds the grid
def build_grid(goal, walls):
  width = config["window_width"]
  height = config["window_height"]

  grid = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(unexplored_symbol)
    
    grid.append(row)

  result = Grid(grid)
  result.set(goal, goal_symbol)

  for wall in walls:
    result.set(wall, wall_symbol)

  return result