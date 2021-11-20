import time

# import symbols from config.json so we don't get bugs checking different symbol values
from config.config import *
from grid import get_path


def bfs(start, grid):
  queue = [start]
  visited = {} # keep track of nodes we have visited
  parents = {} # keep track of node parents
  
  while queue:
    time.sleep(loop_delay)
    
    print(grid)

    pos = queue.pop(0)

    # Goal check
    if (grid.get(pos) == goal_symbol):
      grid.set(pos, money_symbol)
      return get_path(start, pos, parents)
    
    elif (pos not in visited):
      grid.set(pos, explored_symbol)
      visited[pos] = True

      # Add children to the bfs queue
      children = grid.get_children(pos)
      for child in children:
        if grid.get(child) == wall_symbol:
          continue

        queue.append(child)

        # Register parents to construct a path later on
        if (child not in parents):
          parents[child] = pos
