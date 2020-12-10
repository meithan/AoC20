# An graph-theoretic analytical solution for Day 10 Part 2

# Exploits the fact that if A is the adjacency matrix of the graph,
# then entry at (i,j) of A^n equals the number of paths of length n
# from node i to node j.

import sys
import numpy as np

adapters = []
with open("day10.in") as f:
  for line in f:
    adapters.append(int(line.strip()))

adapters.sort()
adapters = [0] + adapters + [adapters[-1]+3]

N = len(adapters)
A = np.zeros((N,N), dtype=int)
for i,x in enumerate(adapters):
  for j,y in enumerate(adapters):
    if 1 <= (y - x) <= 3:
      A[i,j] += 1

count = 0
B = A.copy()
for i in range(N-1):
  B = np.matmul(A, B)
  count += B[0,N-1]

print(count)
