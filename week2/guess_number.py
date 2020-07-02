print("Please think of a number between 0 and 100!")

low = 0
high = 100
input_string = ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

guess = (low + high) / 2

print("Is your secret number " + str(guess) + "?")
answer = input(input_string)

while answer != 'c':
    if answer == 'h':
        low = guess
    elif answer == 'l':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = (low + high) / 2
    print("Is your secret number " + str(guess) + "?")
    answer = input(input_string)

print("Game over. Your secret number was: " + str(guess))
