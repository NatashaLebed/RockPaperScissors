import random

name = input('Enter your name:')
print('Hello, ' + name)

#  user input options, that will be in thr game, if they input nothing, options = 'paper','scissors', 'rock'
choices = input().split(',')
if choices == ['']:
    choices = ['paper', 'scissors', 'rock']
print("Okay, let's start")

# Check if the name is in a rating file
# If 'yes' read score from file, else score = 0
rate_file = open('rating.txt')
for line in rate_file:
    if name == line.split()[0]:
        score = int(line.split()[1])
        break
    else:
        score = 0
rate_file.close()

# Play game Rock_Paper_Scissors until user input '!exit'
while True:
    user_choice = input()

    if user_choice == '!exit':
        print('Bye!')
        break
    if user_choice == '!rating':
        print(f'Your rating: {score}')
        continue
    if user_choice not in choices:
        print('Invalid input')
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
        score += 50
    else:
        n = choices.index(user_choice)
        ordered_options = choices[n + 1:] + choices[:n]
        user_win_options = ordered_options[:len(ordered_options) // 2]
        if computer_choice not in user_win_options:
            print(f'Well done. The computer chose {computer_choice} and failed')
            score += 100
        else:
            print(f'Sorry, but the computer chose {computer_choice}')
