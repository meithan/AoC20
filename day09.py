# Day 9: Encoding Error

import collections
import itertools
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

numbers = []
with open(sys.argv[1]) as f:
  for line in f:
    numbers.append(int(line.strip()))

# ------------------------------------
# Part 1

s = 25
current = collections.deque(numbers[:s])
pairs = itertools.product(current, repeat=2)
idx = s
while True:
  num = numbers[idx]
  found = False
  for a, b in pairs:
    if num == a+b:
      found = True
      current.popleft()
      current.append(num)
      pairs = itertools.product(current, repeat=2)
      idx += 1
      break
  if not found:
    ans1 = num
    break
  if idx == len(numbers):
    break

print("Part 1:", ans1)

# ------------------------------------
# Part 2

s = 2
while s <= len(numbers):

  idx = 0
  tot = sum(numbers[:s])
  found = False

  while True:
    if tot == ans1:
      found = True
      break
    if idx == len(numbers)-s:
      break
    tot -= numbers[idx]
    tot += numbers[idx+s]
    idx += 1

  if found:
    nums = sorted(numbers[idx:idx+s])
    ans2 = nums[0] + nums[-1]
    break

  s += 1

print("Part 2:", ans2)
