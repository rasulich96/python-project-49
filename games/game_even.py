#!/usr/bin/env/ python3
from engine import (
    welcome_user, get_random_number, get_answer_even, check_answer_even,
    get_question_even_game, win
)


def brain_even():
    username = welcome_user()
    score = 0
    get_question_even_game()
    while score < 3:
        random_number = get_random_number(1, 99)
        answer = get_answer_even(random_number)
        score = check_answer_even(random_number, answer, score, username)
    win(username)
