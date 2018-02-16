import random


""" Write some code that simulates flipping a single coin however many times the user decides. 
The code should record the outcomes and count the number of tails and heads. """

print('Welcome to the ultimate coin flip simulator.')

def game():
    flip_times = int(input('How many times should the coin be fliped: '))
    flip = random.randrange(2)
    flip_count = 0
    tail_count = 0
    head_count = 0
    while flip_count <= flip_times:
        flip = random.randrange(2)
        flip_count += 1
        if flip is 0:
            tail_count += 1
            
            print('Tail')
        else:
            head_count += 1
            print('Head')
    
    print('There were', tail_count, 'tails, and', head_count, 'heads.' )
    again = input('Type y if you wanna play again.\nType n if you wanna exit:\n_')
    if again is 'y':
        game()
    elif again is 'n':
            quit()
    else:
         game()
        

game()


