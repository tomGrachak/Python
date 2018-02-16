"""Make a Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""
import random

score = {'Player': 0, 'CPU': 0}
def rps():
    list = ['r', 'p', 's'] 
    ui = input('Enter one of the following:\np for paper\nr for rock\ns for scissors\nq to quit (only for quitters.)\n')
    for n in random.choice(list):
        n = n
        print('>',n)
        if n is 'r' and ui is 'p':
            print('<<< Paper beats rock >>>')
            print('You Won!\n')
            score['Player'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:', score['CPU'], '\n')
            if score['Player'] - score['CPU'] == 3:
                print('Wow, 3 in a row!\n')
            rps()
        elif n is 'p' and ui is 'r':
            print('<<< Paper beats rock >>>')
            print('You loose, sucker!\n')
            score['CPU'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:',score['CPU'],'\n' )
            if score['CPU'] - score['Player'] == 3:
                print('Why don\'t you just give up?\n')
            rps()
        elif n is 'p' and ui is 's':
            print('<<< Scissors beat paper >>>')
            print('You Won!\n')
            score['Player'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:', score['CPU'], '\n')
            if score['Player'] - score['CPU'] == 3:
                print('Wow, 3 in a row!\n')
            rps()
        elif n is 's' and ui is 'p':
            print('You loose, sucker!\n')
            print('<<< Scissors beats paper >>>')
            score['CPU'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:',score['CPU'],'\n' )
            if score['CPU'] - score['Player'] == 3:
                print('Why don\'t you just give up?\n')
            rps()
        elif n is 's' and ui is 'r':
            print('<<< Rock beats scissors >>>')
            print('You Won!\n')
            score['Player'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:', score['CPU'], '\n')
            if score['Player'] - score['CPU'] == 3:
                print('Wow, 3 in a row!\n')
            rps()
        elif n is 'r' and ui is 's':
            print('<<< Rock beats scissors >>>')
            print('You loose, sucker!\n')
            score['CPU'] += 1
            print('Player:', score['Player'], ' - ', 'CPU:',score['CPU'],'\n' )
            if score['CPU'] - score['Player'] == 3:
                print('Why don\'t you just give up?\n')
            rps()
        elif ui is 'q':
            print('The final result is >>> Player:', score['Player'], ' - ', 'CPU:', score['CPU'], '\n')
            if score['CPU'] < score['Player']:
                print('Victory!')
                quit()
            else:
                print('What a looser.')
        else:
            print('Draw!\n')
            print('Player:', score['Player'], ' - ', 'CPU:', score['CPU'], '\n')
            rps()
rps()