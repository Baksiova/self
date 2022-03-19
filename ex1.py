
def show_the_love(lst):
    global min
    m=min(lst)
    lst.remove(min(lst))
    l1 = [int(i) - 1 / 4 * int(i) for i in lst]
    min1 = sum([1 / 4 * int(i) for i in lst]) + m

    for x in l1:
        x =int(x)
        l1 = [x - 1 / 4 * x for x in lst]
        l1.append(int(min1))




    print(l1)
    return l1
print(show_the_love([16, 10, 8]))

