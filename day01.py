# Day 1: Report Repair

import sys

# =================================================

# Read input
entries = []
with open(sys.argv[1]) as f:
  for line in f:
    entries.append(int(line.strip()))

# -------------------------------------------------

# Part 1
# Just try all pairs
for x in entries:
  for y in entries[1:]:
    if x + y == 2020:
      sol1 = x * y
      break

print("Part 1:", sol1)

# -------------------------------------------------

# Part 2
# Just try all triples
for x in entries:
  for y in entries[1:]:
    for z in entries[2:]:
      if x + y + z == 2020:
        sol2 = x * y * z
        break

print("Part 2:", sol2)
