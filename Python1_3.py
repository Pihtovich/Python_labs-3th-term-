numLst = ""
num = int(input("Введите число: "))
copyNum, countSpaces = num, 1
while copyNum // 10:
    copyNum //= 10
    countSpaces += 1
print("Разрядность числа: ", countSpaces)

for i in range(1, num + 1):
    numLst += str(i) + " "
    resStr = " " * (num - i) + str(numLst)
    counter = len(numLst.replace(' ', '')) - 1
    while counter > 0:
        resStr += numLst[counter - 1]
        counter -= 1
    print(resStr + " " * (num - i))
