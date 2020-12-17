# Day 17: Conway Cubes

import copy
import sys

import numpy as np

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

N = 30
cubes = np.zeros((N, N, N), dtype=int)
with open(sys.argv[1]) as f:
  x0 = y0 = z0 = 0
  for line in f:
    x0 = 0
    for c in line.strip():
      x, y, z = x0+N//2-1, y0+N//2-1, z0+N//2-1
      cubes[z,y,x] = (1 if c == "#" else 0)
      x0 += 1
    y0 += 1

# ------------------------------------
# Part 1

deltas = list(((x,y,z) for x in (-1,0,1) for y in (-1,0,1) for z in (-1,0,1) if not (x == 0 and y == 0 and z == 0)))

def do_cycle(cubes):

  new_cubes = np.copy(cubes)

  for i in range(N):
    for j in range(N):
      for k in range(N):

        num_active = 0
        for di, dj, dk in deltas:
          ni = i + di; nj = j + dj; nk = k + dk
          if 0 <= ni < N and 0 <= nj < N and 0 <= nk < N:
            if cubes[ni,nj,nk] == 1:
              num_active += 1

        # print(i, j, k, num_occupied)

        if cubes[i,j,k] == 1:

          if 2 <= num_active <= 3:
            new_cubes[i,j,k] = 1
          else:
            new_cubes[i,j,k] = 0

        elif cubes[i,j,k] == 0:

          if num_active == 3:
            new_cubes[i,j,k] = 1
          else:
            new_cubes[i,j,k] = 0

  return new_cubes

print(np.sum(cubes))
for i in range(6):
  cubes = do_cycle(cubes)
  print(np.sum(cubes))

print("Part 1:", np.sum(cubes))

# ------------------------------------
# Part 2

N = 30
cubes = np.zeros((N, N, N, N), dtype=int)
with open(sys.argv[1]) as f:
  x0 = y0 = z0 = w0 = 0
  for line in f:
    y0 = 0
    for c in line.strip():
      x, y, z, w = x0+N//2-1, y0+N//2-1, z0+N//2-1, w0+N//2-1
      if c == "#":
        cubes[x,y,z,w] = 1
      y0 += 1
    x0 += 1

deltas = [(x,y,z,w) for x in (-1,0,1) for y in (-1,0,1) for z in (-1,0,1) for w in (-1,0,1) if not (x == 0 and y == 0 and z == 0 and w == 0)]

def do_cycle(cubes):

  new_cubes = np.copy(cubes)

  for i in range(N):
    for j in range(N):
      for k in range(N):
        for l in range(N):

          num_active = 0
          for di, dj, dk, dl in deltas:
            ni = i + di; nj = j + dj; nk = k + dk; nl = l + dl
            if 0 <= ni < N and 0 <= nj < N and 0 <= nk < N and 0 <= nl < N:
              if cubes[ni,nj,nk,nl] == 1:
                num_active += 1

          if cubes[i,j,k,l] == 1:

            if 2 <= num_active <= 3:
              new_cubes[i,j,k,l] = 1
            else:
              new_cubes[i,j,k,l] = 0

          elif cubes[i,j,k,l] == 0:

            if num_active == 3:
              new_cubes[i,j,k,l] = 1
            else:
              new_cubes[i,j,k,l] = 0

  return new_cubes

print(np.sum(cubes))
for i in range(6):
  cubes = do_cycle(cubes)
  print(np.sum(cubes))

print("Part 2:", np.sum(cubes))
