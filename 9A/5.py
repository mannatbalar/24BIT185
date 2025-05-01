faculty_names = ['John', 'Sarah', 'Alexander', 'Matthew', 'Elizabeth']

long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print(long_names)