import re
import random

def main():
    minesweeper_win_count = 0
    hangman_win_count = 0

    choice = 0
    while choice != 5:
        mainMenu()
        choice = input('Choice: ')
        print('')

        # minesweeper
        if choice == '1':
            minesweeper_win_count += minesweeper(minesweeper_win_count)
        # hangman
        elif choice == '2':                
            hangman_win_count += hangman(hangman_win_count)
        # random
        elif choice == '3':
            rand_int = random.randint(1,2)
            if rand_int == 1:
                minesweeper(minesweeper_win_count)
            if rand_int == 2:
                hangman(hangman_win_count)
        # stats
        elif choice == '4':
            stats(minesweeper_win_count, hangman_win_count)
        # about
        elif choice == '5':                
            about()
        # exit
        elif choice == '6':
            exit(randomGoodbye() + '\n')
        else:                
            print('Invalid input. Valid inputs are: 1, 2, 3, 4, 5')


            
# --------- MENU ----------
def mainMenu():
    print('')
    print('~ THE PROCRASTINATION STATION ~')
    print('')
    print(randomHello())
    print('')
    # MAIN MENU
    print('  ~  MAIN MENU  ~  ')
    print('-------------------')
    print('| 1) Minesweeper  |')
    print('-------------------')
    print('| 2)   Hangman    |')
    print('-------------------')
    print('| 3) Random Game  |')
    print('-------------------')
    print('| 4)    Stats     |')
    print('-------------------')
    print('| 5)    About     |')
    print('-------------------')
    print('| 6)    Exit      |')
    print('-------------------')
    print('')


# --------- 4) ABOUT ---------
def about():
    print('''
    -------------------------------
    | THE PROCRASTINATION STATION |
    -------------------------------
    |  Developed by Maya Savino   |
    |  In November 2022           |
    |  For NMT                    |
    -------------------------------
    
    ''')
    # leave
    menuOrExit()


# --------- STATS ---------
def stats(minesweeper_win_count, hangman_win_count):
    print(f'''
    --------------------------
    |  ~    STATISTICS    ~  |
    --------------------------
    --------------------------
    | MINESWEEPER |  {minesweeper_win_count}
    ---------------
    |   HANGMAN   |  {hangman_win_count}
    ---------------

    ''')
    # leave
    menuOrExit()
    


# --------- GAMES ---------

# HANGMAN
def hangman(hangman_win_count):

    win_count = 0
    man = '''
 _____
 |    
 |    
_|_    '''
    man_parts = ('O', '|', '/', '\\', '/', '\\') #lol
    wrong_guesses = ''

    print('')
    print('''-------------------''')
    print('''| ~   HANGMAN   ~ |''')
    print('''-------------------''')

    # get choice for random vs custom words
    word = hangmanWords()
    print(word) #

    # generate game
    board = ''
    for letter in str(word):
        board += '_ '

    # play
    wrong_guess_count = 0
    while wrong_guess_count < 6:

        print(man)
        print('')
        print(wrong_guesses)
        print('')
        print(board)
        print('')

        letter_guess = str(input('Letter: ')).lower()
        if re.search('[a-z]+', letter_guess) and len(letter_guess) == 1:
            if letter_guess in word:
                locations = []
                for index, letter in enumerate(word):
                    if letter == letter_guess:
                        locations.append(index)
                # add to board
                for location in locations:
                    board = board[:location*2] + word[location] + board[(location*2)+1:]
                # check for win
                if '_' not in board:
                    win_count += 1
                    print(man)
                    print('')
                    print('VICTORY')
                    print('')
                    print(wrong_guesses)
                    print('')
                    print(board)
                    print('')
                    print('Word: ' + word)
                    print('')
                    # play again?
                    again = playAgain(win_count)
                    if again == 'y':
                        hangman(hangman_win_count)
                    else:
                        return again
            # draw hangman
            elif letter_guess not in word:
                wrong_guesses += (letter_guess + ' ')
                wrong_guess_count += 1
                if wrong_guess_count == 1:
                    man = man[:13] + man_parts[0] + man[13:]
                if wrong_guess_count == 2:
                    man = man[:21] + man_parts[1] + man[21:]
                if wrong_guess_count == 3:
                    man = man[:20] + man_parts[2] + man[21:]
                if wrong_guess_count == 4:
                    man = man[:22] + man_parts[3] + man[22:]
                if wrong_guess_count == 5:
                    man = man[:29] + man_parts[4] + man[29:]
                if wrong_guess_count == 6:
                    man = man[:31] + man_parts[5]
                    print(man)
                    print('')
                    print('GAME OVER')
                    print('')
                    print(wrong_guesses)
                    print('')
                    print(board)
                    print('')
                    print('Word: ' + word)
                    print('')
        else:
            print('Invalid guess - enter a letter.')

    # play again?
    again = playAgain(win_count)
    if again == 'y':
        hangman(hangman_win_count)
    else:
        return again


