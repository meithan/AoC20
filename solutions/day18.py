# Day 18: Operation Order

import queue
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

expressions = []
with open(sys.argv[1]) as f:
  for line in f:
    expr = []
    buf = ""
    for c in line.strip():
      if c == " ":
        continue
      elif c in ("+", "*", "(", ")"):
        if buf != "":
          expr.append(int(buf))
          buf = ""
        expr.append(c)
      else:
        buf += c
    if buf != "":
      expr.append(int(buf))

    # print(line.strip()); print(expr)
    expressions.append(expr)

# ------------------------------------------------------------------------------

ops = ("+", "*")
def operate(op, arg1, arg2):
  if op == "+":
    return arg1 + arg2
  elif op == "*":
    return arg1 * arg2

def evaluate1(expr):

  result = None
  op = None
  idx = 0

  while idx < len(expr):

    token = expr[idx]
    # print(idx, token)

    if isinstance(token, int):
      if result is None:
        result = token
      else:
        result = operate(op, result, token)

    elif token in ops:
      op = token

    elif token == "(":

      count = 1
      idx2 = idx + 1
      while True:
        # print(idx2, expr[idx2])
        if expr[idx2] == "(":
          count += 1
        elif expr[idx2] == ")":
          if count == 1:
            break
          else:
            count -= 1
        idx2 += 1
      subexpr = expr[idx+1:idx2]
      # print(subexpr)
      idx = idx2
      subresult = evaluate1(subexpr)
      if result is None:
        result = subresult
      else:
        result = operate(op, result, subresult)

    idx += 1

  return result

# ------------------------------------
# Part 1

ans1 = 0
for expr in expressions:
  # print(expr, evaluate1(expr))
  ans1 += evaluate1(expr)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

def evaluate2(expr):

  # print("expr:", expr)

  if isinstance(expr, int):
    return expr

  result = None
  op = None
  idx = 0

  numbers = []
  operations = []

  idx = 0
  while idx < len(expr):

    token = expr[idx]

    if isinstance(token, int):
      numbers.append(token)

    elif token in ops:
      operations.append(token)

    elif token == "(":

      count = 1
      idx2 = idx + 1
      while True:

        if expr[idx2] == "(":
          count += 1
        elif expr[idx2] == ")":
          if count == 1:
            break
          else:
            count -= 1
        idx2 += 1
      subexpr = expr[idx+1:idx2]
      idx = idx2
      subresult = evaluate2(subexpr)
      numbers.append(subresult)

    idx += 1

  # print("numbers=",numbers)
  # print("operations=",operations)
  while len(numbers) > 1:
    N = len(operations)
    done = True
    for i in range(N):
      if operations[i] == "+":
        res = numbers[i] + numbers[i+1]
        numbers = numbers[:i] + [res] + numbers[i+2:]
        operations = operations[:i] + operations[i+1:]
        done = False
        break
    if done:
      break

  # print("new_numbers=", numbers)
  result = 1
  for n in numbers:
    result *= n
  # print("result=",result)

  return result

ans2 = 0
for expr in expressions:
  # print(expr, evaluate2(expr))
  ans2 += evaluate2(expr)

print("Part 2:", ans2)
