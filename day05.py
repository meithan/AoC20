# Day 5: Binary Boarding

import sys

# ------------------------------------------------------------------------------

# The simple way is to actually perform the bisection process
# to find the seat's row and column
def calc_seat_ID_orig(bpass):

  row1 = 0
  row2 = 127
  for l in bpass[:7]:
    m = (row1 + row2) // 2
    if l == "F":
      row2 = m
    elif l == "B":
      row1 = m + 1
  row = row1

  col1 = 0
  col2 = 7
  for l in bpass[7:10]:
    m = (col1 + col2) // 2
    if l == "L":
      col2 = m
    elif l == "R":
      col1 = m + 1
  col = col1

  seat_ID = row*8 + col

  return seat_ID

# A smarter way is realizing this bisection process is really
# just counting in binary
def calc_seat_ID(bpass):

  bpass_bin = bpass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")

  row = int(bpass_bin[:7], 2)
  col = int(bpass_bin[7:], 2)
  seat_ID = row*8 + col

  return seat_ID

# -------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

bpasses = []
with open(sys.argv[1]) as f:
  for line in f:
    bpasses.append(line.strip())

# --------------------------------------
# Part 1

seats = set()
for bpass in bpasses:
  seat_ID_alt = calc_seat_ID(bpass)
  seats.add(seat_ID)

print("Part 1:", max(seats))

# --------------------------------------
# Part 2

for n in range(1024):
  if (n not in seats) and (n-1 in seats) and (n+1 in seats):
    my_seat = n
    break

print("Part 2:", my_seat)
