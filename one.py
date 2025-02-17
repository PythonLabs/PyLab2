import itertools

def count_sequences():
    alphabet = ['К', 'А', 'Т', 'Е', 'Р']
    count = 0
    for seq in itertools.product(alphabet, repeat=6):
        if seq[0] == 'Р' and seq[-1] == 'К':
            count += 1
    return count

print(count_sequences())