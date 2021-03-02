import random

print('H A N G M A N\n')

random_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_word = "-" * len(random_word)
print(guessed_word)
count = 0

while count < 9:
    guess = input('Input a letter: ')

    if guess not in random_word:
        print("That letter doesn't appear in the word")
        count += 1
        if count == 8:
            print('You lost!')
            break
    elif guess in guessed_word:
        print("No improvements")
        count += 1
        if count == 8:
            print('You lost!')
            break
    else:
        for i in range(0, len(random_word)):
            if random_word[i] == guess:
                guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
                if guessed_word == random_word:
                    print('You guessed the word!\nYou survived!')
                    exit()
    print(f'\n{guessed_word}')
