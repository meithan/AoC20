# This is my original solution, as-is
# Day 2:

# ----------------------------------

data = []
count = 0
with open("day2.in") as f:
  for line in f:
    tokens = line.strip().split()
    a = int(tokens[0].split("-")[0])
    b = int(tokens[0].split("-")[1])
    letter = tokens[1].strip(":")
    pswd = tokens[2]
    # if a <= pswd.count(letter) <= b:
    #   count += 1
    if( pswd[a-1] == letter and pswd[b-1] != letter) or (pswd[a-1] != letter and pswd[b-1] == letter):
      count += 1

print(count)
