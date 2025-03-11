# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Finds the longest common prefix among a list of strings.

        Args:
            strs (list of str): A list of strings to find the common prefix from.

        Returns:
            str: The longest common prefix among the strings in the list. 
                 If there is no common prefix, returns an empty string.
        """
        
        # Sort the list of strings by length to minimize the number of checks
        strs.sort(key=len)
        
        # Take the shortest string as the reference for the prefix comparison
        key = strs[0]
        
        # Remove the shortest string from the list since it's already used
        strs.remove(key)
        
        # Initialize the result as an empty string
        result = ""
        
        # Loop through substrings of the key string, starting from the entire string down to 1 character
        for i in range(len(key), 0, -1):
            # Check if all strings in the list start with the current prefix substring of 'key'
            if all(j.startswith(key[0:i]) for j in strs):
                result = key[0:i]  # Update the result with the current prefix
                break  # Exit the loop once the longest common prefix is found
        
        # Return the result (the longest common prefix)
        return result
