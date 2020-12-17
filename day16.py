# Day 16: Ticket Translation

import re
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

rules = {}
my_ticket = None
nearby_tickets = []

with open(sys.argv[1]) as f:
  line = " "
  while line != "":

    line = f.readline()

    if line == "\n":
      continue

    if "your ticket" in line:
      line = f.readline()
      my_ticket = [int(x) for x in line.strip().split(",")]

    elif "nearby tickets" in line:
      while True:
        line = f.readline()
        if line == "":
          break
        ticket = [int(x) for x in line.strip().split(",")]
        nearby_tickets.append(ticket)
      break

    else:

      tokens = line.strip().split(":")
      field = tokens[0].strip()
      m = re.search("([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", tokens[1])
      rule1 = (int(m.group(1)), int(m.group(2)))
      rule2 = (int(m.group(3)), int(m.group(4)))
      rules[field] = (rule1, rule2)

# print(rules)
# print(my_ticket)
# print(nearby_tickets)

# ------------------------------------
# Part 1

def satisfies(num, rule):
  return (rule[0][0] <= num <= rule[0][1]) or (rule[1][0] <= num <= rule[1][1])

valid_tickets = []
invalid_numbers = []
for ticket in nearby_tickets:

  ticket_valid = True
  for num in ticket:

    is_valid = False
    for rule in rules.values():
      if satisfies(num, rule):
        is_valid = True
        break

    if not is_valid:
      invalid_numbers.append(num)
      ticket_valid = False

  if ticket_valid:
    valid_tickets.append(ticket)

ans1 = sum(invalid_numbers)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

N = len(my_ticket)

# All fields start with all positions markes as possible
possibles = {x: set(range(N)) for x in rules}

# The (valid) "nearby_tickets" had enough info to solve it, but doesn't hurt
tickets = [my_ticket] + valid_tickets

# Check all numbers in all tickets repeatedly
while True:
  for ticket in tickets:
    for pos, num in enumerate(ticket):

      # Check if this number violates any rule; if it does, remove its
      # position from that field's possibilities
      for field in possibles:
        if not satisfies(num, rules[field]):
          possibles[field].discard(pos)

      # Now check if any field has been reduced to a single possibility;
      # if so, remove its position from all other fields
      for field in possibles:
        if len(possibles[field]) == 1:
          pos = list(possibles[field])[0]
          for field1 in possibles:
            if field1 != field:
              possibles[field1].discard(pos)

  # Stop when all fields have been narrowed down to a single possibility
  if all([len(x) == 1 for x in possibles.values()]):
    break

# Compute the product of the numbers in my ticket for fields starting
# with 'departure'
ans2 = 1
for field in possibles:
  if field.startswith("departure"):
    pos = list(possibles[field])[0]
    ans2 *= my_ticket[pos]

print("Part 2:", ans2)
