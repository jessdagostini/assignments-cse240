player_number = 1
opponent_number = 2
possibilities = {
    "{0}{0}{0}{0}".format(player_number): 200,
    "{0}{0}{0}{1}".format(player_number, opponent_number): 90,
    "{0}{0}{1}{0}".format(player_number, opponent_number): 70,
    "{0}{0}{1}{1}".format(player_number, opponent_number): 50,
    "{0}{1}{0}{0}".format(player_number, opponent_number): 40,
    "{0}{1}{0}{1}".format(player_number, opponent_number): 10,
    "{0}{1}{1}{0}".format(player_number, opponent_number): -20,
    "{0}{1}{1}{1}".format(player_number, opponent_number): -90,
    "{1}{0}{0}{0}".format(player_number, opponent_number): 90,
    "{1}{0}{0}{1}".format(player_number, opponent_number): 70,
    "{1}{0}{1}{0}".format(player_number, opponent_number): 10,
    "{1}{0}{1}{1}".format(player_number, opponent_number): -70,
    "{1}{1}{0}{0}".format(player_number, opponent_number): 50,
    "{1}{1}{0}{1}".format(player_number, opponent_number): -70,
    "{1}{1}{1}{0}".format(player_number, opponent_number): -90,
    "{1}{1}{1}{1}".format(player_number, opponent_number): -100,
    "{0}{0}{0}0".format(player_number): 150,
    "{0}{0}0{0}".format(player_number): 150,
    "{0}{0}00".format(player_number): 120,
    "{0}0{0}{0}".format(player_number): 150,
    "{0}0{0}0".format(player_number): 100,
    "{0}00{0}".format(player_number): 100,
    "{0}000".format(player_number): 90,
    "0{0}{0}{0}".format(player_number): 150,
    "0{0}{0}0".format(player_number): 100,
    "0{0}0{0}".format(player_number): 100,
    "0{0}00".format(player_number): 90,
    "00{0}{0}".format(player_number): 100,
    "00{0}0".format(player_number): 90,
    "000{0}".format(player_number): 90
}

for p in possibilities:
    print(possibilities[p])