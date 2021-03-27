#######################################################################################################################
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
#
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
#
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].
#######################################################################################################################

def maximum_sum_subarray_size_k(nums: list[int], k: int) -> int:
    max_sum = 0
    window_start = 0
    window_sum = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k-1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= nums[window_start]
            window_start += 1
    return max_sum


print(maximum_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3))
print(maximum_sum_subarray_size_k([2, 3, 4, 1, 5], 2))
