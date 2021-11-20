import time

# import symbols from config.json so we don't get bugs checking different symbol values
from config.config import config
goal_symbol = config["goal_symbol"]
money_symbol = config["money_symbol"]
explored_symbol = config["explored_symbol"]
wall_symbol = config["wall_symbol"]
loop_delay = config["loop_delay"]

from grid import get_path


def dfs(start, grid):
  stack = [start]
  visited = {} # keep track of nodes we have visited
  parents = {} # keep track of node parents

  while stack:
    time.sleep(0.02)
    
    print(grid)

    pos = stack.pop(-1)

    # Goal check
    if grid.get(pos) == goal_symbol:
      grid.set(pos, money_symbol)
      return get_path(start, pos, parents)

    # Search deeper using a stack
    elif pos not in visited:
      grid.set(pos, explored_symbol)
      visited[pos] = True

      children = grid.get_children(pos)
      for child in children:
        if grid.get(child) == wall_symbol:
          continue

        if child not in visited:
          stack.append(child)

          # Record the node parent so we can construct a path later on
          if child not in parents:
            parents[child] = pos
