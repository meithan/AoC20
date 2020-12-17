# Day 7: Handy Haversacks

import re
import sys

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# ------------------------------------------------------------------------------

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

labels = {}
G = nx.DiGraph()
for bag in bags.values():
  labels[bag.color] = bag.color
  for child in bag.contents.keys():
    num = bag.contents[child]
    G.add_weighted_edges_from([(bag.color, child.color, num)])
    print("{} -> {} ({})".format(bag.color, child.color, num))

# plt.figure(figsize=(15, 15))

# nx.draw_kamada_kawai(G)
node_colors = ["red" if x == "shiny gold" else "C0" for x in G.nodes()]
pos = graphviz_layout(G, prog="neato")
nx.draw(G, pos, labels=labels, font_size=10, node_color=node_colors, arrowsize=14)
# nx.draw(G, pos, node_color=node_colors, arrowsize=12, node_size=10, edge_color=(0, 0, 0, 0.2))
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
