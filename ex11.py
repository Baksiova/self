def is_disarium(n):
    y = 0
    vysledok = []
    digit_string = str(n)
    print(digit_string)
    digit_map = map(int, digit_string)
    print(digit_list1)
    digit_list = list(digit_map)
    print(digit_list)

    for i in range(1, len(digit_list) + 1):
        vysledok.append(digit_list[y] ** i)
        if y <= len(digit_list):
            y = y + 1

    if sum(vysledok) == n:
        return True
    else:
        return False


print(is_disarium(135))