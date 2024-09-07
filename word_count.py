import re


# mahn_branch
from collections import Counter

def count_words(sentence: str):
    sentence = sentence.lower().replace("_", "-")
    
    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
    word_count = Counter(words)
    
    return dict(word_count)

print(count_words(sentence=input("Enter sentence: ")))

#--------------------------------------------------------

# wai_solu
"""
input: "one fish two fish red fish blue fish"),
output: {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}

1. all output key lower
2. filter every punc except space(\\s) and "_"
3. split according using "_" or "\\s"
4. use frozenset to get key
"""


def count_words(sentence: str):
    sentence = sentence.lower().replace("_", ",")
    
    clean_sen_li = re.findall(r"\b[a-z0-9']+\b", sentence)
    
    keys = set(clean_sen_li)

    return {k:clean_sen_li.count(k) for k in keys}
