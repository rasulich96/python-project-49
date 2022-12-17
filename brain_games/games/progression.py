import random


QUESTION = 'What number is missing in the progression?'


def get_random_progression():
    # Инициализируем пустой список, рандомную длину списка, рандомное начало
    # И рандомный шаг прогрессии
    lenght_random_progression = random.randint(5, 10)
    start_random_progression = random.randint(1, 20)
    step_progression = random.randint(1, 5)
    # Инициализируем список с началом раннее полученного начального значения
    random_progression = [start_random_progression]
    for number in range(lenght_random_progression):
        # Добавляем в список значения с вычислением шага
        random_progression.append(
            random_progression[number] + step_progression
        )
    return random_progression


def build_game():
    random_progression = get_random_progression()
    # Инициализация рандомного индекса для скрытия
    random_hidden_number = random.randint(0, len(random_progression) - 1)
    # Сохраняем значение рандомного индекса для проверки ответа пользователя
    result = random_progression[random_hidden_number]
    # Заменяем значение рандомного индекса на ..
    random_progression[random_hidden_number] = '..'
    # Убираем кавычки от скрытого номера
    question = f"Question: {' '.join(str(i) for i in random_progression)}"
    return str(result), question
