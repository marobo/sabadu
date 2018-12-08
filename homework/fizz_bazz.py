my_game = 0
def play_games(my_game):
    for my_game in range(1, 100):
    	if my_game % 3 == 0:
            print my_game, "/ 3 = Bazz"
	if my_game % 5 == 0:
	    print my_game, "/ 5 = Fizz"
play_games(my_game)
