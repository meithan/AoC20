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

def check_rule(num, rule1, rule2):
  return (rule1[0] <= num <= rule1[1]) or (rule2[0] <= num <= rule2[1])

valid_tickets = []
invalid_numbers = []
for ticket in nearby_tickets:

  ticket_valid = True
  for num in ticket:

    is_valid = False
    for rule in rules.values():
      if check_rule(num, rule[0], rule[1]):
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

possibles = {x: set(range(N)) for x in rules}
for ticket in [my_ticket] + valid_tickets:
  for pos,num in enumerate(ticket):
    for field in rules:
      rule = rules[field]
      if not check_rule(num, rule[0], rule[1]):
        if pos in possibles[field]:
          possibles[field].remove(pos)

solutions = {}
while True:
  all_empty = True
  for field in possibles:
    if len(possibles[field]) == 0:
      continue
    elif len(possibles[field]) == 1:
      all_empty = False
      pos = possibles[field].pop()
      solutions[field] = pos
      for field1 in possibles:
        if field1 != field and pos in possibles[field1]:
          possibles[field1].remove(pos)
  if all_empty:
    break

ans2 = 1
for field in solutions:
  if field.startswith("departure"):
    pos = solutions[field]
    ans2 *= my_ticket[pos]

print("Part 2:", ans2)
