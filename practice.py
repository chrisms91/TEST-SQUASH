

# const test1 = maximumSubarraySizeK([2,3,4,1,5], 2);
# const test2 = maximumSubarraySizeK([2,1,5,1,3,2], 3);
# console.log(test1, test2)


# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def maximum_subarray_size_k(nums, k):
    max_sum = 0
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            ++left
    
    return max_sum

test1 = [2,1,5,1,3,2]
k = 3
print(maximum_subarray_size_k(test1, k))
