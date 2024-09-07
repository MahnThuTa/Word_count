import re

from collections import Counter

def count_words(sentence):
    sentence = sentence.lower().replace("_", "-")
    w = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
    # Use Counter to count occurrences of each word
    word_count = Counter(w)
    
    return word_count

sentence = input("Enter a sentence: ")
print(count_words(sentence))



# mahn_branch
# import re
# from collections import Counter

# def count_words(sentence: str):
#     sentence = sentence.lower().replace("_", "-")
    
#     words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
#     word_count = Counter(words)
    
#     return dict(word_count)

# print(count_words(sentence=input("Enter sentence: ")))

# import string

# def count_words(sentence):
#     sentence = sentence.lower().replace("_", "-")
    
#     for char in string.punctuation.replace("'", ""):
        
#     sentence = sentence.replace(char, " ")
    
#     # Split the sentence into words
#     words = sentence.split()
#     print(string.punctuation)
    
#     word_count = {}
    
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
    
#     return word_count

# print(count_words(sentence=input("Enter sentence: ")))

import re

def count_words(sentence):
    sentence = sentence.lower().replace("_", "-")
    
    words = re.findall(r"\b\w+(?:'\w+)?\b", sentence)
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

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

