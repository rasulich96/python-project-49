#!/usr/bin/env/ python3
import random
import prompt
import sys


def main():
    print('Welcome to the Brain Games')
    brain_even()


def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}! ')
    return username


def is_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def brain_even():
    username = welcome_user()
    score = 0
    correct_answer = ''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while score < 3:
        random_number = random.randint(1, 99)
        print(f'Question: {random_number}')
        answer = prompt.string('You asnwer: ').lower()
        if is_number_even(random_number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if is_number_even(random_number) is True and answer == 'yes':
            score += 1
            print('Correct!')
        elif is_number_even(random_number) is False and answer == 'no':
            score += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            sys.exit(f"Let's try again, {username}!")
    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    main()
