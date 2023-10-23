in_lst = []
with open("input2.txt", "r") as file1:
    for line in file1:
        in_lst.append(line.strip())
out_lst = list(map(int, in_lst))
out_lst.sort()
file1.close()

file2 = open("output.txt", "w")
for i in range(len(out_lst)):
    file2.write(str(out_lst[i]) + " ")
file2.close()


