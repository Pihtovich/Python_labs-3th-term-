# задание 0
# Задан список с числами. Напишите программу, которая выводит
# все элементы списка, которые больше предыдущего, в виде отдельного списка.

# вариант 1-й
hello_str = "Введите последовательность чисел: "
in_lst = [int(item) for item in input(hello_str).split()]
out_lst = [j for i, j in zip(in_lst, in_lst[1:]) if j > i]
print(out_lst)

# вариант 2-й
lst1 = []
input_str = int(input("К-во входных числе: "))
for i in range(0, input_str):
    elem = int(input())
    lst1.append(elem)

lst2 = []
for i in range(1, len(lst1)):
    if lst1[i] > lst1[i - 1]:
        lst2.append(lst1[i])
print(lst2)