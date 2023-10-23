def get_composition(_lst):
    comp = 1
    for i in range(len(_lst)):
        comp *= _lst[i]
    return comp


fin = open("input1.txt", "r")
in_lst = fin.readline().split()
fin.close()

lst = list(map(int, in_lst))
f = open('output.txt','w')
f.write(str(get_composition(lst)))
fin.close()
