from math import sqrt, sin, cos, radians
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

# ------------------------------------------------------------------------------

def hex_to_cart(hx, hy):
  return hx + hy/2, hy*sqrt(3)/2

def num_sign(n):
  return "0" if n == 0 else "{:+}".format(n)

def plot_hex(hx, hy, label=False):
  x,y = hex_to_cart(hx, hy)
  if (hx,hy) in [(0,0), (1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)]:
    color = "k"
    zorder = 0
  else:
    color = "0.8"
    zorder = -10
  hex = RegularPolygon((x, y), numVertices=6, radius=1/sqrt(3), facecolor="w", edgecolor=color, zorder=zorder)
  plt.gca().add_patch(hex)
  if label:
    if (hx,hy) == (0,0):
      s = "0,0"
    else:
      s = ",".join("{:+}".format(x) for x in (hx,hy))
    plt.annotate(s, xy=(x,y), fontsize=20, ha="center", va="center", color=color, zorder=10)

hexes = set()
for hx in range(-3, 3+1):
  for hy in range(-3, 3+1):
    hexes.add((hx,hy))

plt.figure(figsize=(5,5))

for hx,hy in hexes:
  plot_hex(hx, hy, True)

deltas = [(1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)]
dir_names = ["e", "ne", "nw", "w", "sw", "se"]
r1 = 0.2
r2 = 0.68
r3 = 0.43
for i in range(6):
  theta = radians(60*i)
  x1, y1 = r1*cos(theta), r1*sin(theta)
  x2, y2 = r2*cos(theta), r2*sin(theta)
  x3, y3 = r3*cos(theta), r3*sin(theta)
  plt.annotate("", xy=(x2,y2), xytext=(x1,y1), arrowprops=dict(arrowstyle="->", color="C0"))
  # s = ",".join(format(x) for x in deltas[i])
  s = dir_names[i]
  plt.annotate(s, xy=(x3,y3), ha="center", va="center", color="C0", fontsize=16, bbox=dict(pad=0, fc="white", ec="none", alpha=0.8))

L = 2
plt.xlim(-L, L)
plt.ylim(-L, L)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.subplots_adjust(bottom=0, top=1, left=0, right=1)


if "--save" in sys.argv:
  plt.savefig("day24_diagram.png")
else:
  plt.show()
