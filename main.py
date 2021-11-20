from grid import build_grid
from pos import Pos

from bfs import bfs
from dfs import dfs


def main():
  start = Pos(0, 0)  # (x, y)
  goal = Pos(3, 3)
  walls = [
    Pos(2, 0),
    Pos(2, 1),
    Pos(2, 2),
    Pos(2, 3),
    Pos(2, 4),
    Pos(3, 4),
    Pos(4, 4),
    Pos(5, 4)
  ]

  grid = build_grid(goal, walls)

  path = dfs(start, grid)

  print(grid)
  
  
if __name__ == "__main__":
  main()
