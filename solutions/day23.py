# Day 23: Crab Cups

import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  puzzle_input = f.readline().strip()

# ------------------------------------
# Part 1

def do_moves1(num_moves):

  cups = [int(l) for l in puzzle_input]
  min_cup = min(cups)
  max_cup = max(cups)
  N = len(cups)

  idx = 0
  move = 1

  for _ in range(num_moves):

    # print("move=",move)
    # print(cups)

    current = cups[idx]
    # print("current=",current)

    removed = [cups[(idx+1+i)%N] for i in range(3)]
    # print(removed)

    for r in removed:
      cups.remove(r)

    dest = current-1
    while True:
      if dest < min_cup:
        dest = max_cup
      if dest not in removed:
        break
      else:
        dest -= 1

    # print("dest=",dest)
    new_cups = []
    for c in cups:
      new_cups.append(c)
      if c == dest:
        new_cups += removed

    cups = new_cups
    idx = (cups.index(current) + 1) % N

    move += 1

  return cups

# -----------------------------------

cups = do_moves1(100)
N = len(cups)

idx = cups.index(1)
ans1 = ""
for i in range(N-1):
  ans1 += "" + str(cups[(idx+1+i)%N])

print("Part 1:", ans1)

# ------------------------------------
# Part 2

# A Cup is a node in a singly linked list
class Cup:

  def __init__(self, label):
    self.label = label
    self.next = None

  def __repr__(self):
    return "<Cup {}; next: {}>".format(self.label, self.next.label if self.next is not None else "None")

  # Cuts a length-N chain starting from the node following this node
  # Returns the (head, tail) nodes of the cut chain
  def cut_chain(self, N):
    head = self.next
    tail = head
    for i in range(N-1):
      tail = tail.next
    self.next = tail.next
    tail.next = None
    return (head, tail)

  # Inserts the given chain (defined by its head and tail) right
  # after this node
  def insert_chain(self, head, tail):
    old_next = self.next
    self.next = head
    tail.next = old_next

# Utility function to show the print the cup sequence until it loops around
def show_cups(current):
  lbl0 = current.label
  labels = [lbl0]
  current = current.next
  while current.label != lbl0:
    labels.append(current.label)
    current = current.next
  # labels.append(current.label)
  print(" > ".join([str(x) for x in labels]))

# Starting from first, do N moves of the cups game
def do_moves2(first, N):

  current = first
  for move in range(1, N+1):

    # Cut the chain of the next three cups
    head, tail = current.cut_chain(3)

    # Labels of removed cups
    removed = (head.label, head.next.label, tail.label)

    # Determine the destination cup
    dest_lbl = current.label - 1
    while True:
      if dest_lbl < min_cup:
        dest_lbl = max_cup
      if dest_lbl not in removed:
        break
      else:
        dest_lbl -= 1
    dest = cups[dest_lbl]

    # Insert back removed chain after destination cups
    dest.insert_chain(head, tail)

    # Advance to next cup
    current = current.next

# -----------------------------------

# Build the full list of cups numbers
max_cup = 1000000
cup_numbers = [int(l) for l in puzzle_input]
cup_numbers = [int(l) for l in puzzle_input] + list(range(max(cup_numbers)+1, max_cup+1))
min_cup = min(cup_numbers)
N = len(cup_numbers)

# Parse puzzle input into linked Cup objects and a dict for fast lookups
cups = {}
first = None
last = None
for n in cup_numbers:
  cup = Cup(n)
  if first is None:
    first = cup
  cups[n] = cup
  if last is not None:
    last.next = cup
  last = cup
last.next = first

# Do TEN MILLION moves
do_moves2(first, 10000000)

ans2 = cups[1].next.label * cups[1].next.next.label

print("Part 2:", ans2)
