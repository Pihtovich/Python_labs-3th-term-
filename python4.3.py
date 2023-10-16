def get_dictionary_from_list(lst):
    dictionary = dict.fromkeys(lst, 0)
    for s in lst:
        dictionary[s] = dictionary.get(s) + 1
    return [*dictionary.values()]


in_lst = []
length = int(input("Введите длину списка строк: "))
for i in range(length):
    in_lst.append(input())

result = get_dictionary_from_list(in_lst)
print(*result, sep=' ')


