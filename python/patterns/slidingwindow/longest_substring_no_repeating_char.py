#######################################################################################################################
# Given a string, find the length of the longest substring which has no repeating characters.
#
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
#
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
#
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".
#######################################################################################################################

def longest_substring_no_repeating_char(input_str: str) -> int:
    window_start = 0
    is_present = [None for i in range(26)]
    max_window = 0
    for i in range(len(input_str)):
        char_ord = ord(input_str[i]) - 97
        if is_present[char_ord] is not None:
            window_start = max(window_start, is_present[char_ord] + 1)
        is_present[char_ord] = i
        max_window = max(max_window, i - window_start + 1)
    return max_window


print(longest_substring_no_repeating_char('aabccbb'))
print(longest_substring_no_repeating_char('abbbb'))
print(longest_substring_no_repeating_char('abccde'))
print(longest_substring_no_repeating_char('abcabcbb'))
print(longest_substring_no_repeating_char('bbbbb'))
print(longest_substring_no_repeating_char('pwwkew'))
