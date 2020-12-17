# Day 3: Toboggan Trajectory

import sys

# ----------------------------------

if len(sys.argv) == 1: sys.argv.append("day03.in")

# Read forest from file (puzzle input), store as 2D array
forest = []
with open(sys.argv[1]) as f:
  for line in f:
    forest.append(list(line.strip()))
nrows = len(forest)
ncols = len(forest[0])

# Count the trees encountered when going down the forest
# following a slope that goes "dx right, dy down"
# There's no need to actually copy the array values to the right,
# one can use modulo to make the x coordinate wrap around.
def count_trees(dx, dy):
  count = 0
  x = y = 0
  while True:
    x += dx
    y += dy
    if y > nrows-1:
      break
    if forest[y][x % ncols] == "#":
      count += 1
  return count

# Part 1: count the trees for the 3 right, 1 down slope
print("Part 1:", count_trees(3, 1))

# Part 2: compute the counts for the given slopes, and multiply
# them together
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for dx, dy in slopes:
  count = count_trees(dx, dy)
  product *= count
print("Part 2:", product)
