import itertools
import re

#Добавить возможность ввода своих значений от пользователя

class SequenceCounter:
    def count_sequences(self, word):
        alphabet = list(word)
        count = 0
        for seq in itertools.product(alphabet, repeat=len(word)):
            if seq[0] == word[-1] and seq[-1] == word[0]:
                count += 1
        return count

word = input("Введите слово: ")
counter = SequenceCounter()
print("Количество последовательностей:", counter.count_sequences(word))


class ExpressionCalculator:
    @staticmethod
    def calculate_expression(base):
        value = base ** 6 + base ** 4 + (base // 6) ** 6 - 6 ** 14 - 24
        return ExpressionCalculator.to_base_6(value)

    @staticmethod
    def to_base_6(n):
        digits = []
        while n:
            digits.append(n % 6)
            n //= 6
        return len(set(digits[::-1]))

base = int(input("Введите основание степени: "))
print("Результат выражения:", ExpressionCalculator.calculate_expression(base))

class NumberFinder:
    @staticmethod
    def find_numbers(start, end):
        pattern = re.compile(r'12345\d7\d8')
        numbers = []
        for number in range(start, end + 1):
            if number > 10**9:
                break
            if pattern.match(str(number)) and number % 23 == 0:
                numbers.append(number)
        return numbers

    @staticmethod
    def create_table(start, end):
        numbers = NumberFinder.find_numbers(start, end)
        return [(number, number // 23) for number in sorted(numbers)]

start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))
for row in NumberFinder.create_table(start, end):
    print(row)
