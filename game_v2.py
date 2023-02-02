""" Игра 'Угадай число'
Компьютер сам загадывает и угадывает число.
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
            break       # выход из цикла, если угадали
    return count


# Зачем нужен параметр random_predict, если функция работает и без него?
def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем угадывает наш подход

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []        # в этом списке будем сохранять количества попыток
    np.random.seed(1)   # инициализируем ГСЧ каждый раз одинаково для воспроизводимости результата
    random_array = np.random.randint(1, 101, size=1000)     # Загадаем 1000 чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

# Если импортируем как библиотеку, этот вызов функции не исполняется
if __name__ == "__main__":
    score_game(random_predict)      # раз от раза показывается "в среднем за 101 попытку"
