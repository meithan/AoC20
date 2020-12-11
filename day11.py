# Day 11: Seating System

import copy
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Load grid from input
orig_grid = []
with open(sys.argv[1]) as f:
  for line in f:
    orig_grid.append(list(line.strip()))

# We keep orig_grid intact
grid = copy.deepcopy(orig_grid)

NX = len(grid)
NY = len(grid[0])

def show_grid(grid):
  print()
  for row in grid:
    print("".join(row))

# ------------------------------------
# Part 1

# Advances the grid by one step, with rules for Part 1
# Just check how many neighbors each cell has and apply the rules
# Note that we create a new grid instead of overwriting the previous one
def step_part1(grid):

  new_grid = [[""]*NY for _ in range(NX)]
  for i in range(NX):
    for j in range(NY):

      num_occupied = 0
      for di in [-1, 0, +1]:
        for dj in [-1, 0, +1]:
          if di != 0 or dj != 0:
            ni = i + di; nj = j + dj
            if 0 <= ni < NX and 0 <= nj < NY:
              if grid[ni][nj] == "#":
                num_occupied += 1

      if grid[i][j] == "L" and num_occupied == 0:
        new_grid[i][j] = "#"

      elif grid[i][j] == "#" and num_occupied >= 4:
        new_grid[i][j] = "L"

      else:
        new_grid[i][j] = grid[i][j]

  return new_grid

# Keep evolving the grid until the grid stops changing
while True:
  new_grid = step_part1(grid)
  if new_grid == grid:
    break
  grid = new_grid

# Count how many occupied seats are in the final grid
count1 = 0
for i in range(NX):
  for j in range(NY):
      if grid[i][j] == "#":
        count1 += 1

print("Part 1:", count1)

# ------------------------------------
# Part 2

# For Part 2, we have to look for seats (both occupied and unoccupied) in
# lines "radiating out" of the seat under analysis (in the eight directions)
def step_part2(grid):

  new_grid = [[""]*NY for _ in range(NX)]
  for i in range(NX):
    for j in range(NY):

      num_occupied = 0
      for di, dj in [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        ni = i + di
        nj = j + dj
        while 0 <= ni < NX and 0 <= nj < NY:
          if grid[ni][nj] == "L":
            break
          elif grid[ni][nj] == "#":
            num_occupied += 1
            break
          ni += di; nj += dj

      if grid[i][j] == "L" and num_occupied == 0:
        new_grid[i][j] = "#"

      elif grid[i][j] == "#" and num_occupied >= 5:
        new_grid[i][j] = "L"

      else:
        new_grid[i][j] = grid[i][j]

  return new_grid

# Be sure to start from the original grid
grid = copy.deepcopy(orig_grid)

# Iterate until stability
while True:
  new_grid = step_part2(grid)
  if new_grid == grid:
    break
  grid = new_grid

# Count occupied seats
count2 = 0
for i in range(NX):
  for j in range(NY):
      if grid[i][j] == "#":
        count2 += 1

print("Part 2:", count2)
