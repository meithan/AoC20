# Day 25: Combo Breaker

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  card_key = int(f.readline().strip())
  door_key = int(f.readline().strip())

# ------------------------------------
# Part 1

# This basically computes the modular exponentiation
# number ^ loop_size (mod 20201227)
# by repeated multiplication ... not very fast!
def transform(number, loop_size):
  p = 20201227
  x = 1
  for i in range(loop_size):
    x = (x*number) % p
  return x

# Finds the loop_size s such that 7^s = pkey (modulo 20201227),
# i.e. compute the discrete logarithm base 7 of pkey modulo 20201227.
# We do this by brute-force: check 7^1, 7^2, 7^3, etc. Since the order of
# the multiplicative group of integers modulo p is p-1 when p is a prime,
# we need to check at most p-1 values. This would be completely impractical
# if p were a very large (hundreds of digits) prime!
def find_loop_size(pkey):
  p = 20201227
  x = 1
  loop_size = 1
  for i in range(p-1):
    x = (7*x) % p
    if x == pkey:
      return loop_size
    else:
      loop_size += 1

# Finds the encryption key given the card and door public keys.
# Basically breaks the Diffie-Hellman protocol, i.e. finds g^(a*b) (mod p)
# when given g^a (mod p) and g^b (mod p), with g = 7, p = 20201227.
# Don't try this with a very large p!
def break_encryption(card_key, door_key):
  card_loop_size = find_loop_size(card_key)
  enc_key = transform(door_key, card_loop_size)
  return enc_key

ans1 = break_encryption(card_key, door_key)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

# No Part 2 for Day 25!
