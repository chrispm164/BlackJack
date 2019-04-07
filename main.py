from Deck import *
from Player import *

players = []
win_score = 0
winners = []

d = Deck()
d.shuffle()

print('Welcome to BlackJack.\n')

prompt = ''
while prompt == '':
    try:
        prompt = int(input("How many players? "))
    except ValueError:
        print('Please enter a valid number. \n')

num_play = prompt
for i in range(num_play):
    players.append(Player())

print('Dealing hand...')

for p in players:
    p.add_card(d.deal_card())
    p.add_card(d.deal_card())

for p in players:
    print('\nIt is Player ' + str(players.index(p) + 1) + '\'s turn. ')
    print('Your hand is a ' + str(p.hand)[1:-1])
    print('It has a value of ' + str(p.hand_value()))
    action = ''
    while action != 'H' or action != 'S':
        action = input('\nWould you like to hit or stand? (H/S)')
        if action == 'H':
            p.add_card(d.deal_card())
            print('Your hand is a ' + str(p.hand)[1:-1])
            print('It has a value of ' + str(p.hand_value()))
            if p.hand_value() > 21:
                print('You bust.')
                break
            else:
                action = ''
        elif action == 'S':
            print('You stand.')
            if win_score < p.hand_value() <= 21:
                win_score = p.hand_value()
                winners.clear()
                winners.append(players.index(p) + 1)
            elif p.hand_value() == win_score:
                winners.append(players.index(p) + 1)
            break

print('The winner(s) are Player(s) ' + str(winners)[1:-1])
print('The winning score was ' + str(win_score))
