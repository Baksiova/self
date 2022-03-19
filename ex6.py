def count_boomerangs(lst):
	return sum(lst[i] == lst[i-2] for i in range(2,len(lst)))

print(count_boomerangs([3, 2, 3, 2, 1, 5, 1, 2, 2, -2, 2]))