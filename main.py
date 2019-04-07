from Deck import *
from Dealer import *


running = True

while running:
    players = []
    win_score = 0
    winners = []

    d = Deck()
    d.shuffle()
    dealer = Dealer()

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

    dealer.add_card(d.deal_card())
    dealer.add_card(d.deal_card())

    for p in players:
        print('\nIt is Player ' + str(players.index(p) + 1) + '\'s turn. ')
        print('Your hand is a ' + str(p.hand)[1:-1])
        print('It has a value of ' + str(p.hand_value()))
        for o in players:
            if o != p:
                print('Player ' + str(players.index(o) + 1) + ' is showing a ' + str(o.hand[0]))
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

    print('\nDealer\'s Turn')
    print('The dealer\'s hand is a ' + str(dealer.hand)[1:-1])
    print('The dealer has a score of ' + str(dealer.hand_value()) + '.')
    if dealer.hand_value() < 17:
        print('The dealer takes their turn.')
        dealer.dealer_turn(d.deal_card())
        print('The dealer\'s hand is now a ' + str(dealer.hand)[1:-1])
        print('The dealer now has a score of ' + str(dealer.hand_value()) + '.')

    if dealer.hand_value() > 21:
        print('The dealer busts.')
    else:
        if dealer.hand_value() > win_score:
            print('\nThe dealer wins with a score of ' + str(dealer.hand_value()) + '.')
        else:
            if len(winners) == 1:
                print('\nThe winner is Player ' + str(winners)[1:-1])
            else:
                print('\nThe winners are Players ' + str(winners)[1:-1])
            print('The winning score was ' + str(win_score))

    replay = input('\nWould you like to play again? (Y/N) ')
    while replay != 'Y' and replay != 'N':
        replay = input('\nWould you like to play again? (Y/N) ')
        print(replay)
    if replay == 'Y':
        pass
    else:
        running = False
