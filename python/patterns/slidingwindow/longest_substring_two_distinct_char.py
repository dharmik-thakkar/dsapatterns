#######################################################################################################################
# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits in each basket.
# The only restriction is that each basket can have only one type of fruit.
#
# You can start with any tree, but once you have started you can’t skip a tree.
# You will pick one fruit from each tree until you cannot,
# i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.
#
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
#
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
#######################################################################################################################

def longest_substring_two_distinct_char(trees: list[str]) -> int:
    counter = {}
    substr_size = 0
    window_start = 0
    for i in range(len(trees)):
        if trees[i] in counter:
            substr_size += 1
            counter[trees[i]] += 1
        elif len(counter) < 2:
            counter[trees[i]] = 1
            substr_size += 1
        else:
            counter[trees[i]] = 1
            while len(counter) > 2:
                if counter[trees[window_start]] == 1:
                    del counter[trees[window_start]]
                else:
                    counter[trees[window_start]] -= 1
                window_start += 1
            substr_size = max(substr_size, i - window_start)
    return substr_size


print(longest_substring_two_distinct_char(['A', 'B', 'C', 'A', 'C']))
print(longest_substring_two_distinct_char(['A', 'B', 'C', 'B', 'B', 'C']))
