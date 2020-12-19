# Day 19: Monster Messages

import re
import sys

# ------------------------------------------------------------------------------

class Rule:

  # A rule is identified by its number
  # patterns contains the one or two patterns that this rule must satisfy
  # regex is used to store this rule's regex once it's computed
  def __init__(self, _id):
    self.id = _id
    self.patterns = []
    self.regex = None

  # Compute the regex that corresponds to this rule
  def get_regex(self):

    # If regex already computed just return it
    if self.regex is not None:
      return self.regex

    # Compute the regex of each part
    v = []
    for pat in self.patterns:
      s = ""
      for r in pat:
        if isinstance(r, str):
          # This part matches a single character
          s += r
        else:
          # This part is another rule, so we get its regex recursively
          s += r.get_regex()
      v.append(s)

    # Before returning the regex, we "remember" it so we don't compute
    # again if asked
    if len(v) == 1:
      self.regex = v[0]
      return self.regex
    else:
      self.regex = "(" + "|".join(v) + ")"
      return self.regex

  # Check is string s matches this rule
  def matches(self, s):
    p = self.get_regex()
    return re.fullmatch(p, s) is not None

  def __repr__(self):
    return "<{}: {}>".format(self.id, self.patterns)

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

rules = {}
messages = []
with open(sys.argv[1]) as f:
  for line in f:

    line = line.strip()
    if line == "":
      break
    else:

      tokens = line.split(":")

      # Get rule; create new one it if not yet added
      _id = int(tokens[0])
      if _id not in rules:
        rules[_id] = Rule(_id)
      rule = rules[_id]

      # Fill pattern(s) for the rule
      for token in tokens[1].split("|"):
        parts = token.split()
        for i in range(len(parts)):
          if parts[i].isnumeric():
            _id = int(parts[i])
            if _id not in rules:
              rules[_id] = Rule(_id)
            parts[i] = rules[_id]
          else:
            parts[i] = parts[i].strip('"')
        rule.patterns.append(parts)

  # Now just add messages
  for line in f:
    messages.append(line.strip())

# ------------------------------------
# Part 1

ans1 = 0
for m in messages:
  if rules[0].matches(m):
    ans1 += 1

print("Part 1:", ans1)

# ------------------------------------
# Part 2

ans2 = 0
for reps in range(1, 10):

  # Reset rule 0
  rules[0].regex = None

  # Change rules 8 and 11
  # For rule 11 we set the parts of the regex to have reps repetitions
  rules[8].regex = "{}+".format(rules[42].get_regex())
  rules[11].regex = "{0}{{{2}}}{1}{{{2}}}".format(rules[42].get_regex(), rules[31].get_regex(), reps)

  count = 0
  for m in messages:
    if rules[0].matches(m):
      count += 1
  print(reps, count)
  ans2 += count

print("Part 2:", ans2)
