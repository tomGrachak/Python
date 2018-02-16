import random
def game():
    print('Guess 3 numbers between 1 and 9 to win this game.\n')
    r = random.randrange(1,9)
    points = 0
    print(r)
    user_nums = []
    for n in range(6):
        r = random.randrange(9)

        try:
            user_nums = (int(input('Enter your number: ')))
        except ValueError:
                user_nums = (int(input('Be sure to enter a number: ')))
        if user_nums == r:
            print('Bravo!')
            nums.append(user_nums)
            print(nums[:])
            points += 1
    if points == 3:
        print('Congrats, You Won!!!')
        ng = input('Wanna play again?\n ')
        if ng == 'y':
            game()
        else:
                print('So long, You hot stud.')
                quit()
    else:
        print('Game over, Sucker!')
        ng = input('Wanna play again?\n ')
        if ng == 'y':
            game()
        else:
                print('So long, You hot stud.')
                quit()

nums = []
game()