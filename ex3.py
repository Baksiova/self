A = [6, 7, 8, 9, 10, 11, 12]
subset_of_A = set([6, 9, 12]) # the subset of A

result = [a for a in A if a not in subset_of_A]
print(result)