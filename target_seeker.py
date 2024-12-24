import random

target = random.randint(1, 100)  # Generate the target number
max_attempts = 5  # Set to 5 attempts for a balanced challenge
attempts = 0

while attempts < max_attempts:
    userChoice = input("Guess the target or Quit: ")
    if userChoice == "Quit":
        break

    userChoice = int(userChoice)
    attempts += 1
    if userChoice == target:
        print(f"Congrates: Correct Guess!! It took you {attempts} tries.")
        break
    elif userChoice < target:
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")

if attempts == max_attempts:
    print(f"Sorry, you've reached {max_attempts} attempts. The target was {target}.")
print("---------GAME OVER----------")


