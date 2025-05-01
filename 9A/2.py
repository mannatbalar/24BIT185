list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 1, 7, 1, 2, 0]

result = list(map(lambda x, y: x + y, list1, list2))
print(result)