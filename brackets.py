import random 

x = 0
ls = []
length = length = int(input("How many players?\n"))
while x == 0:
  for c in range(length):
    names= input ("Add Names:")
    ls.append(f"{names}")
    x=1
  print (ls)
list2 = ls
bracketA = ["buy","buy"]
bracketB = ["buy","buy"]
bracketC = ["buy","buy"]
bracketD = ["buy","buy"]
bracketE = ["buy","buy"]
bracketF = ["buy","buy"]
bracketG = ["buy","buy"]
bracketH = ["buy","buy"]
brackets = [bracketA, bracketB, bracketC, bracketD, bracketE, bracketF, bracketG, bracketH]

for item in brackets:
  x = 0
  try:
    while x < 2:
      length = len(list2) - 1
      rand = random.randint(0, length)
      item[x] = list2[rand]
      list2.pop(rand)
      x += 1
  except ValueError:
    break
x = 0
print(brackets)
for item in brackets:
  print(len(brackets))
  print(item)
  if item[0] == "buy" and item[1] == "buy":
    brackets.pop(x)
  x += 1
print (brackets)

