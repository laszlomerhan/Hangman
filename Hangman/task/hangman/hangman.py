import random

while True:
    print('H A N G M A N\n')
    choose = input('Type "play" to play the game, "exit" to quit: ')
    if choose == 'play':

        random_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
        guessed_word = "-" * len(random_word)
        lst = []
        count = 0
        print(f'\n{guessed_word}')

        while count < 9:
            guess = input('Input a letter: ')

            if guess == '' or len(guess) > 1:
                print("You should input a single letter")
            elif guess.isupper() or not guess.isalpha():
                print("Please enter a lowercase English letter")
            elif guess in lst:
                print("You've already guessed this letter")
            elif guess not in random_word:
                print("That letter doesn't appear in the word")
                count += 1
                if count == 8:
                    print("You lost!\n")
                    break
            else:
                for i in range(0, len(random_word)):
                    if random_word[i] == guess:
                        guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
                if guessed_word == random_word:
                    print(f'You guessed the word {guessed_word}!\nYou survived!\n')
                    break
            lst.append(guess)
            print(f'\n{guessed_word}')
    else:
        break
