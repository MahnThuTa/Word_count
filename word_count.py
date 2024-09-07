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