def calculate_expression():
    """
    Вычисляет значение выражения 216*6 + 216*4 + 36*6 - 6*14 - 24,
    переводит его в систему счисления с основанием 6 и возвращает количество уникальных цифр.

    Пример:
    >>> calculate_expression()  # Значение выражения: 216*6 + 216*4 + 36*6 - 6*14 - 24 = 2160
    3  # В числе 2160 в шестеричной системе (14400) уникальные цифры: 1, 4, 0
    """
    value = 216 * 6 + 216 * 4 + 36 * 6 - 6 * 14 - 24

    def to_base_6(n):
        digits = []
        while n > 0:
            digits.append(n % 6)
            n //= 6
        return digits[::-1]  # Возвращаем цифры в правильном порядке

    base_6_digits = to_base_6(value)
    unique_digits = set(base_6_digits)
    return len(unique_digits)

# Запуск доктестов
if __name__ == "__main__":
    import doctest
    doctest.testmod()