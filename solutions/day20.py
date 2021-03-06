# Day 20: Jurassic Jigsaw

from math import sqrt
import sys

import numpy as np

# ------------------------------------------------------------------------------

class Tile:

  def __init__(self, _id, grid0):
    self.id = _id
    self.variant = 0
    self.grids = self.gen_variants(grid0)

  def __repr__(self):
    return "<{}, {}>".format(self.id, self.variant)

  def show(self, variant=None):
    if variant is None:
      variant = self.variant
    for row in self.get_grid(variant):
      print(" ".join([str(x) for x in row]))

  # Generate the 8 variants (orientations) of the grid
  def gen_variants(self, grid0):
    grids = []
    grids.append(grid0)
    g = grid0
    for i in range(3):
      g = self.rotate90(g)
      grids.append(g)
    g = self.fliplr(grid0)
    grids.append(g)
    for i in range(3):
      g = self.rotate90(g)
      grids.append(g)
    return grids

  # Returns the specified variant of the grid, or the 'default' one
  def get_grid(self, variant=None):
    if variant is None:
      variant = self.variant
    return self.grids[variant]

  # Reverses the rows of the grid
  def reverse_rows(self, grid):
    N = len(grid[0])
    new_grid = []
    for row in grid:
      new_grid.append([row[len(row)-i-1] for i in range(N)])
    return new_grid

  # Reverses the column of the grid
  def reverse_cols(self, grid):
    N = len(grid[0])
    new_grid = [[None]*N for i in range(N)]
    for i in range(N):
      for j in range(N):
        new_grid[N-i-1][j] = grid[i][j]
    return new_grid

  # Transposes the grid
  def transpose(self, grid):
    N = len(grid[0])
    new_grid = [[None]*N for i in range(N)]
    for i in range(N):
      for j in range(N):
        new_grid[i][j] = grid[j][i]
    return new_grid

  # Rotates the grid counter-clockwise by 90°
  def rotate90(self, grid):
    return self.reverse_cols(self.transpose(grid))

  # Flips the grid horizontally (left-right)
  def fliplr(self, grid):
    return self.reverse_rows(grid)

  # Checks whether we can match any of the variants of 'other' tile
  # to any of the edges of this tile
  # Returns a tuple with the edge matched and the variant (of the other tile)
  def match(self, other):

    g1 = self.get_grid()
    for variant in range(8):

      g2 = other.get_grid(variant)

      # top
      match = True
      for j in range(10):
        if g1[0][j] != g2[9][j]:
          match = False
          break
      if match:
        return ("top", variant)

      # bottom
      match = True
      for j in range(10):
        if g1[9][j] != g2[0][j]:
          match = False
          break
      if match:
        return ("bottom", variant)

      # left
      match = True
      for i in range(10):
        if g1[i][0] != g2[i][9]:
          match = False
          break
      if match:
        return ("left", variant)

      # right
      match = True
      for i in range(10):
        if g1[i][9] != g2[i][0]:
          match = False
          break
      if match:
        return ("right", variant)

    return None

  # Checks if the monster pattern is in the grid rooted at (i0,j0)
  def monster_at(self, i0, j0):
    grid = self.get_grid()
    for i,j in monster_pix:
      if grid[i0+i][j0+j] != "#":
        return False
    return True

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read in input and create tiles and their variants
N = 10
tiles = {}
with open(sys.argv[1]) as f:
  while True:
    tile_id = f.readline().strip().replace("Tile ", "").strip(":")
    if tile_id == "":
      break
    tile_id = int(tile_id)
    grid = [[None]*N for i in range(N)]
    for i in range(N):
      line = f.readline().strip()
      for j in range(N):
        # Rows are reversed to have origin at bottom-left
        grid[N-i-1][j] = line[j]
    tiles[tile_id] = Tile(tile_id, grid)
    line = f.readline()

# Define monster, rawr!
monster_str = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "]
monster_pix = []
for i in range(3):
  for j in range(20):
    if monster_str[i][j] == "#":
      monster_pix.append((i,j))

# ------------------------------------
# Part 1

# Find the corners
topleft = None
corners = []
for id1 in tiles:
  tile1 = tiles[id1]
  matches = []
  for id2 in tiles:
    tile2 = tiles[id2]
    if id1 != id2:
      m = tile1.match(tile2)
      if m is not None:
        matches.append(m)
  if len(matches) == 2:
    if topleft is None:
      if sorted([matches[0][0], matches[1][0]]) == ["bottom", "right"]:
        topleft = tile1
    corners.append(tile1)

ans1 = 1
for tile in corners:
  ans1 *= tile.id

print("Part 1:", ans1)

# ------------------------------------
# Part 2

# Assemble image
N = int(sqrt(len(tiles)))
remain = set([x for x in tiles])
tile_grid = [[None]*N for i in range(N)]

tile_grid[0][0] = topleft
remain.remove(tile_grid[0][0].id)

# Assemble the image by finding matching tiles for all positions
# Starting with the corner tile, find which tile matches to its right,
# and keep finding the right-matching tile of the one before until we
# reach the other corner. Then we go down one row, find which tile matches
# below the first tile in the row above, and complete that row as we did
# with the first.
for ii in range(N):
  for jj in range(N):

    if ii == jj == 0:
      continue

    if jj == 0:
      tile1 = tile_grid[ii-1][jj]
      direc = "bottom"
    elif jj > 0:
      tile1 = tile_grid[ii][jj-1]
      direc = "right"

    found = False
    for id2 in remain:
      tile2 = tiles[id2]
      m = tile1.match(tile2)
      if m is None:
        continue
      if m[0] == direc:
        tile2.variant = m[1]
        tile_grid[ii][jj] = tile2
        remain.remove(tile2.id)
        found = True
        break

# Remove borders and assemble actual final image
grid = [[0]*(8*N) for i in range(8*N)]
for ii in range(N):
  for jj in range(N):
    g = tile_grid[ii][jj].get_grid()
    for i in range(8):
      for j in range(8):
        x = ii*8 + i
        y = jj*8 + j
        grid[x][y] = g[1+i][1+j]
image = Tile(0, grid)

# For each variant of the final image, look for the monster
for variant in range(8):
  num_monsters = 0
  image.variant = variant
  monster_coords = []
  for i in range(8*N-3):
    for j in range(8*N-20):
      if image.monster_at(i, j):
        monster_coords.append((i,j))
        num_monsters += 1
  if num_monsters > 0:
    print("{} monsters found with variant {}".format(num_monsters, variant))
    # np.savetxt("day20.npy", image.get_grid(), fmt="%d")
    # print(monster_coords)
    break

# Determine how rough the waters are
# Each monster has 15 #; we assume no overlap between monster #'s
roughness = 0
grid = image.get_grid()
for i in range(8*N):
  for j in range(8*N):
    if grid[i][j] == "#":
      roughness += 1
roughness -= num_monsters*15

print("Part 2:", roughness)
