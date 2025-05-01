import string

def ispangram(sentence):
    
    
    alphabet_set = set(string.ascii_lowercase)
    
    
    sentence_set = set(sentence.lower())

    
    return alphabet_set <= sentence_set


test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels",
    "Hello, this is not a pangram!"
]

for sentence in test_sentences:
    result = ispangram(sentence)
    print(f"\"{sentence}\" -> Pangram: {result}")
