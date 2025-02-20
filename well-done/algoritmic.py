import itertools
import re

class SequenceCounter:
    @staticmethod
    def count_sequences():
        alphabet = ['К', 'А', 'Т', 'Е', 'Р']
        count = 0
        for seq in itertools.product(alphabet, repeat=6):
            if seq[0] == 'Р' and seq[-1] == 'К':
                count += 1
        return count

class ExpressionCalculator:
    @staticmethod
    def calculate_expression():
        value = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
        return ExpressionCalculator.to_base_6(value)

    @staticmethod
    def to_base_6(n):
        digits = []
        while n:
            digits.append(n % 6)
            n //= 6
        return len(set(digits[::-1]))

class NumberFinder:
    @staticmethod
    def find_numbers():
        pattern = re.compile(r'12345\d7\d8')
        numbers = []
        for number in range(123450708, 123459798 + 1):
            if number > 10**9:
                break
            if pattern.match(str(number)) and number % 23 == 0:
                numbers.append(number)
        return numbers

    @staticmethod
    def create_table():
        numbers = NumberFinder.find_numbers()
        return [(number, number // 23) for number in sorted(numbers)]

# Вывод результатов
print(SequenceCounter.count_sequences())
print(ExpressionCalculator.calculate_expression())
for row in NumberFinder.create_table():
    print(row)
