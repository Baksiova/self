def count_boomerangs(lst):
	return sum(lst[i-2]==lst[i]!=lst[i-1] for i in range(2,len(lst)))

print(count_boomerangs([3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]))