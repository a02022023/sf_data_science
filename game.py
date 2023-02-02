""" Игра 'Угадай число' """
import numpy as np
number = np.random.randint(1, 101)      # загадываем число
count = 0                               # количество попыток угадывания

while True:
    guessed_number = int(input('Угадай число от 1 до 100: '))
    count += 1
    if guessed_number > number:
        print(f"Число должно быть меньше {guessed_number}")
    elif guessed_number < number:
        print(f"Число должно быть больше {guessed_number}")
    else:
        print(f"Ты угадал с {count}-й попытки, это число {number}!")
        break
