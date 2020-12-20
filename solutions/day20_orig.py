# Day 20: Jurassic Jigsaw

from math import sqrt
import sys

import numpy as np

# ------------------------------------------------------------------------------

class Tile:

  def __init__(self, _id, grid0):
    self.id = _id
    self.grid0 = grid0
    self.variant = 0
    self.left = None
    self.right = None
    self.top = None
    self.bottom = None

  def __repr__(self):
    return "<{}, {}>".format(self.id, self.variant)

  def get_grid(self, variant=None):
    if variant is None:
      variant = self.variant
    if variant == 0:
      return self.grid0
    g = self.grid0
    for i in range(variant % 4):
      g = np.rot90(g)
    if variant >= 4:
      g = np.fliplr(g)
    return g

  def match(self, other):

    g1 = self.get_grid()
    for variant in range(8):

      g2 = other.get_grid(variant)

      # top
      match = True
      for j in range(10):
        if g1[0,j] != g2[9,j]:
          match = False
          break
      if match:
        return ("top", variant)

      # bottom
      match = True
      for j in range(10):
        if g1[9,j] != g2[0,j]:
          match = False
          break
      if match:
        return ("bottom", variant)

      # left
      match = True
      for i in range(10):
        if g1[i,0] != g2[i,9]:
          match = False
          break
      if match:
        return ("left", variant)

      # right
      match = True
      for i in range(10):
        if g1[i,9] != g2[i,0]:
          match = False
          break
      if match:
        return ("right", variant)

    return None

  # Checks if the monster pattern is in the grid rooted at (i0,j0)
  def monster_at(self, i0, j0):
    grid = self.get_grid()
    for i,j in monster_pix:
      if grid[i0+i, j0+j] != 1:
        return False
    # Found, zero out monster pixels
    for i,j in monster_pix:
      grid[i0+i, j0+j] = 0
    return True

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

tiles = {}
with open(sys.argv[1]) as f:
  while True:
    tile_id = f.readline().strip().replace("Tile ", "").strip(":")
    if tile_id == "":
      break
    tile_id = int(tile_id)
    tile = np.zeros(shape=(10,10), dtype=int)
    for i in range(10):
      line = f.readline().strip()
      for j in range(10):
        tile[10-i-1,j] = 1 if line[j] == '#' else 0
    tiles[tile_id] = Tile(tile_id, tile)
    line = f.readline()

N = int(sqrt(len(tiles)))

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
remain = set([x for x in tiles])
image1 = [[None]*N for i in range(N)]

image1[0][0] = topleft
remain.remove(image1[0][0].id)

for ii in range(N):
  for jj in range(N):

    if ii == jj == 0:
      continue

    if jj == 0:
      tile1 = image1[ii-1][jj]
      direc = "bottom"
    elif jj > 0:
      tile1 = image1[ii][jj-1]
      direc = "right"

    found = False
    for id2 in remain:
      tile2 = tiles[id2]
      m = tile1.match(tile2)
      if m is None:
        continue
      if m[0] == direc:
        tile2.variant = m[1]
        image1[ii][jj] = tile2
        remain.remove(tile2.id)
        found = True
        break

# Remove borders and assemble actual image
grid = np.zeros(shape=(8*N,8*N), dtype=int)
for ii in range(N):
  for jj in range(N):
    g = image1[ii][jj].get_grid()
    for i in range(8):
      for j in range(8):
        x = ii*8 + i
        y = jj*8 + j
        grid[x][y] = g[1+i][1+j]
image = Tile(0, grid)

# For each variant of the image, look for the monster
for variant in range(8):
  num_monsters = 0
  image.variant = variant
  for i in range(8*N-3):
    for j in range(8*N-20):
      if image.monster_at(i, j):
        num_monsters += 1
  if num_monsters > 0:
    print("{} monsters found with variant {}".format(num_monsters, variant))
    break

# Determine how rough the waters are
roughness = np.sum(image.get_grid())

print("Part 2:", roughness)
