import itertools

def count_sequences():
    """
    Возвращает количество последовательностей длины 6 в алфавите {К, А, Т, Е, Р},
    которые начинаются с 'Р' и заканчиваются на 'К'.

    Пример:
    >>> count_sequences()  # Последовательности: Р****К, где * — любая из 5 букв
    625
    """
    alphabet = ['К', 'А', 'Т', 'Е', 'Р']
    count = 0
    for seq in itertools.product(alphabet, repeat=6):
        if seq[0] == 'Р' and seq[-1] == 'К':
            count += 1
    return count

# Запуск доктестов
if __name__ == "__main__":
    import doctest
    doctest.testmod()