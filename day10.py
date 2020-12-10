# Day 10: Adapter Array

from collections import deque
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

adapters = []
with open(sys.argv[1]) as f:
  for line in f:
    adapters.append(int(line.strip()))

# ------------------------------------
# Part 1

adapters.sort()
device = adapters[-1]+3

diffs = []
joltage = 0
idx = 0
while idx < len(adapters):
  j = adapters[idx]
  diffs.append(j-joltage)
  joltage = j
  idx += 1
diffs.append(3)

ones = diffs.count(1)
threes = diffs.count(3)

print("Part 1:", ones*threes)

# ------------------------------------
# Part 2

adapters = [0] + adapters + [device]

## Divide and conquer brute force!

# Split the problem into smaller sub-problems
sub_problems = []
j = 0
for i in range(len(adapters)-1):
  if adapters[i+1] - adapters[i] == 3:
    sub_problems.append(adapters[j:i+1])
    j = i + 1
sub_problems.append([device])
# print(sub_problems)

# Finds all paths between the first and last adapter
# using breadth-first search
def find_paths(_adapters):

  start = _adapters[0]
  goal = _adapters[-1]
  to_check = deque([(start,)])
  paths = []
  while len(to_check) > 0:
    path = to_check.popleft()
    if path[-1] == goal:
      paths.append(path)
      continue
    reachable = [x for x in _adapters if 1 <= x-path[-1] <= 3]
    for adap in reachable:
      new_path = path + (adap,)
      to_check.append(new_path)

  return(paths)

# Count the number of paths in each sub-problem, multiply them all
count = 1
for sub_problem in sub_problems:
  num = len(find_paths(sub_problem))
  count *= num

print("Part 2:", count)
