import random

def guess_the_number():
   number_to_guess = random.randint(1, 100)
   guess = None

   while guess != number_to_guess:
      try:
         guess = int(input("Guess a number between 1 and 100: "))

         if guess < number_to_guess:
            print("Too low!")
         elif guess > number_to_guess:
            print("Too high!")
         else:
            print("Congratulations! You guessed the right number.")
      except ValueError:
         print("Please enter a valid number.")

guess_the_number()
