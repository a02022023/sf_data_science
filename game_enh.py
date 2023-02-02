""" 26.01.2023 - Игра 'Угадай число', улучшенная версия """
import numpy as np
left, right = 1, 100
left_bracket, right_bracket = '[', ']'
number = np.random.randint(left, right+1)       # загадываем число
count = 0                                       # количество попыток угадывания

while True:
    print('')
    count += 1
    guessed_number = int(input(f"Попытка #{count}: Угадай число из диапазона {left_bracket}{left}; {right}{right_bracket}: "))
    if number < guessed_number:
        print(f"Число должно быть меньше {guessed_number}")
        right = guessed_number
        right_bracket = ')'
    elif number > guessed_number:
        print(f"Число должно быть больше {guessed_number}")
        left = guessed_number
        left_bracket = '('
    else:
        print(f"Ты угадал с {count}-й попытки, это число {number}!")
        break
