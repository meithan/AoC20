# Day 4: Passport Processing

import re
import sys

# ------------------------------------------------------------------------------

# The expected fields (except for cid)
exp_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

# Validity check for Part 1
def is_valid1(passport):
  for field in exp_fields:
    if field not in passport:
      if field != "cid":
        return False
  return True

# Validity check for Part 2
# First checks Part 1 validity, then checks each of the rules
# for the individual fields -- regexes rule!
def is_valid2(passport):

  if not is_valid1(passport):
    return False

  if not re.fullmatch("[0-9]{4}", passport["byr"]):
    return False
  if not (1920 <= int(passport["byr"]) <= 2002):
    return False

  if not re.fullmatch("[0-9]{4}", passport["iyr"]):
    return False
  if not (2010 <= int(passport["iyr"]) <= 2020):
    return False

  if not re.fullmatch("[0-9]{4}", passport["eyr"]):
    return False
  if not (2020 <= int(passport["eyr"]) <= 2030):
    return False

  m = re.search("([0-9]+)(cm|in)", passport["hgt"])
  if not m:
    return False
  if m.group(2) == "cm":
    if not (150 <= int(m.group(1)) <= 193):
      return False
  elif m.group(2) == "in":
    if not (59 <= int(m.group(1)) <= 76):
      return False

  if not re.fullmatch("#[0-9a-f]{6}", passport["hcl"]):
    return False

  if not re.fullmatch("(amb|blu|brn|gry|grn|hzl|oth)", passport["ecl"]):
    return False

  if not re.fullmatch("[0-9]{9}", passport["pid"]):
    return False

  return True

# ------------------------------------------------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read in passports from the input, split key:value pairs
passports = []
with open(sys.argv[1]) as f:
  passport = {}
  for line in f:
    if line == "\n":
      passports.append(passport)
      passport = {}
    else:
      for kv in line.strip().split():
        k, v = kv.split(":")
        passport[k] = v
  passports.append(passport)

# Part 1

count1 = 0
for passport in passports:
  if is_valid1(passport):
    count1 += 1

print("Part 1:", count1)

# Part 2

count2 = 0
for passport in passports:
  if is_valid2(passport):
    count2 += 1

print("Part 2:", count2)
