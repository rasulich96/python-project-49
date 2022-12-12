#!/usr/bin/env python3
import random


QUESTION = 'What number is missing in the progression?'


# Возможно это можно было сделать в одну строчку через функции,
# но функции мы еще не прошли :с
def get_random_progression():
    # Инициализируем пустой список, рандомную длину списка, рандомное начало
    # И рандомный шаг прогрессии
    random_progression = []
    lenght_random_progression = random.randint(5, 10)
    start_random_progression = random.randint(1, 20)
    step_progression = random.randint(1, 5)
    for number in range(lenght_random_progression):
        # Если список пустой, то добавляем начальное значение прогрессии
        if random_progression == []:
            random_progression.append(start_random_progression)
            continue
        # Добавляем в список значения с вычислением шага
        # [number - 1] нужен т.к. в данной итерации еще нет индекса number
        # а прогрессия у нас предыдущий индекс + шаг прогрессии
        random_progression.append(random_progression[number - 1] + step_progression)
    # Инициализация рандомного индекса для скрытия
    random_hidden_number = random.randint(0, lenght_random_progression - 1)
    # Сохраняем значение рандомного индекса для проверки ответа пользователя
    result = random_progression[random_hidden_number]
    # Заменяем значение рандомного индекса на ..
    random_progression[random_hidden_number] = '..'
    return result, random_progression


def game_func():
    result, random_progression = get_random_progression()
    # Убираем кавычки от скрытого номера
    question = str(f"Question: {' '.join(str(i) for i in random_progression)}")
    return str(result), question
