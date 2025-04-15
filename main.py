import random

# initialize variables
word_bank = [   
    'adventure', 'balance', 'creativity', 'determination', 'empathy', 'growth', 'leadership', 
    'motivation', 'respect', 'success', 'teamwork', 'trust', 'wisdom', 'inspiration', 'kindness', 
    'learning', 'peace', 'reflection', 'resilience', 'vision'
]
word = random.choice(word_bank)
guessed_word = ['_'] * len(word)
attempts = 10

# main game loop
while attempts > 0:
    print('\nCurrent word:' + ' '.join(guessed_word))
    guess = input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Correct guess!')
    else:
        attempts -= 1
        print(f'Incorrect guess! Attempts left: {attempts}')
    if '_' not in guessed_word:
        print(f'Congratulations! You guessed the word: {word}')
        break

if '_' in guessed_word:
    print(f'Sorry, you ran out of attempts. The word was: {word}')


