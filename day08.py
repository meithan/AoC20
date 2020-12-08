# Day 8:

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read input, parse instructions and save them as the program
program = []
with open(sys.argv[1]) as f:
  for line in f:
    op, arg = line.strip().split()
    program.append((op, int(arg)))

# Executes the given program
# Returns (exit code, accumulator value) on normal termination (exit code 0)
# or if an infinite loop is detected (exit code 1)
def exec_program(program):

  idx = 0
  acc = 0
  prev_idx = set()

  while True:

    # An infinite loop occurs if we come back to a previously
    # executed instruction (since their effect does not depend
    # on the value of the accumuator)
    if idx in prev_idx:
      # print("infinite loop!")
      return 1, acc
    else:
      prev_idx.add(idx)

    # Execution terminated successfully
    if idx == len(program):
      return 0, acc

    # Instruction to execute
    op, arg = program[idx]

    # Add to accumulator
    if op == "acc":
      acc += arg
      idx += 1

    # Jump
    elif op == "jmp":
      idx += arg

    # No operation
    elif op == "nop":
      idx += 1

# ------------------------------------
# Part 1

# Run the original program; answer is the returned value of the acccumulator
_, ans1 = exec_program(program)
print("Part 1:", ans1)

# ------------------------------------
# Part 2

# Make copies of the original program, modifying each of the instructions
# if it's a jmp or a nop. Stop when an exit code of 0 is returned.
for i in range(len(program)):

  if program[i][0] == "jmp":
    _program = program[:]
    _program[i] = ("nop", program[i][1])
    exit_code, acc = exec_program(_program)
  elif program[i][0] == "nop":
    _program = program[:]
    _program[i] = ("jmp", program[i][1])
    exit_code, acc = exec_program(_program)
  else:
    exit_code = 1

  if exit_code == 0:
    ans2 = acc
    break

print("Part 2:", ans2)
