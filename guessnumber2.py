import random
exit = 0
while exit == 0:
  print("Welcome to the number guessing game!")
  print("The object of the game is to guess my number.")
  print("The number will be between 1 and 50.")
  guess = 0
  number = random.randint(1,50)
  tries = 0
  endgame = 0
  while endgame == 0:
    tries += 1
    guess = int(input("Guess a number!"))
    if guess > number:
      print("My number is smaller than that!")
    elif guess < number:
      print("My number is bigger than that!")
    else:
      print("You guessed my number in %d attempts!" % tries)
      endgame = 1
    if tries >= 10:
      print("I'm sorry, you ran out of tries! Game Over.")
      endgame = 1
  input("Press enter to play again.")
  print("\n")
  
