import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def build_game():
    random_number = random.randint(1, 99)
    result = ''
    if is_number_even(random_number) is True:
        result = 'yes'
    else:
        result = 'no'
    question = str(f'Question: {random_number}')
    return result, question
