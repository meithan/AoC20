# Day 1: Report Repair

# A faster solution, just because!
# Uses sets, which have O(1) membership checks on average.
# The solutions are about 100x faster!

import sys
import time

# =================================================

if len(sys.argv) == 1: sys.argv.append("day01.in")

# Read input
entries = set()
with open(sys.argv[1]) as f:
  for line in f:
    entries.add(int(line.strip()))

# -------------------------------------------------

# Part 1
# O(n) instead of O(n^2)
# This takes 4.7 microseconds vs. 3.1 milliseconds
start = time.time()
for x in entries:
  if 2020 - x in entries:
    sol1 = x * (2020 - x)
    break
end = time.time()

print("Part 1:", sol1)
print("Elapsed:", (end-start)*1e3, "ms")

# -------------------------------------------------

# Part 2
# O(n^2) instead of O(n^3)
# This takes 6.1 milliseconds vs. 671 milliseconds
start = time.time()
for x in entries:
  for y in entries:
    if x == y: continue
    if 2020 - x - y in entries:
      sol2 = x * y * (2020 - x - y)
      break
end = time.time()

print("Part 2:", sol2)
print("Elapsed:", (end-start)*1e3, "ms")
