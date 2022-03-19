numbers = [1,2,3,4,5]


def return_power(number, power =2):
    return number ** power

temp = []
for number in numbers:
    temp.append(return_power(number))
print(temp)
map(return_power(, numbers))