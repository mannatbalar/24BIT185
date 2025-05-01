def ispalindrome(s):
    
    
    cleaned = s.replace(" ", "").lower()
    
    
    return cleaned == cleaned[::-1]


test_strings = [
    "Madam",
    "Race car",
    "Hello",
    "No lemon no melon"
]

for text in test_strings:
    result = ispalindrome(text)
    print(f"\"{text}\" -> Palindrome: {result}")
