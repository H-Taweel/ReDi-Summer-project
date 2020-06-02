import random
from string import ascii_uppercase
import Gallow


def welcoming():
    print("This is HANGMAN GAME!")
    player_name = input("Please enter your name to play this game:\n").capitalize()
    print(f"Welcome to HANGMAN GAME {player_name}! You have 8 attempts to guess the full word!")
    print("There are multiple difficulty settings shown below, please choose one:")
    print("For Easy type E")
    print("For Medium type M")
    print("For Hard type H")
    return player_name


def difficulties(player_name):
    diff = input(f"{player_name}, which difficulty you'd like to play?:\n").upper()
    diffs = ["E", "M", "H"]
    while diff not in diffs:
        print("You did NOT choose any difficulty, please choose one:")
        diff = input().upper()
    if diff == 'E': #len(word) <= 4
        print(f"Well {player_name}, you've chosen Easy difficulty.")
        f = open("C:/Users/hisha/PycharmProjects/Hangman game/WordList_easy.txt", "r")
        easy_file = f.read().split()
        word = random.choice(easy_file)
    elif diff == 'M':
        print(f"Well {player_name}, you've chosen Medium difficulty.")
        f = open("C:/Users/hisha/PycharmProjects/Hangman game/WordList_medium.txt", "r")
        medium_file = f.read().split()
        word = random.choice(medium_file)
    elif diff == 'H':
        print(f"Well {player_name}, you've chosen Hard difficulty.")
        f = open("WordList_hard.txt")
        hard_file = f.read().split()
        word = random.choice(hard_file)
    return word


def gallow_board(incorrect_letters, secret_word, correct_letters):
    print(Gallow.gallow[len(incorrect_letters)])
    for letter in secret_word:
        if letter in correct_letters:
            print("\033[1;34m", letter, end=' ' + "\033[0m")  # correct
        else:
            print('_', end=' ')  # length of the secret word
    print('\n')
    print("\033[3;91m*****INCORRECT LETTERS*****\033[0m")
    for letter in incorrect_letters:
        print("\033[1;91m", letter, end=' ' + "\033[0m")
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def player_guess(incorrect_letters, secret_word, correct_letters): # Handling_errors:
    while True:
        guess = input("Guess a letter:\n").upper()  # Asking the player for input
        if guess in correct_letters or guess in incorrect_letters:  # If player already guessed the letter
            print("You have already guessed this letter")
        elif len(guess) > 1:  # If player inputs more than a letter
            print("Please enter only ONE letter at time")
        elif len(guess) == 0:  # If player inputs nothing or pressed Enter
            print("You entered NOTHING!! Please enter a letter")
        elif guess not in ascii_uppercase:  # If user inputs anything else but letters
            print("NOT VALID!! please enter ONLY letter") # We can use .isalpha to accept german letters
        else:
            break
    if guess in secret_word:  # Check player's guess
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)


def check_win(incorrect_letters, secret_word, correct_letters): # If user won or lost:
    if len(incorrect_letters) == 8:  # attempts = 8
        return 'loss'
    for i in secret_word:
        if i not in correct_letters:
            return 'no win'
    return 'win'


def play_game(player_name):
    secret_word = difficulties(player_name).upper()
    correct_letters = []
    incorrect_letters = []
    print(secret_word)
    print('The word contains', len(secret_word), 'letters')
    play_turn = True
    turn_count = 0
    while play_turn: # Looping the entire game till the user wins or looses
        gallow_board(incorrect_letters, secret_word, correct_letters)
        player_guess(incorrect_letters, secret_word, correct_letters)
        attempts = len(incorrect_letters)
        score = 1000
        points = score - (attempts * 125)
        '''result = {}'''

        win_condition = check_win(incorrect_letters, secret_word, correct_letters)
        if win_condition == 'loss':
            print(Gallow.gallow[-2])
            print(f"GAME OVER {player_name}! The word was {secret_word}")
            return None
        elif win_condition == 'win':
            print(Gallow.gallow[-1])
            print(f"Great {player_name}, YOU WON! The word was {secret_word}\nYour score is: {str(points)}")
            turn_count += 1
            with open('Scoreboard.txt', 'a') as file:
                file.write(player_name + " " + str(points) + "\n")
            return


def scoreboard():
   file_highscore = open('Scoreboard.txt' , 'r')
   scores = []
   for line in file_highscore.readlines():
      score_info = line.split()
      scores.append((score_info[0], int(score_info[1])))

   scores.sort(key = lambda x:x[1], reverse = True)
   print('The First 5 Highscores are:')
   for score, name in scores[:5]:
      print(name, score)


def end_game():
        while True:
            results = play_game(player_name)
            play_again = input('Would you like to play again? \nPlease type Yes(y) or No(n):\n').lower()
            yes_or_no = ['y', 'yes', 'no', 'n']
            while play_again not in yes_or_no:
                print('\033[91mPlease type "yes" or "y" to play again  OR\nIf you want to end this game please type "no" or "n"\033[0m')
                play_again = input('y/n: ').lower()
                print(play_again)

            if play_again == 'no' or play_again == 'n':
                print(f"Thank you for your time!")
                score_board = scoreboard()
                break
            elif play_again == 'yes' or play_again == 'y':
                print(f'Great! Game Restarted')

# the whole game:
player_name = welcoming()
end_game()