import sys

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# ------------------------------------------------------------------------------

adapters = []
with open(sys.argv[1]) as f:
  for line in f:
    adapters.append(int(line.strip()))
adapters.sort()
device = adapters[-1]+3
adapters = [0] + adapters + [device]

labels = {}
G = nx.DiGraph()
for a in adapters:
  labels[a] = a
  reachable = [x for x in adapters if 1 <= x-a <= 3]
  for b in reachable:
    G.add_edge(a, b)

# plt.figure(figsize=(15, 15))

# nx.draw_kamada_kawai(G)
# node_colors = ["red" if x == "shiny gold" else "C0" for x in G.nodes()]
pos = graphviz_layout(G, prog="neato")
print(pos)
nx.draw(G, pos, labels=labels, font_color="white", font_size=10, arrowsize=14)
# nx.draw(G, pos, node_color=node_colors, arrowsize=12, node_size=10, edge_color=(0, 0, 0, 0.2))
# edge_labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

if "--save" in sys.argv:
  plt.savefig("day10_viz.svg")
else:
  plt.show()
