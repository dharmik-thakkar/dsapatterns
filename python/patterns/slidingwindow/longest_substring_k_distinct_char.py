#######################################################################################################################
# Given a string, find the length of the longest substring in it with no more than K distinct characters.
#
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
#
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
#
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
#######################################################################################################################

def longest_substring_k_distinct_char(inp_str: str, k: int) -> int:
    counter = {}
    substr_size = 0
    window_start = 0
    for i in range(len(inp_str)):
        if inp_str[i] in counter:
            substr_size += 1
            counter[inp_str[i]] += 1
        elif len(counter) < k:
            counter[inp_str[i]] = 1
            substr_size += 1
        else:
            counter[inp_str[i]] = 1
            while len(counter) > k:
                if counter[inp_str[window_start]] == 1:
                    del counter[inp_str[window_start]]
                else:
                    counter[inp_str[window_start]] -= 1
                window_start += 1
            substr_size = max(substr_size, i-window_start)
    return substr_size


print(longest_substring_k_distinct_char('araaci', 2))
print(longest_substring_k_distinct_char('araaci', 1))
print(longest_substring_k_distinct_char('cbbebi', 3))
