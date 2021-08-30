import random

while True:
    guess = None
    count = 1
    r = random.randint(1,9)

    while guess != count :
        guess = input('Type a number between 1 - 9: ')
        if guess.isdigit():
            guess = int(guess)
            if guess == r:
                print('YOU WON!')
            elif(guess > r):
                print('Your guess is too big, please try again')
                count = +1
            elif(guess < r):
                print('your guess is too small, please try again')
                count = +1
            elif (count >= 5):
                print('YOU LOOSE!!! The number is', r)
    print('It took you', count, "guesses")