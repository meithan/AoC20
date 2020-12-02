# Day 2: Password Philosophy

# ----------------------------------

count1 = count2 = 0
with open("day2.in") as f:
  for line in f:
    tokens = line.strip().split()
    a, b = [int(x) for x in tokens[0].split("-")]
    letter = tokens[1].strip(":")
    pswd = tokens[2]
    if a <= pswd.count(letter) <= b:
      count1 += 1
    if (pswd[a-1] == letter) ^ (pswd[b-1] == letter):
      count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
