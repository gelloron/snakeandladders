import random


snake_positions = {98: 10, 95: 87, 91: 88, 82: 63, 61: 57, 42: 29, 25: 19, 11: 7}
ladder_position = {1: 98, 5: 17, 18: 26, 33: 40, 48: 59, 67: 86, 75: 90}
print("hi and welcome to a game of snakes and ladders ")
num_of_players = input("please enter the number of players > ")
if num_of_players == "2":
    player1 = input("please enter the first player name > ")
    player2 = input("please enter the second player name > ")
    print(player1, "is playing against", player2)
elif num_of_players == "3":
    player1 = input("please enter the first player name > ")
    player2 = input("please enter the second player name > ")
    player3 = input("please enter the third player name > ")
    print(player1, "and", player2, "and", player3, "are playing against each other")
player1_position = player2_position = player3_position = 0


def moving(position):
    dice = random.randint(1, 6)
    position = position + dice
    if position in snake_positions:
        print(f'better luck next time')
        position = snake_positions[position]
        print(f"your position is {position}")
    elif position in ladder_position:
        print(f"oh yeah ")
        position = ladder_position[position]
        print(f"your position is {position}")
    else:
        print(f"your position is {position} ")
    print("\n")
    return position


while True:
    if num_of_players == "2":
        p1_dice_roll = input(f'{player1} please press \"1\" to roll a dice ')
        player1_position = moving(player1_position)
        p2_dice_roll = input(f'{player2} please press \"2\" to roll the dice ')
        player2_position = moving(player2_position)
    elif player1_position == 100:
        print(f'{player1} is the winner')
        break
    elif player2_position == 100:
        print(f'{player2} is the winner')
        break
    elif num_of_players == "3":
        p1_dice_roll = input(f'{player1} please press \"1\" to roll a dice ')
        player1_position = moving(player1_position)
        p2_dice_roll = input(f'{player2} please press \"2\" to roll the dice ')
        player2_position = moving(player2_position)
        p3_dice_roll = input(f'{player3} please press \"3\" to roll the dice ')
        player3_position = moving(player3_position)
    elif player1_position == 100:
        print(f'{player1} is the winner')
        break
    elif player2_position == 100:
        print(f'{player2} is the winner')
        break
    elif player3_position == 100:
        print(f'{player3} is the winner')
        break
