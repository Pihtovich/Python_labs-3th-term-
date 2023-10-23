in_dict = {}
with open("input3.txt", "r", encoding='utf-8') as file1:
    for line in file1:
        string = line.rstrip()
        in_dict[line[:len(string) - 1]] = string[-1]
sort_dict = dict(sorted(in_dict.items(), key=lambda x: x[1], reverse=True))
file1.close()

file2 = open("output.txt", "w", encoding='utf-8' )
lst = list(sort_dict.keys())
for name in lst[:2]:
    string = name + str(sort_dict.get(name)) + "\n"
    file2.write(string)