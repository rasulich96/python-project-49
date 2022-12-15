import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    # Т.к. делитель не может быть больше половины самого числа,
    # зараннее разделим его на 2, так сократим количество итераций
    div = number // 2
    while div > 1:
        if number == 1:
            return False
        if number % div == 0:
            return False
        else:
            div -= 1
    return True


def build_game():
    random_number = random.randint(1, 99)
    question = f'Question: {random_number}'
    result = is_prime(random_number)
    if is_prime(random_number) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, question
