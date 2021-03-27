#######################################################################################################################
# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.
#
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
#
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
#
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
#######################################################################################################################
import math


def smallest_subarray_given_sum(nums: list[int], k: int) -> int:
    min_size = math.inf
    curr_sum = 0
    window_start = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        while curr_sum >= k:
            if i - window_start + 1 < min_size:
                min_size = i - window_start + 1
            curr_sum -= nums[window_start]
            window_start += 1
    return min_size


print(smallest_subarray_given_sum([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_given_sum([2, 1, 5, 2, 8], 7))
print(smallest_subarray_given_sum([3, 4, 1, 1, 6], 8))
