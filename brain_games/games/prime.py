import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    # Отрицательные числа не могут быть простыми
    if number <= 1:
        return False
    # Делим число на диапазон от до самого числа
    # range пройдет от 2х до Number - 1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def build_game():
    random_number = random.randint(1, 99)
    question = f'Question: {random_number}'
    result = is_prime(random_number)
    if is_prime(random_number):
        result = 'yes'
    else:
        result = 'no'
    return result, question
