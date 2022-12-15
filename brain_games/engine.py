import prompt


def start_game(selected_game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    # Выводим на экран условие выбранной игры
    print(selected_game.QUESTION)
    score = 0
    while score != 3:
        # Забираем с каждой игры правильный результат и задаваемый вопрос
        result, question = selected_game.build_game()
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
