# Day 7: Handy Haversacks

import re
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# A class for a bag of a certain color, its contents (which bags it contains)
# and its "parent bags" (which bags contain it)
class Bag:
  def __init__(self, color):
    self.color = color
    self.parents = set()
    self.contents = {}
  def __repr__(self):
    return "<{}>".format(self.color)
  def __hash__(self):
    return hash(self.color)
  def __eq__(self, other):
    return self.color == other.color
  def tot_bags(self):
    total = 0
    for bag, count in self.contents.items():
      total += count
      total += count * bag.tot_bags()
    return total

# ------------------------------------

# Read bags from the input, building a graph of relationships between them
# As a bag can have multiple parents, this is not a tree but a directed graph
bags = {}
with open(sys.argv[1]) as f:
  for line in f:
    line = line.strip()
    i = line.find("bags")
    color = line[:i-1]
    if color not in bags:
      bag = Bag(color)
      bags[color] = bag
    else:
      bag = bags[color]
    if "no other bags" in line:
      continue
    contents = line[i+13:]
    for part in contents.split(","):
      m = re.search("([0-9]+) (.+) bag", part)
      number = int(m.group(1))
      other_color = m.group(2)
      if other_color not in bags:
        other_bag = Bag(other_color)
        bags[other_color] = other_bag
      else:
        other_bag = bags[other_color]
      bag.contents[other_bag] = number
      other_bag.parents.add(bag)

    if "no other bags" in line:
      continue

# ------------------------------------
# Part 1

# Walk up the graph from the shiny gold bag, remembering all seen bags
seen = set()
to_search = [x for x in bags["shiny gold"].parents]
while len(to_search) > 0:
  bag = to_search.pop()
  if bag.color not in seen:
    seen.add(bag.color)
  for other_bag in bag.parents:
    to_search.append(other_bag)

print("Part 1:", len(seen))

# ------------------------------------
# Part 2

# Recursively compute the total number of bags contained in the shiny gold bag
tot_bags = bags["shiny gold"].tot_bags()

print("Part 2:", tot_bags)
