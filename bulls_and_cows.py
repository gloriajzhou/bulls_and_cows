# Bulls and Cows (4-digit numerical version)

# Generate a random four-digit code
import random
print("Can you break the four-digit code?")
print("First, let's go over some terminology.")
print("One 'hit' means there is one number in the code you guessed that is both correct and in the correct position.")
print("One 'duck' means there is one number in the code you guessed that is correct but in the wrong position.")
code_gen = str(random.randint(1000, 9999))
first_val = code_gen[0]
second_val = code_gen[1]
third_val = code_gen[2]
fourth_val = code_gen[3]

player_status = "Y"
guess_count = 0

while player_status == "Y" or player_status == "y":
    print("Please enter your guess as a four-digit integer.")
    code_guess = str(input())
    val_one = code_guess[0]
    val_two = code_guess[1]
    val_three = code_guess[2]
    val_four = code_guess[3]
    guess_count = guess_count + 1

    if code_guess == code_gen:
        print("Congratulations! You have cracked the code.")
        player_status = "N"
        guess_count_string = str(guess_count)
        print("You used a total of " + guess_count_string + " guesses.")
    elif (first_val == val_one and second_val == val_two and third_val == val_three) or (first_val == val_one and second_val == val_two and fourth_val == val_four) or (first_val == val_one and third_val == val_three and fourth_val == val_four) or (second_val == val_two and third_val == val_three and fourth_val == val_four):
        print("There are 3 hits, 0 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and second_val == val_two and third_val == val_four and fourth_val == val_three) or (first_val == val_one and second_val == val_four and third_val == val_three and fourth_val == val_two) or (first_val == val_four and second_val == val_two and third_val == val_three and fourth_val == val_one) or (first_val == val_two and second_val == val_one and third_val == val_three and fourth_val == val_four) or (first_val == val_three and second_val == val_two and third_val == val_one and fourth_val == val_four) or (first_val == val_one and second_val == val_three and third_val == val_two and fourth_val == val_four):
        print("There are 2 hits, 2 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and second_val == val_two and (third_val == val_four or fourth_val == val_three)) or (first_val == val_one and third_val == val_three and (second_val == val_four or fourth_val == val_two)) or (first_val == val_one and fourth_val == val_four and (second_val == val_three or third_val == val_two)) or (second_val == val_two and third_val == val_three and (first_val == val_four or fourth_val == val_one)) or (second_val == val_two and fourth_val == val_four and (first_val == val_three or third_val == val_one)) or (third_val == val_three and fourth_val == val_four and (first_val == val_two or second_val == val_one)):
        print("There are 2 hits, 1 duck.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and (second_val == val_two or third_val == val_three or fourth_val == val_four)) or (second_val == val_two and (third_val == val_three or fourth_val == val_four)) or (third_val == val_three and fourth_val == val_four):
        print("There are 2 hits, 0 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and second_val == val_three and third_val == val_four and fourth_val == val_two) or (first_val == val_one and second_val == val_four and third_val == val_two and fourth_val == val_three) or (second_val == val_two and first_val == val_three and third_val == val_four and fourth_val == val_one) or (second_val == val_two and first_val == val_four and third_val == val_one and fourth_val == val_three) or (third_val == val_three and first_val == val_two and second_val == val_four and fourth_val == val_one) or (third_val == val_three and first_val == val_four and second_val == val_one and fourth_val == val_two) or (fourth_val == val_four and first_val == val_two and second_val == val_three and third_val == val_one) or (fourth_val == val_four and first_val == val_three and second_val == val_one and third_val == val_two):
        print("There is 1 hit, 3 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and third_val == val_two and (second_val == val_three or second_val == val_four)) or (first_val == val_one and second_val == val_three and third_val == val_four) or (first_val == val_one and third_val == val_four and (fourth_val == val_two or fourth_val == val_three)) or (first_val == val_one and fourth_val == val_three and third_val == val_two) or (first_val == val_one and second_val == val_four and (fourth_val == val_two or fourth_val == val_three)) or (first_val == val_one and second_val == val_three and fourth_val == val_two) or (second_val == val_two and first_val == val_three and (third_val == val_one or third_val == val_four)) or (second_val == val_two and first_val == val_four and third_val == val_one) or (second_val == val_two and first_val == val_four and (fourth_val == val_one or fourth_val == val_three)) or (second_val == val_two and first_val == val_three and fourth_val == val_one) or (second_val == val_two and third_val == val_four and (fourth_val == val_one or fourth_val == val_three)) or (second_val == val_two and third_val == val_one and fourth_val == val_three) or (third_val == val_three and second_val == val_four and (fourth_val == val_one or fourth_val == val_two)) or (third_val == val_three and second_val == val_one and fourth_val == val_two) or (third_val == val_three and first_val == val_four and (fourth_val == val_one or fourth_val == val_two)) or (third_val == val_three and first_val == val_two and fourth_val == val_one) or (third_val == val_three and first_val == val_two and (second_val == val_one or second_val == val_four)) or (third_val == val_three and first_val == val_four and second_val == val_one) or (fourth_val == val_four and first_val == val_two and (second_val == val_one or second_val == val_three)) or (fourth_val == val_four and first_val == val_three and second_val == val_one) or (fourth_val == val_four and first_val == val_three and (third_val == val_one or third_val == val_two)) or (fourth_val == val_four and first_val == val_two and third_val == val_one) or (fourth_val == val_four and second_val == val_three and (third_val == val_one or third_val == val_two)) or (fourth_val == val_four and second_val == val_one and third_val == val_two):
        print("There is 1 hit, 2 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_one and ((second_val == val_three or second_val == val_four) or (third_val == val_two or third_val == val_four) or (fourth_val == val_two or fourth_val == val_three))) or (second_val == val_two and ((first_val == val_three or first_val == val_four) or (third_val == val_one or third_val == val_four) or (fourth_val == val_one or fourth_val == val_three))) or (third_val == val_three and ((first_val == val_two or first_val == val_four) or (second_val == val_one or second_val == val_four) or (fourth_val == val_one or fourth_val == val_two))) or (fourth_val == val_four and ((first_val == val_two or first_val == val_three) or (second_val == val_one or second_val == val_three) or (third_val == val_one or third_val == val_two))):
        print("There is 1 hit, 1 duck.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif first_val == val_one or second_val == val_two or third_val == val_three or fourth_val == val_four:
        print("There is 1 hit, 0 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_two and (second_val == val_one or second_val == val_three or second_val == val_four) and (third_val == val_one or third_val == val_four) and (fourth_val == val_one or fourth_val == val_three)) or (first_val == val_three and (second_val == val_one or second_val == val_four) and (third_val == val_one or third_val == val_four) and fourth_val == val_two) or (first_val == val_four and (second_val == val_one or second_val == val_three) and third_val == val_two and (fourth_val == val_one or fourth_val == val_three)):
        print("There are 0 hits, 4 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_two and (second_val == val_three or second_val == val_four) and (third_val == val_one or fourth_val == val_one or fourth_val == val_three or third_val == val_four)) or (first_val == val_three and (second_val == val_one or fourth_val == val_one or second_val == val_four or fourth_val == val_two) and (third_val == val_two or third_val == val_four)) or (first_val == val_four and (fourth_val == val_two or fourth_val == val_three) and (second_val == val_one or third_val == val_one or second_val == val_three or third_val == val_two)) or ((second_val == val_three or second_val == val_four or second_val == val_one) and (third_val == val_four or third_val == val_two or third_val == val_one) and (fourth_val == val_two or fourth_val == val_three or fourth_val == val_one)):
        print("There are 0 hits, 3 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif (first_val == val_two and (second_val == val_one or second_val == val_three or second_val == val_four or third_val == val_one or third_val == val_four or fourth_val == val_one or fourth_val == val_three)) or (first_val == val_three and (second_val == val_one or second_val == val_four or third_val == val_one or third_val == val_two or third_val == val_four or fourth_val == val_one or fourth_val == val_two)) or (first_val == val_four and (second_val == val_one or second_val == val_three or third_val == val_one or third_val == val_two or fourth_val == val_one or fourth_val == val_two or fourth_val == val_three)) or (second_val == val_three and (third_val == val_one or third_val == val_two or third_val == val_four or fourth_val == val_one or fourth_val == val_two)) or (second_val == val_one and (third_val == val_two or third_val == val_four or fourth_val == val_two or fourth_val == val_three)) or (second_val == val_four and (third_val == val_one or third_val == val_two or fourth_val == val_one or fourth_val == val_two or fourth_val == val_three)) or (third_val == val_four and (fourth_val == val_one or fourth_val == val_two or fourth_val == val_three)) or (third_val == val_one and (fourth_val == val_two or fourth_val == val_three)) or (third_val == val_two and (fourth_val == val_one or fourth_val == val_three)):
        print("There are 0 hits, 2 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    elif first_val == val_two or first_val == val_three or first_val == val_four or second_val == val_one or second_val == val_three or second_val == val_four or third_val == val_one or third_val == val_two or third_val == val_four or fourth_val == val_one or fourth_val == val_two or fourth_val == val_three:
        print("There are 0 hits, 1 duck.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()
    else:
        print("There are 0 hits, 0 ducks.")
        print("Would you like to continue guessing? [Y or N]")
        player_status = input()

if not (player_status == "Y" or player_status == "y"):
    print("The correct code was " + str(code_gen) + ". Thank you for playing.")
