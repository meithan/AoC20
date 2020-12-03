# Day 2: Password Philosophy

import sys

# ----------------------------------

if len(sys.argv) == 1: sys.argv.append("day02.in")

count1 = count2 = 0
with open(sys.argv[1]) as f:
  for line in f:

    # Split each line and parse its elements
    tokens = line.strip().split()
    a, b = [int(x) for x in tokens[0].split("-")]
    letter = tokens[1].strip(":")
    pswd = tokens[2]

    # Check the conditions for both parts
    if a <= pswd.count(letter) <= b:
      count1 += 1
    if (pswd[a-1] == letter) ^ (pswd[b-1] == letter):
      count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
