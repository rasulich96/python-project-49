#!/usr/bin/env python3
import random
import prompt
import sys
    

def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def is_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_random_number(start=1, end=99):
    random_number = random.randint(start, end)
    return random_number


def get_random_calc_operation():
    random_operation = random.choice('+-*/')
    return random_operation


def get_correct_answer_for_even_game(number):
    correct_answer = ''
    if is_number_even(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def get_correct_answer_for_calc_game(random_number_1, random_number_2, operation):
    result = 0
    if operation == '+':
        result = random_number_1 + random_number_2
        return result
    elif operation == '-':
        result = random_number_1 - random_number_2
        return result
    elif operation == '*':
        result = random_number_1 * random_number_2
        return result
    else:
        result = random_number_1 // random_number_2
        return result


def get_answer_even(random_number):
    print(f'Question: {random_number}')
    answer = prompt.string('You answer: ').lower()
    return answer


def get_answer_calc(random_number_1, random_number_2, operation):
    print(f'Question: {random_number_1} {operation} {random_number_2}')
    answer = prompt.int('You answer: ')
    return answer


def check_answer_even(random_number, answer, score, username):
    if is_number_even(random_number) is True and answer == 'yes':
        print('Correct!')
        score += 1
        return score
    elif is_number_even(random_number) is False and answer == 'no':
        print('Correct!')
        score += 1
        return score
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
            f"'{get_correct_answer_for_even_game(random_number)}'.")
        sys.exit(f"Let's try again, {username}!")


def check_answer_calc(
        random_number_1, random_number_2, operation, answer, score, username
    ):
    correct_answer = get_correct_answer_for_calc_game(
        random_number_1, random_number_2, operation
    )
    if correct_answer == answer:
        print('Correct!')
        score += 1
        return score
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
        f"'{correct_answer}'"
        )
        sys.exit(f"Let's try again, {username}!")


def win(username):
    print(f'Congratulations, {username}!')
