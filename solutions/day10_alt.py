# An graph-theoretic analytical solution for Day 10 Part 2

# Exploits the fact that "if A is the adjacency matrix of the directed or
# undirected graph G, then the matrix An (i.e., the matrix product of n copies
# of A) has an interesting interpretation: the element (i, j) gives the number
# of (directed or undirected) walks of length n from vertex i to vertex j."

import sys
import numpy as np

adapters = []
with open("day10.in") as f:
  for line in f:
    adapters.append(int(line.strip()))

adapters.sort()
adapters = [0] + adapters + [adapters[-1]+3]

# Build adjacency matrix
N = len(adapters)
A = np.zeros((N,N), dtype=int)
for i,x in enumerate(adapters):
  for j,y in enumerate(adapters):
    if i == j: continue
    if 1 <= (y - x) <= 3:
      A[i,j] = 1

# print(A)

# For each power A^n, the value at [0, N-1] is the number of
# distinct paths from the first to last node; add those together.
count = 0
B = A.copy()
for i in range(N-1):
  B = np.matmul(A, B)
  count += B[0,N-1]

print(count)
