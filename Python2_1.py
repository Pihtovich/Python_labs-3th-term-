def Pascal_triangle(num):
    lstNum = [[1]]
    for i in range(1, num + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if not(j == 0 or j == i):
                row[j] = lstNum[i - 1][j - 1] + lstNum[i - 1][j]
        lstNum.append(row)
    return lstNum


print("==Треугольник Паскаля==")
countStr = int(input("Введите число строк: "))
result = Pascal_triangle(countStr)
for z in range(len(result)):
    print(result[z])


