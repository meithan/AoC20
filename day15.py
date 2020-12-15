# Day 15: Rambunctious Recitation

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  numbers = [int(x) for x in f.readline().strip().split(",")]

# ------------------------------------

# We store spoken numbers and the last turn they were spoken
spoken = {}

# Speak the initial numbers
turn = 1
for x in numbers:
  spoken[x] = turn
  last = x
  turn += 1

# Begin game
while True:

  # print("turn=", turn, "last=", last)
  if last not in spoken or spoken[last] == turn-1:
    to_speak = 0
  else:
    to_speak = (turn-1) - spoken[last]
  # print(to_speak)

  # Note that we add the number spoken on the *last* turn, not on the
  # current turn!
  spoken[last] = turn-1
  last = to_speak

  if turn == 2020:
    print("Part 1:", to_speak)

  if turn == 30000000:
    print("Part 2:", to_speak)
    break

  turn += 1
