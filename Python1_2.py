def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("==Треугольник Паскаля==")
num = int(input("Введите число строк: ")
for i in range(1, num + 1):
    countNum = fibonacci(i)
    for i in range(1, countNum):

