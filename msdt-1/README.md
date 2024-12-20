# Современные средства разработки ПО

## Лабораторная 1 "Стандарты кодирования"
В рамках данной лабораторной работы требуется продемонстрировать способность приводить код на python к стандартам кодирования (PEP8 или любому иному набору стандартов, например, описанному в лекции).

## Задание на лабораторную работу
1. Создать отдельную ветку в своем [форке](https://docs.github.com/en/get-started/quickstart/fork-a-repo) данного репозитория.
2. Взять произвольный существующий код на python (свой старый, другого студента, найденный в интернете);
3. Привести код в соответствие с [PEP8](https://peps.python.org/pep-0008/) или иным набором стандартов, например, описанным в лекциях (по крайней мере часть модулей, если их много);
4. Рекомендуетмся закоммитить изменения в несколько коммитов. Каждый коммит должен соответствовать применению отдельного правила (PEP8 или иного набора стандартов);
5. Открыть [пул-риквест](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) в иcходный репозиторий и ждать ревью.
_Убедительная просьба указывать свою фамилию, номер группы и номер лабораторной в названии пул риквеста_

## Условия сдачи
* Осмысленное название коммитов обязательно (лучше на русском, если на английском не вывозите),
* Один коммит = один исправленный аспект, например *правила именования переменных*, *правила именования функций*, *пробелы вокруг операторов* и т.д.
* Размер исходного кода - не менее __300__ строк,
* Исходный код и вносимые правки не должны повторяться среди студентов одной группы,
* Должно быть применено минимум **5** различных правил оформления кода,
* В описании пул-риквеста есть ссылка на исходный источник редактируемого кода.

## Ремарки:
Работать с git вы можете так, как вам удобно:
* через интерфейс [командной строки](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
* через [плагин](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#fetch) в IDE,
* через десктопный клиент, типа [такого](https://desktop.github.com/).

Если вы столкнулись с непреодолимыми трудностями в ходе выполнения лабораторной работы, вы можете задать вопрос в:
* телеграм-чате предмета,
* преподавателю напрямую в телеграм: @RumyantsevN1k1ta


## Ход выполнения

### Форматирование
1. Добавлены пробелы между математическими операторами
2. Заменены одинарные на двойные кавычки в docstring
3. Имена классов приведены к PascalCase
4. Имена методов приведены к snake_case
5. Кавычки в коде приведены к единому стандарту
6. Код отформатирован с помощью black
