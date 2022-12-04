#!/usr/bin/env python3
from engine import (
    welcome_user, get_random_number, get_random_calc_operation,
    get_answer_calc, check_answer_calc, win
    )


QUESTION = 'What is the result of the expression?'

def brein_calc():
    username = welcome_user()
    score = 0
    print(QUESTION)
    while score < 3:
        random_number_1 = get_random_number(1, 99)
        random_number_2 = get_random_number(1, 99)
        operation = get_random_calc_operation()
        answer = get_answer_calc(random_number_1, random_number_2, operation)
        score = check_answer_calc(
            random_number_1, random_number_2, operation, answer,
            score, username
        )
    win(username)
