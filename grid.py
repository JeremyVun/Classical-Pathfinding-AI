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

  ###
  # Implement get_children(pos) function
  ###

  # Overload for printing
  def __str__(self):
    result = ''.join([f"{row}\n" for row in self.grid])
    result += "\n" * 14
    return result

###
# Implement get_path(start, goal, parents) function
###

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