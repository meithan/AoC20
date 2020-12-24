# Day 24: Lobby Layout

import re
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

inst_lists = []
with open(sys.argv[1]) as f:
  for line in f:
    inst_lists.append(re.findall("(e|w|nw|ne|sw|se)", line.strip()))

# ------------------------------------
# Part 1

def walk(inst_list):
  x = y = 0
  for inst in inst_list:
    if inst == "e":
      x += 1
    elif inst == "w":
      x -= 1
    elif inst == "ne":
      y += 1
    elif inst == "sw":
      y -= 1
    elif inst == "nw":
      x -= 1
      y += 1
    elif inst == "se":
      x += 1
      y -= 1
  return (x, y)

# ------------------------------------

blacks = set()
for inst_list in inst_lists:
  pos = walk(inst_list)
  if pos in blacks:
    blacks.remove(pos)
  else:
    blacks.add(pos)
start_blacks = blacks.copy()

ans1 = len(blacks)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

deltas = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)]

def do_generation(blacks):

  new_blacks = set()

  neighs = {}
  seeds = set()
  for x, y in blacks:
    for dx, dy in deltas:
      pos = (x+dx, y+dy)
      if pos not in neighs:
        neighs[pos] = 0
      neighs[pos] += 1
      if neighs[pos] == 2:
        seeds.add(pos)
      if neighs[pos] == 3:
        seeds.remove(pos)

  for pos in blacks:
    if neighs.get(pos, 0) in (1,2):
      new_blacks.add(pos)

  for pos in seeds:
    if neighs.get(pos, 0) == 2:
      new_blacks.add(pos)

  return new_blacks

# ------------------------------------

for i in range(1, 100+1):
  blacks = do_generation(blacks)

ans2 = len(blacks)

print("Part 2:", ans2)
