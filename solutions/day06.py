# Day 6: Custom Customs

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse and separate input into groups, with the answers
# of each person a set
groups = []
with open(sys.argv[1]) as f:
  new_group = []
  for line in f:
    if line == "\n":
      groups.append(new_group)
      new_group = []
    else:
      new_group.append(set(line.strip()))
if len(new_group) > 0:
  groups.append(new_group)

# ------------------------------------

# Part 1: for each group, compute the union of the
# answers of the persons

ans1 = 0
for group in groups:
  set_union = set()
  for person in group:
    set_union = set_union | person
  ans1 += len(set_union)

print("Part 1:", ans1)

# ------------------------------------

# Part 2: for each group, compute the intersection
# of the answers of the persons

ans2 = 0
for group in groups:
  set_intersection = group[0]
  for person in group[1:]:
    set_intersection = set_intersection & person
  ans2 += len(set_intersection)

print("Part 2:", ans2)
