# Day 14: Docking Data

import re
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read input, parse instructions
program = []
with open(sys.argv[1]) as f:
  for line in f:
    if "mask" in line:
      program.append(("mask", line.split()[2]))
    elif "mem" in line:
      m = re.match("mem\[([0-9]+)\] = ([0-9]+)", line)
      program.append(("mem", int(m.group(1)), int(m.group(2))))

# ------------------------------------
# Part 1

# Runs the given program in v1
def run_program_v1(program):

  memory = {}
  mask = ""
  for inst in program:

    if inst[0] == "mem":

      # Apply mask to value
      addr, val = inst[1], inst[2]
      bits = list(bin(val)[2:].zfill(36))
      for i in range(36):
        if mask[i] == "1":
          bits[i] = "1"
        elif mask[i] == "0":
          bits[i] = "0"
      new_val = int("".join(bits), 2)

      memory[addr] = new_val

    elif inst[0] == "mask":

      # Update mask
      mask = inst[1]

  return memory

memory = run_program_v1(program)
ans1 = sum(memory.values())

print("Part 1:", ans1)

# ------------------------------------
# Part 2

# Runs the given program in v2
def run_program_v2(program):

  memory = {}
  mask = ""
  for inst in program:

    if inst[0] == "mem":

      # Apply mask to addresss
      addr, val = inst[1], inst[2]
      addr_bits = list(bin(addr)[2:].zfill(36))
      float_pos = []
      for i in range(36):
        if mask[i] == "1":
          addr_bits[i] = "1"
        elif mask[i] == "0":
          pass
        elif mask[i] == "X":
          addr_bits[i] = "X"
          float_pos.append(i)

      # Generate new addresses for all 2^N combinations of the
      # the N floating bits
      num_floating = addr_bits.count("X")
      for n in range(2**num_floating):
        new_addr_bits = [b for b in addr_bits]
        bits_repl = list(bin(n)[2:].zfill(num_floating))
        for i in range(num_floating):
          new_addr_bits[float_pos[i]] = bits_repl[i]
        new_addr = int("".join(new_addr_bits), 2)
        memory[new_addr] = val

    elif inst[0] == "mask":

      # Update mask
      mask = inst[1]

  return memory

memory = run_program_v2(program)
ans2 = sum(memory.values())

print("Part 2:", ans2)
