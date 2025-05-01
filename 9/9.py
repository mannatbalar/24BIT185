def count_alpha_digits(s):
    
    alpha_count = 0
    digit_count = 0
    
    for char in s:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    
    return {'alphabets': alpha_count, 'digits': digit_count}


test_string = "Hello123, this is test4567!"
result = count_alpha_digits(test_string)

print("Input string:")
print(test_string)
print("\nCount result:")
print(result)
