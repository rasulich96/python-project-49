#!/usr/bin/env python3
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answe "no"'


def is_prime(number):
    result = 'yes'
    # Т.к. делитель не может быть больше половины самого числа,
    # зараннее разделим его на 2, так сократим количество итераций
    div = number // 2
    while div > 1:
        if number % div == 0:
            result = 'no'
            print(result)
            return result
        else:
            div -= 1
    return result


def game_func():
    random_number = random.randint(1, 99)
    question = f'Question: {random_number}'
    result = is_prime(random_number)
    return result, question
