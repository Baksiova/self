def count_boomerangs(arr):
    x= 0
    counter = 0
    for n in range(2,(len(arr))):
        if n == arr[x+2]:
            counter = counter+1

    x = x+1
    return counter

print(count_boomerangs([5, 6, 6, 7, 6, 3, 9]))

