# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # С клавиатуры вводится цифра (от 1 до 4).
    # Вывести на экран названия месяцев,соответствующих времени года с номером (считать зиму временем года No 1).
    m = int(input('Введите номер времени года'))
    if m == 1:
        print('Зима')
    elif m == 2:
        print('Весна')
    elif m == 3:
        print('Лето')
    elif m == 4:
        print('Осень')
    else:
        print('Ошибка', file=sys.stderr)
