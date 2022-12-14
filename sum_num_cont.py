#!/usr/bin/env python3
# Created by: Peter Sobowale
# Created on: December 7, 2022
# This program asks the user how many numbers they plan on adding.
# The user will  add each number and then the program
# will display the sum of the numbers


def main():
    # initialize Variables
    sum_display = ""
    sum = 0
    counter = 0

    # try check for exceptions
    try:
        # ask user for total number of inputs (to be added) and casts variable to int
        total_number = int(input("Enter the total numbers to be added: "))

    # erroneous data
    except Exception:
        print("Please enter a whole number!")

    # If the user entered a valid number (input wise)
    else:

        # If the user entered a negative number for the total numbers
        if total_number < 0:
            print("Please enter a positive integer!")

        else:
            # while loop
            while counter < total_number:
                # try check for exceptions
                try:
                    # Asks user for the number they want to add (converts to int)
                    user_add = int(input("\nEnter the number you want to add: "))

                # In the event of an exception
                except Exception:
                    print("Please enter a whole number!\n")

                else:
                    # If the user tried to add a negative number
                    if user_add < 0:
                        print("You may not enter a negative number!\n")

                        # continue statement
                        continue

                    # iF the user tries to add 0 to the sum
                    elif user_add == 0:
                        print("0 <= 0, therefore it will not be added.\n")

                    # If the user tries to add a valid number
                    else:
                        # Displays to user that the number was added
                        print(f"{user_add} added to the sum.\n")

                        # Increments counter
                        counter += 1

                        # Adds the number to the sum
                        sum += user_add

                        # Ensures that there will not be an empty plus symbol at the end of the sum message
                        if counter != total_number:

                            # Adds the user's number to string that will be later displayed
                            sum_display += str(user_add) + " + "

                        # Else statement meant to handle the last number the user plans to add
                        else:

                            # Adds number user plans to add to the sum (as string)
                            sum_display += str(user_add)

            # If statement to account for the message if the total number is 0
            if total_number != 0:

                # Displays all the numbers added to sum (and the sum itself)
                print(f"{sum_display} = {sum}")

            # Displays sum to user
            print(f"Sum = {sum}")

    # Final message displayed to user regardless of input
    finally:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()
