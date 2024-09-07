import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower().replace("_", "-")
    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    
    return word_count

sentence = input("Enter a sentence: ")
print(count_words(sentence))
