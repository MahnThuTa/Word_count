import re
from collections import Counter

def count_words(sentence: str):
    sentence = sentence.lower().replace("_", "-")
    
    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
    word_count = Counter(words)
    
    return dict(word_count)

print(count_words(sentence=input("Enter sentence: ")))
