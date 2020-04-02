game = False

picks = ["rock", "paper", "scissors"]

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

    import random                                       # cpu pulls a random str from the "picks" list
    cpu_pick = random.choice(picks)

    if player_pick == "rock":                           # win condition
        if cpu_pick == "scissors":
            player_pick = input("\nYour rock wins! Wanna go again?: ")
    elif player_pick == "paper":
        if cpu_pick == "rock":
            player_pick = input("\nYour paper wins! Wanna go again?: ")
    elif player_pick == "scissors":
        if cpu_pick == "paper":
            player_pick = input("\nYour scissors win! Wanna go again?: ")

    if str(player_pick) == str(cpu_pick):               # tie condition
        player_pick = input("\nIt's a tie! Again?: ")

    else:                                               # lose condition
        player_pick = input("\nYou lost, the computer chose " + cpu_pick + " wanna try again?: ")


while game is False:
    game_introduction()

while game is True:
    try:
        if player_pick == "exit":                       # exit option
            print("Thanks for playing.")
            break

        for x in picks:                                 # error definition
            if player_pick not in picks:
                raise AssertionError

        print("Rock, paper, scissors!")

        game_start()

    except AssertionError:                              # error exception
        print("\nAn error has occurred, check your input and try again...\n")
        continue
