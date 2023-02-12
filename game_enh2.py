""" 10.02.2023 - Игра 'Угадай число' 
Программа сама загадывает число и сама же угадывает путем деления отрезка пополам.
Число от 1 до 100 угадывается максимум за 8 попыток.
"""
import numpy as np
left, right = 1, 100
b_left, b_right = '[', ']'                      # b - сокращение от bracket
# number = np.random.randint(left, right+1)       # загадываем число из диапазона [left; right]
number = 100
count = 0                                       # счетчик попыток угадывания

while True:
    print('')
    count += 1
    
    predict_number = 100 if ((left == 99) and (right == 100)) else (left + right) // 2    # предполагаемое число

    print(f"Попытка #{count}, диапазон {b_left}{left}; {right}{b_right}: предположим, что это число {predict_number}")
    if number < predict_number:
        print(f"Число должно быть меньше {predict_number}")
        right = predict_number
        b_right = ')'
    elif number > predict_number:
        print(f"Число должно быть больше {predict_number}")
        left = predict_number
        b_left = '('
    else:
        print(f"Число {number} угадано с {count}-й попытки")
        break
