class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implements the `strStr()` function, which returns the index of the first occurrence 
        of the substring `needle` in the string `haystack`. If `needle` is not found, 
        it returns -1. If `needle` is an empty string, it returns 0.

        Args:
            haystack (str): The main string to be searched.
            needle (str): The substring to search for within `haystack`.

        Returns:
            int: The index of the first occurrence of `needle` in `haystack` or -1 if not found.
        """
        # Return 0 if the needle is an empty string
        if not needle:
            return 0
        
        # Return -1 if needle is longer than haystack, as it cannot be found
        if len(needle) > len(haystack):
            return -1
        
        # Iterate through the possible starting indices in haystack
        # The loop ends at (len(haystack) - len(needle) + 1) to avoid index out of range
        for i in range(0, len(haystack) - len(needle) + 1):
            # Check if the substring of haystack from i to i + len(needle) matches needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # Return -1 if no match is found
        return -1
