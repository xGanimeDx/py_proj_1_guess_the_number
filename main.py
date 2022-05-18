import random

number = random.randint(1, 20)
tries = 3
while True:
    guess = int(input('Make a guess: '))
    tries -= 1
    if number == guess:
        print('WIN! You got the number!')
        break
    elif number != guess and tries > 0:
        print(f'WRONG! Try again! {tries} out of 3 left.')
        if guess > number:
            print('The number is less than current guess.')
        else:
            print('The number is greater than current guess.')
        continue
    else:
        print(f'LOSE! Then number was {number}.')
        break
