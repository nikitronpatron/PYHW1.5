# Создайте функцию генератор чисел Фибоначчи

n = int(input('Enter N: '))

def fibonacci_sequence(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

fibonacci_numbers = fibonacci_sequence(n)
print(fibonacci_numbers)