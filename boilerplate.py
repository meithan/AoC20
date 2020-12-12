#

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  for line in f:
    pass

# ------------------------------------
# Part 1



ans1 = 0

print("Part 1:", ans1)

# ------------------------------------
# Part 2



ans2 = 0

print("Part 2:", ans2)
