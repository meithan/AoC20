# Day 22: Crab Combat

from collections import deque
import copy
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

deck1_orig = deque()
deck2_orig = deque()
with open(sys.argv[1]) as f:
  for line in f:
    if "Player 1" in line:
      deck = deck1_orig
    elif "Player 2" in line:
      deck = deck2_orig
    elif line.strip() == "":
      continue
    else:
      deck.append(int(line.strip()))

def play_Combat(deck1, deck2):

  round = 0
  while True:

    round += 1

    card1 = deck1.popleft()
    card2 = deck2.popleft()

    # print("Round", round)
    # print("Player 1 plays", card1)
    # print("Player 2 plays", card2)

    if card1 > card2:
      deck1.extend([card1, card2])
      # print("Player 1 wins the round")
    else:
      deck2.extend([card2, card1])
      # print("Player 2 wins the round")

    if len(deck2) == 0:
      # print("Player 2 wins")
      return (1, deck1)
    elif len(deck1) == 0:
      # print("Player 1 wins")
      return (2, deck2)

# ------------------------------------
# Part 1

deck1 = deck1_orig.copy()
deck2 = deck2_orig.copy()

winner, winner_deck = play_Combat(deck1, deck2)
N = len(winner_deck)
ans1 = sum([(N-i)*winner_deck[i] for i in range(N)])

print("Part 1:", ans1)

# ------------------------------------
# Part 2

def play_Recursive_Combat(deck1, deck2, depth=1):

  # print("Starting game at depth=", depth, len(deck1), len(deck2))

  past_states = set()
  round = 0
  while True:

    round += 1
    # print("Round", round)

    # print("Player 1 deck:", deck1)
    # print("Player 2 deck:", deck2)

    state = (tuple(deck1), tuple(deck2))
    # print(state)
    if state in past_states:
      # print("Player 1 wins by repetition after {} rounds".format(round))
      # input()
      return (1, None)
    else:
      past_states.add(state)


    card1 = deck1.popleft()
    card2 = deck2.popleft()
    # print("Player 1 plays", card1)
    # print("Player 2 plays", card2)

    if len(deck1) >= card1 and len(deck2) >= card2:
      # print("\nRecursing")
      sub_deck1 = deque(list(deck1)[:card1])
      sub_deck2 = deque(list(deck2)[:card2])
      winner, _ = play_Recursive_Combat(sub_deck1, sub_deck2, depth+1)
      # print("Player {} wins subgame".format(winner))
    else:
      if card1 > card2:
        winner = 1
      else:
        winner = 2

    if winner == 1:
      # print("Player 1 wins round")
      deck1.extend([card1, card2])
    elif winner == 2:
      # print("Player 2 wins round")
      deck2.extend([card2, card1])

    if len(deck2) == 0:
      # print("Player 1 wins game fairly after {} rounds".format(round))
      return (1, deck1)
    elif len(deck1) == 0:
      # print("Player 2 wins game fairly after {} rounds".format(round))
      return (2, deck2)

    # input()

# ------------------------------------

deck1 = deck1_orig.copy()
deck2 = deck2_orig.copy()

winner, winner_deck = play_Recursive_Combat(deck1, deck2)
# print(winner_deck, len(winner_deck))

N = len(winner_deck)
ans2 = sum([(N-i)*winner_deck[i] for i in range(N)])

print("Part 2:", ans2)
