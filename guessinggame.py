# importing an external module from the python standard library into
# the module you are working within allows you to utilize all the
# objects in that external module (similar to a wildcard symbol)
import random

# generate a random number between 1 and 5 inclusive (of both values).
# this number is going to be computer generated to check against the user's input value given.
computer_guess = random.randint(1, 5)

# represents the number of user tries to guess correct until correctly guessed.
# the value chosen by the user must be range-appropriate in order to count as an attempt.
attempts = 0
total_attempts = 10

print("*******************************************\n"
      "You have {} attempts to guess correctly."
      "\n*******************************************\n".format(total_attempts))

while True:

    if attempts == total_attempts:
        print("{0} equals {1} and so maximum number of attempts has been reached.\n"
              .format(attempts, total_attempts) +
              "user guess was {0} while computer guess was {1}.\n"
              .format(user_guess, computer_guess) +
              "Exiting program now.")
        break

    # get user to provide a value to check against.
    user_guess = int(input("Guess a number from 1 to 5 or press \"0\" to exit the program\t:"))

    if user_guess == 0:

        print('"0" was pressed.\nExiting program.\nGoodbye.')
        break

    elif 0 < user_guess < 6:

        if user_guess < computer_guess:

            attempts += 1
            print("No. attempts remaining: {}".format(total_attempts - attempts))
            if (total_attempts - attempts) == 0:
                continue
            print("guess higher than {}".format(user_guess))
            continue

        elif user_guess > computer_guess:

            attempts += 1
            print("No. attempts remaining: {}".format(total_attempts - attempts))
            if (total_attempts - attempts) == 0:
                continue
            print("guess lower than {}".format(user_guess))
            continue

        else:

            attempts += 1
            print("user\t:{0:02}\t | \tcomputer\t:{1:02}\nNo. Attempts: {2:03}"
                  .format(user_guess, computer_guess, attempts))
            break

    else:

        print("{:02} is not a valid entry!".format(user_guess))