# MINESWEEPER
def minesweeper(minesweeper_win_count):
    win_count = 0

    print('')
    print('''-------------------''')
    print('''| ~ MINESWEEPER ~ |''')
    print('''-------------------''')
 
    board = '''

          1     2     3     4     5
        _____________________________
       |     |     |     |     |     |
   1   |  M  |  2  |  M  |  2  |  M  |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   2   |  2  |  2  |  2  |  2  |  2  |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   3   |  M  |  2  |  2  |  M  |  2  |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   4   |  3  |  M  |  4  |  M  |  2  |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   5   |  M  |  2  |  3  |  M  |  2  |
       |_____|_____|_____|_____|_____|

     '''
    
    board_display = '''

          1     2     3     4     5
        _____________________________
       |     |     |     |     |     |
   1   |     |     |     |     |     |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   2   |     |     |     |     |     |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   3   |     |     |     |     |     |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   4   |     |     |     |     |     |
       |_____|_____|_____|_____|_____|
       |     |     |     |     |     |
   5   |     |     |     |     |     |
       |_____|_____|_____|_____|_____|

     '''
    print(board)
    print(board_display)

    choice = ''
    while choice != 'M':
        # choose square
        x = ''
        y = ''
        while not (x == '1' or x == '2' or x == '3' or x == '4' or x == '5') or not (y == '1' or y == '2' or y == '3' or y == '4' or y == '5'):
            x = input('X axis: ')
            y = input('Y axis: ')
            if not (x == '1' or x == '2' or x == '3' or x == '4' or x == '5'):
                print('Invalid input - Enter 1-5 for the x axis.')
            if not (y == '1' or y == '2' or y == '3' or y == '4' or y == '5'):
                print('Invalid input - Enter 1-5 for the y axis.')

        # determine actual board location
        if x == '1':
            x_location = (125, 131, 137, 143, 149)
        if x == '2':
            x_location = (242, 248, 254, 260, 266)
        if x == '3':
            x_location = (359, 365, 371, 377, 383)
        if x == '4':
            x_location = (476, 482, 488, 494, 500)
        if x == '5':
            x_location = (593, 599, 606, 611, 617)

        if y == '1':
            location = x_location[0]
        if y == '2':
            location = x_location[1]
        if y == '3':
            location = x_location[2]
        if y == '4':
            location = x_location[3]
        if y == '5':
            location = x_location[4]

        # flag or test
        f_or_t = ''
        while f_or_t != 'f' and f_or_t != 't':
            f_or_t = (input('Flag or Test? (F/t): ')).lower()
            # flag
            if f_or_t == 'f':
                board_display = board_display[:location] + 'F' + board_display[(location+1):]
                print(board_display)
            # test
            elif f_or_t == 't':
                # losing
                if board[location] == 'M':
                    print(board)
                    print('KABOOM! YOU LOSE')
                    print('')
                    choice = 'M'
                    # play again?
                    again = playAgain(win_count)
                    if again == 'y':
                        minesweeper(minesweeper_win_count)
                    else:
                        return again
                # winning
                elif board_display == board.replace('M', 'F'):
                    print('CONGRATULATIONS!!! YOU WIN!!!')
                    win_count += 1
                    # play again?
                    again = playAgain(win_count)
                    if again == 'y':
                        minesweeper(minesweeper_win_count)
                    else:
                        return again
                # update board
                else:
                    board_display = board_display[:location] + board[location] + board_display[(location+1):]
                    print(board_display)
            else:
                print('Invalid input - Enter "F" to flag or "T" to test.')


# RANDOMIZED WELCOME MESSAGE
def randomHello():
    messages = ("Let's giggity get crackity lackin'", "Shouldn't you be studying?", "Due today, do tomorrow. Let's play.", 
                "Don't worry, I'm sure your final project will only take an hour. You don't have to start it right now.",
                "Welcome, I guess...", "Sup b- I mean friend.")
    choice = random.randint(0,5)
    message = messages[choice]
    return message

# RANDOMIZED GOODBYE MESSAGE
def randomGoodbye():
    messages = ("You sure you need to go?", "Come on, just one more. Those assignments can wait.", "See you in an hour.",
                "I'll miss you :(", "Come back after you feel 1 second of frustration doing your work.", "Duces.")
    choice = random.randint(0,5)
    message = messages[choice]
    return message

# PLAY AGAIN? (GAMES)
def playAgain(win_count):
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = (input('Play again? (Y/n): ')).lower()
        if play_again == 'y':
            return 'y'
        elif play_again == 'n':
            return win_count
        else:
            print('Invalid input - Enter "Y" or "N"')

# LEAVE OR EXIT? (STATS/ABOUT)
def menuOrExit():
    menu_or_exit = ''
    while menu_or_exit != 'r' and menu_or_exit != 'e':
        menu_or_exit = (input('Return to main menu or exit arcade? (R/e): ')).lower()
        if menu_or_exit == 'r':
            return 0
        elif menu_or_exit == 'e':
            exit('\n' + randomGoodbye() + '\n')    

def hangmanWords():
    # random or custom, is file valid
    while True:
        rand_or_cust = (input('Random or custom words? (R/c): ')).lower()
        # random
        if rand_or_cust == 'r': 
            filename = 'hangman_words.txt'
        # custom
        elif rand_or_cust == 'c':
            filename = input('Enter the name of the file containing your words: ')
        else:
            print('Invalid input - enter "R" or "C"')
            hangmanWords()
        # open file
        try:
            with open(filename, 'r') as words_file:
                text = words_file.read()
                words = text.split(' ')
                rand_word = random.randint(0, len(words)-1)
                word = words[rand_word]
                return word
        except FileNotFoundError:
            print('File not found. Did you add the file to the folder containing the game file?')
        except IsADirectoryError:
            print('You entered the name of a directory. Did you add .txt at the end?')


if __name__ == '__main__':
    main()