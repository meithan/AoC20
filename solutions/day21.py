# Day 21: Allergen Assessment

import re
import sys

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Just all the lists of ingredients
ing_lists = []
# Just all the different ingredients
ingredients = set()
# Dict with alergen: <list of ingredients possibly containing it>
allergens = {}

with open(sys.argv[1]) as f:
  for line in f:

    # Parse line
    m = re.match("(.+) \(contains (.+)\)", line.strip())
    ings = m.group(1).split()
    allergs = m.group(2).split(", ")

    # Save the ingredients list (for counts later)
    ing_lists.append(ings)

    # Add the ingredients to the set of all ingredients
    for ing in ings:
      ingredients.add(ing)

    # For each allergen, we compute the intersection of the set of the
    # possible ingredientes previously saved and the new set of possibles
    for a in allergs:
      if a not in allergens:
        allergens[a] = set(ings)
      else:
        allergens[a] = allergens[a] & set(ings)

# ------------------------------------
# Part 1

# Determine the set of all ingredients that may contain an allergen
# By just making the union of all the sets of possibles
may_contain = set()
for a in allergens:
  ings = allergens[a]
  may_contain = may_contain | ings

# Ingredients not in this set are allergen-free
allergens_free = ingredients - may_contain

# Count how many times each allergen-free ingredient appears
ans1 = 0
for ing in allergens_free:
  for l in ing_lists:
    ans1 += l.count(ing)

print("Part 1:", ans1)

# ------------------------------------
# Part 2

# When an allergen has a single possible ingredient, remove it from
# all other allergens. Keep doing this until we know which ingredient
# contains which allergen
solutions = {}
while True:
  for a in allergens:
    if len(allergens[a]) == 1:
      solutions[a] = allergens[a].pop()
      for a1 in allergens:
        allergens[a1].discard(solutions[a])
  if all(len(allergens[a])==0 for a in allergens):
    break

# Sort the list ingredientes by allergen, build the answer
dangerous = [(solutions[a], a) for a in solutions]
dangerous.sort(key=lambda x: x[1])
ans2 = ",".join([x[0] for x in dangerous])

print("Part 2:", ans2)
