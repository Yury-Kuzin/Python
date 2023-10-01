"""
    Именованные параметры

    Обычно параметры функции передаются позиционно, т.е. зависят от порядка их передачи в функцию.
    Но есть возможность указывать имя параметра при передаче ему значения.

    Если же необходимо ограничить использование именованных параметров, можно разделять
    именованные параметры от позиционных при помощи символов '*' и '/'.

    * - означает начало именованных параметров, которые можно передать ТОЛЬКО по имени
    / - означает, что параметры, которые идут ДО символа / можно передавать только позиционно

"""


def convert_to(num, base_from, /, base_to):
    return '000'


print(convert_to('14', 16, base_to=10))
