# Day 17: Conway Cubes

import itertools
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

orig_actives = set()
with open(sys.argv[1]) as f:
  x = y = 0
  for line in f:
    x = 0
    for c in line.strip():
      if c == "#":
        orig_actives.add((x,y))
      x += 1
    y += 1

# ------------------------------------

def gen_deltas(ndims):
  deltas = list(itertools.product((-1,0,1), repeat=ndims))
  deltas.remove((0,)*ndims)
  return deltas

def do_cycle(actives, deltas):

  new_actives = set()
  num_neighs = {}
  seeds = set()

  # Accumulate the number of neighbors of the actives in the num_neighs set
  for active in actives:
    for ds in deltas:
      neigh = tuple(active[i]+ds[i] for i in range(len(ds)))
      if neigh not in num_neighs:
        num_neighs[neigh] = 0
      num_neighs[neigh] += 1
      if num_neighs[neigh] == 3:
        seeds.add(neigh)
      elif num_neighs[neigh] == 4:
        seeds.discard(neigh)

  # See which actives remain active (if they have 2 or 3 neighbors)
  for active in actives:
    if active not in num_neighs:
      continue
    elif 2 <= num_neighs[active] <= 3:
      new_actives.add(active)

  # Activate dead cells in seed sites
  for seed in seeds:
    if seed not in actives:
      new_actives.add(seed)

  return new_actives

# ------------------------------------
# Part 1

ndims = 3
deltas = gen_deltas(ndims)

actives = set()
for coords in orig_actives:
  actives.add(coords + (0,))

print(len(actives))
for i in range(6):
  actives = do_cycle(actives, deltas)
  print(len(actives))

print("Part 1:", len(actives))

# ------------------------------------
# Part 2

ndims = 4
deltas = gen_deltas(ndims)

actives = set()
for coords in orig_actives:
  actives.add(coords + (0,0))

print(len(actives))
for i in range(6):
  actives = do_cycle(actives, deltas)
  print(len(actives))

print("Part 1:", len(actives))
