import random
import shelve

def Highscore():
  db = shelve.open("Highscores")
  print("Scores:")
  print(db["scores"])
  db.close

exit = 0
while exit == 0:
  try:
    Highscore()
  except:
    KeyError
    print("Setting up database...")
    db = shelve.open("Highscores")
    db["scores"] = []
    db.close
  print("Welcome to the number guessing game!")
  print("The object of the game is to guess my number.")
  print("The number will be between 1 and 100.")
  number = random.randint(0,100)
  tries = 0
  endgame = 0
  while endgame == 0:
    tries += 1
    exit2 = 0
    while exit2 == 0:
      try:
        guess = int(input("Guess a number!\n"))
        exit2 = 1
      except:
        ValueError
        print("That's not a number!")
    if guess > number:
      print("My number is smaller than that!")
    elif guess < number:
      print("My number is bigger than that!")
    else:
      print("You guessed my number in %d attempts!" % tries)
      name = input("What is your name?")
      db = shelve.open("Highscores")
      temp = db["scores"]
      temp.append((name, tries))
      db["scores"] = temp
      db.close()
      endgame = 1
    if tries >= 10:
      print("I'm sorry, you ran out of tries! Game Over.")
      endgame = 1
  input("Press enter to play again.")
  print("\n")
