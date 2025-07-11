# Prompt: Write a function to check for palindromes


# AI Output (before)

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Racecar")) # True



# Issues Identified  

# 1. Doesn't remove non-alphanumeric characters (e.g., punctuation, spaces)
# 2. Fails on input like: "A man, a plan, a canal: Panama"
# 3. No input validation or handling of edge cases



# Improved Code (After)

import re    # Importing the regular expressions module for pattern-based string cleaning

def is_better_palindrome(s):
    s = re.sub(r'[^a-z0-9]', ' ', s.lower()) # clean string
    return s == s[::-1]



# Test Cases

print(is_better_palindrome("Racecar")) # True
print(is_better_palindrome("A man, a plan, a canal: Panama")) # True
print(is_better_palindrome("Hello")) # False



# Result / Insight

# 1. Improved version handles special characters and spaces
# 2. Uses regex for cleaning input before comparison
# 3. More robust and realistic for real-world use cases
