def convert(input_string):
    words = input_string.split()
    unique_sorted_words = sorted(set(words))
    return ' '.join(unique_sorted_words)
test_input = "apple banana mango banana orange apple grape"
result = convert(test_input)
print("Original string:")
print(test_input)
print("\nAfter removing duplicates and sorting:")
print(result)
