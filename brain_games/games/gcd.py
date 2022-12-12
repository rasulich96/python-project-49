#!/usr/bit/env python3
import random
import math


QUESTION = 'Find the gratest common divisor of given numbers.'


def game_func():
    random_number_1 = random.randint(1, 99)
    random_number_2 = random.randint(1, 99)
    result = math.gcd(random_number_1, random_number_2)
    question = str(f'Question: {random_number_1} {random_number_2}')
    return str(result), question
