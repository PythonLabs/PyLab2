def find_numbers():
    import re
    pattern = re.compile(r'12345\d7\d8')
    numbers = []
    for number in range(123450708, 123459798 + 1):
        if number > 10**9:
            break
        if pattern.match(str(number)) and number % 23 == 0:
            numbers.append(number)
    return numbers

def create_table():
    numbers = find_numbers()
    table = []
    for number in sorted(numbers):
        table.append((number, number // 23))
    return table

# Пример вывода таблицы
table = create_table()
for row in table:
    print(row)