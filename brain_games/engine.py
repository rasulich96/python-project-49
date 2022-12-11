#!/usr/bin/env python3
import prompt
import sys


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def checking_result(select_game):
    username = welcome_user()
    # Выводим на экран условие выбранной игры
    print(select_game.QUESTION)
    score = 0
    while score != 3:
        result, question = select_game.game_func()
        print(question)
        answer = prompt.string('Your answer: ').lower()
        # Сначала проверим ошибку, чтобы сразу завершить программу при ошибке,
        # иначе будет лишняя проверка условия
        if answer != result:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{result}'"
            )
            # завершаем программу при ошибке
            return print(f"Let's try again, {username}!")
        else:
            print('Correct!')
            score += 1
    print(f'Congratulations, {username}!')
