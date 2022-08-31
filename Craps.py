import random
from enum import Enum;
class status:
    WIN = 1
    CONTINUE = 2
    LOST = 3
def diceRoll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    sum = d1 + d2
    print(f'Dice 1: {d1}, Dice 2: {d2}\nSum: {d1} + {d2} = {sum}')
    return sum


def main():
    print("________________Welcome to Craps________________")
    point = 0
    sum = diceRoll()
    if(sum == 7 or sum == 11):
        print(f'Congrats, you beat the house: You rolled a {sum}')
        status = 1
    elif(sum == 2 or sum == 3 or sum == 12):
        print(f'Sorry, The house wins, You rolled Craps which was {sum}')
        status = 3
    else:
        print(f'You rolled a {sum}. Your point is {sum}')
        point = sum
        status = 2
    
    while(status == 2): 
        print('\n')
        sum = diceRoll()
        if(sum == point):
            print(f'Congrats, you beat the house: You rolled a {sum} which is your point.')
            break
        if(sum == 7):
            print(f'Sorry, The house wins, You rolled a {sum} before making your point.')
            break
    again = input("\nDo you want to play Craps again? (Y or N)")
    if(again.upper() == 'Y'):
        main()
main()
