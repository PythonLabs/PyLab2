def find_numbers():
    # модуль регулярного выражения
    import re
    pattern = re.compile(r'12345\d7\d8')
    numbers = []
    # Шаблон регулярного выражения
    for number in range(123450708, 123459798 + 1):
        if number > 10**9:
            break
        # Проверка соответствия чисел для шаблона
        if pattern.match(str(number)) and number % 23 == 0:
            numbers.append(number)
    return numbers

# Задание таблицы
def create_table():
    numbers = find_numbers()
    table = []
    for number in sorted(numbers):
        # Добавления картежа чисел, которые делятся на 23
        table.append((number, number // 23))
    return table

# Пример вывода таблицы
table = create_table()
for row in table:
    print(row)