#!/usr/bin/env python3
import random


QUESTION = 'What is the result of the expression?'


def get_random_expression():
    # Инициализируем два случайных номера и случайное математическое выражение
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
    return result, random_number_1, random_number_2, random_operation


def game_func():
    random_expression = get_random_expression()
    # Разворачиваем кортеж, полученный из get_random_expression
    result, number_1, number_2, random_operation = random_expression
    question = str(
        f'Question: {number_1} {random_operation} {number_2}'
    )
    return str(result), question
