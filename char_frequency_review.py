# Prompt: Count the frequency of characters in a string


# AI Output (Before)

def char_frequency(s):

    freq={}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_frequency("hello world")) # Output:{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}



# Issues Identified

# 1. Includes spaces and punctuation by default - may not be desired in all use cases
# 2. Does not normalize case (e.g., 'H' and 'h' are treated as different characters)
# 3. Could be simplified using Python's built-in 'collections.Counter'



# Improved Code (After)

from collections import Counter

def better_char_frequency(s):
    cleaned = s.replace(" ", "").lower()  # Remove spaces, convert to lowercase
    return dict(Counter(cleaned))



# Test Cases

print(better_char_frequency("hello world"))      
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

print(better_char_frequency("Data Science"))      
# Output: {'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}



# Result / Insight

# 1. Improved readability and performance by using 'Counter'
# 2. Normalized input by converting to lowercase and removing spaces
# 3. Makes frequency analysis more meaningful in real-world applications