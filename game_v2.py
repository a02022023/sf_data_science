"""Игра "Угадай число".
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def fast_predict(number: int = np.random.randint(1, 101)) -> int:
    left, right = 1, 100    # границы, в которых находится угадываемое число (будут сужаться)
    count = 0               # счетчик попыток угадывания
    while True:
        count += 1
        predict_number = 100 if ((left == 99) and (right == 100)) else (left + right) // 2    # предполагаемое число
        if number < predict_number:
            right = predict_number
        elif number > predict_number:
            left = predict_number
        else:
            break   # число number угадано с count-й попытки
    return count


def score_game(predict_func) -> int:
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    array_size = 1000
    random_array = list(np.random.randint(1, 101, size=(array_size)))  # список загаданных чисел

    # Угадаем каждое загаданное число из random_array и запомним число попыток, за которое оно было угадано
    count_ls = list(map(predict_func, random_array))

    score = int(np.mean(count_ls))
    print(f"Размер выборки из загаданных чисел: {array_size}")
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    # score_game(random_predict)
    score_game(fast_predict)
