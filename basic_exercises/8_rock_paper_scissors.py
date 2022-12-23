"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""


def compare_selection(input1, input2):
    """
    :type input1: basestring
    :type input2: basestring
    """
    if input1 == input2:
        return "It's a tie!"
    elif input1 == 'rock':
        if input2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif input1 == 'scissors':
        if input2 == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif input1 == 'paper':
        if input2 == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."
        sys.exit()


operation = input('Type "c" to begin: ')
player_one = input("Please enter your name player one: ")
player_two = input("please enter your name player two: ")

while operation != 'q':
    selection_one = input("%s,rock, paper or scissors? " % player_one)
    selection_two = input("%s, rock, paper or scissors? " % player_two)
    print(compare_selection(selection_one, selection_two))
    operation = input('Type "q" to quit or "c" to continue: ')

