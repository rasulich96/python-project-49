#!/usr/bit/env python3
import random
import math


QUESTION = 'Find the greatest common divisor of given numbers.'


def is_number_gcd():
    # Инициализируем два рандомных номера и находим их НОД
    random_number_1 = random.randint(1, 99)
    random_number_2 = random.randint(1, 99)
    result = math.gcd(random_number_1, random_number_2)
    return result, random_number_1, random_number_2


def game_func():
    result, random_number_1, random_number_2 = is_number_gcd()
    question = str(f'Question: {random_number_1} {random_number_2}')
    return str(result), question
