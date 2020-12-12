# Day 12: Rain Risk

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

actions = []
with open(sys.argv[1]) as f:
  for line in f:
    action = line[0]
    amount = int(line.strip()[1:])
    actions.append((action, amount))

# ------------------------------------
# Part 1

dx, dy = 1, 0
x, y = 0, 0

for action, amount in actions:
  if action == "F":
    x += dx*amount
    y += dy*amount
  elif action == "N":
    y += amount
  elif action == "S":
    y -= amount
  elif action == "E":
    x += amount
  elif action == "W":
    x -= amount
  elif action in ["L", "R"]:
    if amount == 90:
      c = 0; s = 1
    elif amount == 180:
      c = -1; s = 0
    elif amount == 270:
      c = 0; s = -1
    if action == "R":
      s *= -1
    dx, dy = dx*c - dy*s, dx*s + dy*c

ans1 = abs(x) + abs(y)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

wx, wy = 10, 1
x, y = 0, 0

for action, amount in actions:
  if action == "F":
    x += wx*amount
    y += wy*amount
  elif action == "N":
    wy += amount
  elif action == "S":
    wy -= amount
  elif action == "E":
    wx += amount
  elif action == "W":
    wx -= amount
  elif action in ["L", "R"]:
    if amount == 90:
      c = 0; s = 1
    elif amount == 180:
      c = -1; s = 0
    elif amount == 270:
      c = 0; s = -1
    if action == "R":
      s *= -1
    wx, wy = wx*c - wy*s, wx*s + wy*c

ans2 = abs(x) + abs(y)

print("Part 2:", ans2)
