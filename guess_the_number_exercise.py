low = 0
high = 100
guess = int((high + low)/2.0)
print("Please think a number between 0 and 100:")
while guess <= high:
    print("Is your secret number "+ str(guess) + "?")
    input_answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.: ")
    if input_answer == "l":
        low = guess
    elif input_answer == "h":
        high = guess
    elif input_answer == "c":
        print("Game over. Your secret number was: "+ str(guess))
        break
    else:
        print("I don't understand what you typed.")
        continue
    guess = int((high + low)/2.0)