#!/usr/bin/env/ python3
import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_func():
    random_number = random.randint(1, 99)
    result = ''
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    question = str(f'Question: {random_number}')
    return result, question
