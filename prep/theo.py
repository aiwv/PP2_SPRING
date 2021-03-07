# преобразовать лист с туплами в дикт
color_counts = [('red', 2), ('green', 1), ('blue', 3), ('purple', 5)]
colors = dict(color_counts)
print(colors)

# """Возвращает True, если последовательность является палиндромом."""
def palindromic(sequence):
    for i, item in enumerate(sequence):
        if item != sequence[-(i+1)]:
            return False
    return True
sequence = input()
print(palindromic(sequence))


# Zip используется для перебора сразу нескольких объектов одновременно.
one_iterable = [2, 1, 3, 4, 7, 11]
another_iterable = ['P', 'y', 't', 'h', 'o', 'n']
for n, letter in zip(one_iterable, another_iterable):
    print(letter, n)


# reverse
numbers = [2, 1, 3, 4, 7]
numbers.reverse()
for n in numbers:
    print(n, end=' ')


# palindrome 2
def palindromic(sequence):
    for n, m in zip(sequence, reversed(sequence)):
        if n != m:
            return False
    return True

sequence = input()
print(palindromic(sequence))


# sum
numbers = [2, 1, 3, 4, 7, 11, 18]
print(sum(n for n in numbers))


# sorted
numbers = [1, 8, 2, 13, 5, 3, 1]
words = ["python", "is", "lovely"]
print(sorted(words,  key = len))
# max to min:
print(sorted(numbers, reverse=True)) 