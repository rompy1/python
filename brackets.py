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
bracketA = [0,0]
bracketB = [0,0]
bracketC = [0,0]
bracketD = [0,0]
brackets = [bracketA, bracketB, bracketC, bracketD]

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
print (brackets)


