import random

exit = 0
while exit == 0:
  print ("This is the number guessing game")
  print ("The number is between 0 and 100.")
  print ("You have only 10 tries, don't fuck up. Good Luck!")
 
  number = random.randint(0,100)
  tries = 0
  endgame = 0
  while endgame == 0:
    tries += 1
    guess = int(input("GUESS NUMBER:"))
    if guess > number:
        print ("The number is smaller.")
    elif guess < number:
        print ("The number is larger.")
    elif tries == 1: 
        print ("Holy Shit man")
        print (f"You have guessed this in {tries} try")
    elif tries < 4:
        print ("Damn you're good")
        print (f"You have guessed this in {tries} tries")
    elif tries < 8:
        print ("You are Average.")
        print (f"You have guessed this in {tries} tries")
    else:
        print (f"You have guessed this in {tries} tries")
        print ("Suprisingly, you don't suck.")
        endgame = 1
    if tries > 10:
        print ("You ran out of attempts. You suck!") 
  input("Press enter to play again.")
  print("\n")
