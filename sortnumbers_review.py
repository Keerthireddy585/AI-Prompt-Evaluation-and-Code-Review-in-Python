# Prompt: Write a function to sort a list of integers in ascending order


# AI Output (Before)

def sort_numbers(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(sort_numbers([5, 2, 9, 1, 5, 6]))



# Issues Identified

# 1. Inefficient sorting algorithm (O(n^2)) - similar to selection sort
# 2. Modifies the original list in-place (could be undesirable)
# 3. Does not handle non-integer or mixed-type inputs
# 4. Python has built-in sorting that is faster and cleaner



# Improved Code (After)

def better_sort_numbers(nums):
    
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements must be integers")
    
    return sorted(nums)



# Test Cases

print(better_sort_numbers([5, 2, 9, 1, 5, 6]))       # Output: [1, 2, 5, 5, 6, 9]
print(better_sort_numbers([-3, 0, 2, 7]))            # Output: [-3, 0, 2, 7]
# print(better_sort_numbers([3, 'a', 2]))            # Raises ValueError



# Result / Insight

# 1. Improved version uses Python’s optimized sorting algorithm (Timsort)
# 2. Adds input validation to prevent runtime errors
# 3. Returns a new list instead of modifying the original, improving reusability