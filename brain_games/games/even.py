#!/usr/bin/env/ python3
import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    result = ''
    if number % 2 == 0:
        result = 'yes'
        return result
    else:
        result = 'no'
        return result


def game_func():
    random_number = random.randint(1, 99)
    result = is_number_even(random_number)
    question = str(f'Question: {random_number}')
    return result, question
