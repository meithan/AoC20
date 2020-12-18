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
    expressions.append(expr)

# ------------------------------------------------------------------------------

valid_operators = ("+", "*")

def apply(op, arg1, arg2):
  if op == "+":
    return arg1 + arg2
  elif op == "*":
    return arg1 * arg2

def evaluate(expr, precedence_rules):

  RPN = queue.Queue()
  operators = []

  for token in expr:

    # print("token:", repr(token))

    # Numbers we just add to the queue
    if isinstance(token, int):

      RPN.put(token)
      # print("number added to queue:", token)

    # Operators
    elif token in valid_operators:

      if len(operators) == 0:

        # Just push the operator to the stack
        # print("operator added to stack:", token)
        operators.append(token)

      else:

        # If the last operator on top of the stack is an opening parens, we
        # just push the new op to the stack (regardless of what op came before
        # the parens).
        # Otherwise, we compare the precedence of the new operator with that
        # of on top of the stack:
        # - New op has greater precedence: we just push it to the stack.
        # - New op has lower precedence: we pop the last op from the stack
        #   and add it to the queue; then we push the new op to the stack.
        # - Equal precedence: if the operators are applied from left to
        #   right, then we treat the new op as having lower precedence (since
        #   we would apply it later as it is to the right of the last op), so
        #   we pop the last op from the stack and add it to the queue before
        #   pushing the new op to the stack. For right-to-left evaluation we
        #   would do the opposite.
        last_op = operators[-1]
        if last_op == "(":
          operators.append(token)
        else:
          if precedence_rules[token] <= precedence_rules[last_op]:
            last_op = operators.pop()
            RPN.put(last_op)
            # print("{} has lower or equal precedence than {}".format(token, last_op))
            # print("{} removed from stack and added to queue".format(last_op))
          else:
            # print("{} has higher precedence than {}".format(token, last_op))
            pass
          operators.append(token)
        # print("operator added to stack:", token)

    elif token == "(":

      # When an opening parens is encountered we push it to the stack
      operators.append("(")
      # print("parens added to stack")

    elif token == ")":

      # When a closing parens is encountered, we push operators from the
      # stack and add them to the queue until we encounter a matching
      # opening parens, and then stop.
      # print("Popping operators from stack and pushing them to queue:")
      while True:
        op = operators.pop()
        if op == "(":
          break
        else:
          RPN.put(op)
          # print(op)

  # print("partial RPN:", list(RPN.queue))
  # print("remaining ops:", operators)

  # After we've gone through all the tokens, we successively pop all
  # operators left on the stack and add them to the queue
  while len(operators) > 0:
    op = operators.pop()
    if op != "(":
      RPN.put(op)

  # print("final RPN:", list(RPN.queue))

  # The queue now contains the operations to be performed in Reverse Polish
  # Notation, in the proper order considering the specified rules of operator
  # precedence.

  # Execute the expression
  exec_stack = []
  while not RPN.empty():

    # Pop next token from the RPN queue
    token = RPN.get()

    if isinstance(token, int):

      # If a number (operand) is encountered we push it into the execution stack
      exec_stack.append(token)

    else:

      # If an operator is encountered, we pop the last two operands in the
      # stack,apply the operator to them, and push the result back into the
      # stack.
      arg2 = exec_stack.pop()
      arg1 = exec_stack.pop()
      result = apply(token, arg1, arg2)
      exec_stack.append(result)

  # The remaining on the stack in the result of the evaluation.
  final_result = exec_stack.pop()
  return final_result

# ------------------------------------
# Part 1

precedence_rules = {'+': 0, '*': 0}

ans1 = 0
for expr in expressions:
  # print("-"*80)
  # print("".join([str(x) for x in expr]))
  result = evaluate(expr, precedence_rules)
  # print("result=", result)
  ans1 += result

print("Part 1:", ans1)

# ------------------------------------
# Part 2

precedence_rules = {'+': 1, '*': 0}

ans2 = 0
for expr in expressions:
  # print("-"*80)
  # print("".join([str(x) for x in expr]))
  result = evaluate(expr, precedence_rules)
  # print("result=", result)
  ans2 += result

print("Part 2:", ans2)
