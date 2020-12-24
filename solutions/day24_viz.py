from math import sqrt
import re
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from day24 import do_generation, start_blacks

# ------------------------------------------------------------------------------

def plot(blacks):

  global L

  plt.clf()

  for hx,hy in blacks:
    x = hx + hy/2
    y = hy*sqrt(3)/2
    hex = RegularPolygon((x, y), numVertices=6, radius=1/sqrt(3), facecolor="k", edgecolor='w')
    plt.gca().add_patch(hex)

  xs, ys = zip(*blacks)
  Lmax = max([abs(x) for x in xs]+[abs(y) for y in ys])
  if Lmax > L*1.08:
    # L *= 1.5
    L *= 2

  # plt.title(gen)
  plt.xlim(-L, L)
  plt.ylim(-L, L)
  # plt.axis("off")

# ----------------------------------------

blacks = start_blacks

plt.ion()
plt.show()
plt.figure(figsize=(10,10))

gen = 0
L = 30
# L = 60
plot(blacks)
plt.gca().set_aspect("equal")
plt.tight_layout()
plt.subplots_adjust(bottom=0, top=1, left=0, right=1)

for gen in range(1, 100+1):
  blacks = do_generation(blacks)
  # plot(blacks)
  # plt.pause(0.1)

plot(blacks)

if "--save" in sys.argv:
  plt.savefig("day24.png")

input("Press ENTER to exit")
