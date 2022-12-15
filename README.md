### Hexlet tests and linter status:
[![Actions Status](https://github.com/rasulich96/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/rasulich96/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/de483d8ab79fbbc9b9c3/maintainability)](https://codeclimate.com/github/rasulich96/python-project-49/maintainability)

<hr>

Добро пожаловать в Brain-games!

Реализация кода разделена на 3 ветви: движок игры, сама логика игры и скрипт запуска определенной игры.

В движок игры вынесены основные операции, которые повторяются в играх, т.е. приветствие с просьбой ввести имя игрока, вывод в терминал правила игры, получение правильного ответа и вопроса для игрока и сравнение правильного ответа с ответом игрока. А так же, в движке идет подсчет количества победных раундов. В каждой игре всегда по 3 раунда. Чтобы выиграть надо ответить правильно 3 раза подряд, любая ошибка и игра заканчивается.

<hr>

К существующим играм, можно добавлять и свою игру, движок их правильно обработает, если соблюдать некоторые правила:
 - Сама игра должна возвращать правильный ответ (переменная result) для сравнения с ответом пользователя и вопрос игры (переменная question);
 - Переменные result и question должны быть обязательно строковым типом;
 - Для описания правил игры можно использовать глобальную константу QUESTION. При запуске игры, после приветствия и ответа пользователя движок выводит в терминал содержимое этой константы;
 - Ответ игрока движок ожидает строкового типа, чтобы сравнивать с правильным ответом;
 - Ответ игрока не зависит от регистра букв, движок переделывает ответ игрока в строчные буквы. Поэтому при создании игры это надо учитывать.

<hr>

Игры запускаются через зараннее записанные скрипты. Скрипт вызывает главную функцию из движка (checking_result) и передает в него параметр - название игры, который мы импортирует из папки с играми.

В проекте можно вызывать следующие команды:
 - make build - собрать программу
 - make publish - отладить
 - make package-install - установить программу
 - make package-reinstall - переустановка программы
 - make install - установка poetry
 - make brain-even - запуск игры нахождения четного/нечетного числа
 - make brain-calc - запуск игры решения математических выражений
 - make brain-gcd - запуск игры нахождения НОД (наименьший общий делитель)
 - make brain-progression - запуск игры угадывания пропущенного числа
 - make brain-prime - запуск игры проверки на простое число
 - make lint - проверка чистоты кода через линтер flake8

Для работы проекта использовались следующие программы и их версии:
 1. python, версии выше 3.8
 2. prompt, версии выше 0.4
 3. poetry, вырсия выше 1.2
 4. flake8, версия выше 6.0 

<hr>

Ниже приведены аскинемы по запуску, выигрышу и проигрышу в различных играх:

Демонстрация сборки, отладки и переустановки программы:

[![asciicast](https://asciinema.org/a/jDdD4X9axO5Yrn55eNTBTPeP2.svg)](https://asciinema.org/a/jDdD4X9axO5Yrn55eNTBTPeP2)

<hr>

Игра brain-even. Демонстрация запуска, выигрыша и проигрыша в игре:

[![asciicast](https://asciinema.org/a/Xmd6itsMO95lPog74uwC3rggm.svg)](https://asciinema.org/a/Xmd6itsMO95lPog74uwC3rggm)

<hr>

Игра brain-calc. Демонстрация запуска, выигрыша и проигрыша в игре:

[![asciicast](https://asciinema.org/a/eSvRxTtySAr2SD3AKJBHirAZf.svg)](https://asciinema.org/a/eSvRxTtySAr2SD3AKJBHirAZf)

<hr>

Игра brain-gcd. Демонстрация запуска, выигрыша и проигрыша в игре:

[![asciicast](https://asciinema.org/a/KmoOj0dl7zRfEYcqCJfbE5rYf.svg)](https://asciinema.org/a/KmoOj0dl7zRfEYcqCJfbE5rYf)

<hr>

Игра brain-progression. Демонстрация запуска, выигрыша и проигрыша в игре:

[![asciicast](https://asciinema.org/a/Rxvkii4UmVCSdYGeOQsyqiHxO.svg)](https://asciinema.org/a/Rxvkii4UmVCSdYGeOQsyqiHxO)

<hr>

Игра brain-prime. Демонстрация запуска, выигрыша и проигрыша в игре:

[![asciicast](https://asciinema.org/a/2C53nA8f3rXkQf8V9sm95meJx.svg)](https://asciinema.org/a/2C53nA8f3rXkQf8V9sm95meJx)