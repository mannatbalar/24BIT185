def create_array(x, y, z, value):
   
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

array = create_array(3, 4, 5, 'n')

for i, matrix in enumerate(array):
    print(f"Layer {i}:")
    for row in matrix:
        print(row)
    print()
