game = False

picks = ["paper", "rock", "scissors"]
player_pick = ()

def game_introduction():
    global player_pick
    global game

    print("\nWelcome to this simple game of rock, paper, scissors, you can exit at any time by typing in 'exit'.\n")

    player_pick = input("Pick between rock, paper and scissors: ")
    game = True


def game_start():
    global picks
    global player_pick

    import random
    cpu_pick = random.choice(picks)

    if player_pick == cpu_pick:                                                 # tie condition
        player_pick = input("\nIt's a tie, try again?: ")

    elif picks.index(cpu_pick) == (picks.index(player_pick) + 1) % 3:             # win condition
        player_pick = input("\nYour " + player_pick + " wins! Wanna go again?: ")

    else:                                                                       # lose condition
        player_pick = input("\nYou lost, the computer picked " + cpu_pick + ". Wanna try again?: ")


while game is False:
    game_introduction()

while game is True:
    try:
        if player_pick == "exit":  # exit option
            print("Thanks for playing.")
            break

        for x in picks:                                           # error definition
            if player_pick not in picks:
                raise AssertionError

        print("Rock, paper, scissors!")

        game_start()

    except AssertionError:                                       # error exception
        print("\nAn error has occurred, check your input and try again...\n")
        continue
