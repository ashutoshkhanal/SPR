print('***********Welcome to Rock Paper Scissors Game***********')

print('Rules: Rock beats scissors, Scissors beats paper, Paper beats rock \n')

while True:

    player1 = input("What's your name?")
    player2 = input("And your name?")


    game_start={'rock': 1,'paper': 2,'scissors': 3}

    player_1 = input("%s, do yo want to choose rock, paper or scissors?" % player1)
    player_2 = input("%s, do you want to choose rock, paper or scissors?" % player2)

    a = game_start.get(player_1)
    b = game_start.get(player_2)

    difference = a - b

    if difference in [-2, 1]:
        print('player 1 wins.')

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue

        else:
            print('game over.')
            break

    elif difference in [-1, 2]:
        print('player 2 wins.')

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break

    else:
        print('Draw.Please continue.')
        print('')
