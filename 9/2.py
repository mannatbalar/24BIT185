def compute(n):
    
    n_str = str(n)
    return int(n_str) + int(n_str*2) + int(n_str*3) + int(n_str*4)


for digit in range(4, 8):
    result = compute(digit)
    print(f"compute({digit}) = {result}")
