#!/usr/bin/env python3
import random


QUESTION = 'What is the result of the expression?'


def game_func():
    random_number_1 = random.randint(1, 99)
    random_number_2 = random.randint(1, 99)
    random_operation = random.choice('+-*')
    result = 0
    if random_operation == '+':
        result = random_number_1 + random_number_2
    elif random_operation == '-':
        result = random_number_1 - random_number_2
    else:
        result = random_number_1 * random_number_2
    question = str(
        f'Question: {random_number_1} {random_operation} {random_number_2}'
        )
    return str(result), question
