class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_indices = {}
        max_length = 0
        start = 0

        for i, char in enumerate(s):
            if char in char_indices and char_indices[char] >= start:
                start = char_indices[char] + 1

            char_indices[char] = i
            current_length = i - start + 1
            max_length = max(max_length, current_length)

        return max_length
