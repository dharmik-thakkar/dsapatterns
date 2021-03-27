#######################################################################################################################
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]
#######################################################################################################################

def find_average_of_k_size_subarray(nums: list[int], k: int) -> list[int]:
    result = []
    window_sum = 0
    window_start = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k-1:
            result.append(window_sum / k)
            window_sum -= nums[window_start]
            window_start += 1
    return result


print(find_average_of_k_size_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))  # [2.2, 2.8, 2.4, 3.6, 2.8]
