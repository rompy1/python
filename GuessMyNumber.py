import random
exit = 0
while exit == 0:
  print("Welcome to the number guessing game!")
  print("The object of the game is to guess my number.")
  print("The number will be between 1 and 50.")
  guess = -5000
  number = random.randint(1,50)
  tries = 0
  while guess != number:
    tries += 1
    guess = int(input("Guess a number!"))
    if guess > number:
      print("My number is smaller than that!")
    elif guess < number:
      print("My number is bigger than that!")
  print("You guessed my number in %d attempts!" % tries)
  input("Press enter to play again.")
  print("\n")
