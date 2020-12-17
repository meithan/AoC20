# Day 13: Shuttle Search

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  earliest = int(f.readline())
  buses = f.readline().strip().split(",")

# ------------------------------------
# Part 1

numbers = [int(x) for x in buses if x != "x" ]
best_wait = 1e30
for n in numbers:
  wait = n - (earliest % n)
  if wait < best_wait:
    best_wait = wait
    best = n

ans1 = best*best_wait

print("Part 1:", ans1)

# ------------------------------------
# Part 2

numbers = []
delays = []
for d,p in enumerate(buses):
  if p != "x":
    numbers.append(int(p))
    delays.append(d)

# Finds smallest x such that a*p1 + d1 = x, b*p2 = x + d2
def offset(p1, d1, p2, d2):
  a = 1
  while True:
    x = a * p1 + d1
    if (x+d2) % p2 == 0:
      return x
    a += 1

p1 = numbers[0]
d1 = delays[0]
for i in range(1,len(numbers)):
  p2 = numbers[i]
  d2 = delays[i]
  off = offset(p1, d1, p2, d2)
  # print(p1, d1, p2, d2, off)
  p1 = p1*p2
  d1 = off

ans2 = off

print("Part 2:", ans2)

## ----------------
## Brute force! Yeah, right ... x_x
#
# def check(n, nums):
#   for p,d in zip(numbers, delays):
#     if (n+d) % p != 0:
#       return False
#   return True
#
# p0 = numbers[0]
# n0 = 100000000000000
# # n0 = 1000000
# pk = p0
# n = n0 + (pk - n0 % pk)
# while True:
#   if check(n):
#     print(n)
#     break
#   if n % 1000000 == 0:
#     print("{:,}".format(n))
#   n += pk

# # -------------------------
# # Alternative: full chinese remainder theorem >_<
#
# def modinv(a, m):
#   for x in range(1, m):
#     if x*a % m == 1:
#       return x
#
# N = 1
# for p,d in zip(numbers, delays):
#   N *= p
# x = 0
# for p,d in zip(numbers, delays):
#   y = N//p
#   z = modinv(y, p)
#   w = (p-d)%p
#   x += w*y*z
# ans2 = x % N
#
# print(ans2)
