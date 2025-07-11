# Prompt: Write a function to find the factorial of a number


# AI Output (Before)

def factorial(n):
    result = 1

    for i in range(1,n):
        result *= i
    return result

print(factorial(5))    # output : 24 (Incorrect)



# Issues Identified

# 1. The loop ends at n-1 instead of n (range is exclusive of the upper limit), Should be range(1, n+1)
# 2. No input validation for negative or non-integer values
# 3. No support for 0! = 1 case, though this code handles it by default



# Improved Code (After)

def improved_factorial(n):

    if not isinstance (n, int):
        raise TypeError("Input must be an Integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result=1
    for i in range (1, n+1):   # Loop from 1 to n (inclusive)
        result*=i
    return result



# Test Cases

print(improved_factorial(5)) # Output : 120
print(improved_factorial(0)) # Output : 1
print(improved_factorial(-3))  # Raises ValueError
print(improved_factorial(3.5)) # Raises TypeError



# Result / Insight

# 1. Fixed off-by-one error in the loop
# 2. Added input validation for negative and non-integer values
# 3. Ensures correct handling of edge cases like 0 and invalid input types