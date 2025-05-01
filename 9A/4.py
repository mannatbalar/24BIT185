lst = ['madam', 'Python', "malayalam", 12321]

for item in lst:
    if isinstance(item, str) and item == item[::-1]:
        print(item)