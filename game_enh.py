""" 02.02.2023 - Игра 'Угадай число', улучшенная версия с делением отрезка пополам"""
import numpy as np
left, right = 1, 100
b_left, b_right = '[', ']'                      # b - сокращение от bracket
number = np.random.randint(left, right+1)       # загадываем число
count = 0                                       # счетчик попыток угадывания

while True:
    print('')
    count += 1
    # Указываем номер текущей попытки и просим ввести угаданное число
    guessed_number = int(input(f"Попытка #{count}: Угадай число из диапазона {b_left}{left}; {right}{b_right}: "))
    if number < guessed_number:
        print(f"Число должно быть меньше {guessed_number}")
        right = guessed_number
        b_right = ')'
    elif number > guessed_number:
        print(f"Число должно быть больше {guessed_number}")
        left = guessed_number
        b_left = '('
    else:
        print(f"Ты угадал с {count}-й попытки, это число {number}!")
        break
