def generate_tuples(end):
    
    return [(x, x**2, x**3) for x in range(1, end + 1)]

end_value = 5
result = generate_tuples(end_value)
print(f"Tuples from 1 to {end_value}:")
for item in result:
    print(item)
