### Hexlet tests and linter status:
[![Actions Status](https://github.com/rasulich96/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/rasulich96/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/de483d8ab79fbbc9b9c3/maintainability)](https://codeclimate.com/github/rasulich96/python-project-49/maintainability)

Добро пожаловать в Brain-games!

Реализация кода разделена на 3 ветви: движок игры, сама логика игры и скрипт запуска определенной игры.

В движок игры вынесены основные операции, которые повторяются в играх, т.е. приветствие с просьбой ввести имя игрока, вывод в терминал правила игры, получение правильного ответа и вопроса для игрока и сравнение правильного ответа с ответом игрока. А так же, в движке идет подсчет количества победных раундов. В каждой игре всегда по 3 раунда. Чтобы выиграть надо ответить правильно 3 раза подряд, любая ошибка и игра заканчивается.

К существующим играм, можно добавлять и свою игру, движок их правильно обработает, если соблюдать некоторые правила:
    - Сама игра должна возвращать правильный ответ (переменная result) для сравнения с ответом пользователя и вопрос игры (переменная question);
    - Переменные result и question должны быть обязательно строковым типом;
    - Для описания правил игры можно использовать глобальную константу QUESTION. При запуске игры, после приветствия и ответа пользователя движок выводит в терминал содержимое этой константы;
    - Ответ игрока движок ожидает строкового типа, чтобы сравнивать с правильным ответом;
    - Ответ игрока не зависит от регистра букв, движок переделывает ответ игрока в строчные буквы. Поэтому при создании игры это надо учитывать.

Игры запускаются через зараннее записанные скрипты. Скрипт вызывает главную функцию из движка (checking_result) и передает в него параметр - название игры, который мы импортирует из папки с играми.

Ниже приведены аскинемы по запуску, выигрышу и проигрышу в различных играх:

Playing brain-even:
[![asciicast](https://asciinema.org/a/Qn2nzbI3hd3dFPLLib4qNTMDo.svg)](https://asciinema.org/a/Qn2nzbI3hd3dFPLLib4qNTMDo)

Playing brain-calc:
[![asciicast](https://asciinema.org/a/eSvRxTtySAr2SD3AKJBHirAZf.svg)](https://asciinema.org/a/eSvRxTtySAr2SD3AKJBHirAZf)

Playing brain-gcd:
[![asciicast](https://asciinema.org/a/KmoOj0dl7zRfEYcqCJfbE5rYf.svg)](https://asciinema.org/a/KmoOj0dl7zRfEYcqCJfbE5rYf)

Playing brain-progression:
[![asciicast](https://asciinema.org/a/Rxvkii4UmVCSdYGeOQsyqiHxO.svg)](https://asciinema.org/a/Rxvkii4UmVCSdYGeOQsyqiHxO)

Playing brain-prime:
[![asciicast](https://asciinema.org/a/2C53nA8f3rXkQf8V9sm95meJx.svg)](https://asciinema.org/a/2C53nA8f3rXkQf8V9sm95meJx)