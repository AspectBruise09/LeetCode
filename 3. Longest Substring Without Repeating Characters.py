class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: Length of the longest substring without repeating characters.
        """
        def test_duplicate(value: str) -> bool:
            """
            Checks if the given string has duplicate characters.

            Args:
                value (str): The substring to check.

            Returns:
                bool: True if duplicates exist, False otherwise.
            """
            # Compare length of the string with the length of unique characters in the set
            return len(value) != len(set(value))

        # Return 0 for an empty string
        if not s:
            return 0

        # List to store all substrings without duplicates
        substrings = []

        # Iterate over all possible starting points of substrings
        for i in range(1, len(s) + 1):
            toggle_duplicate = False  # Flag to break inner loop when duplicates are found

            # Iterate to generate substrings from the current starting point
            for j in range(i, len(s) + 1):
                # Extract the substring from index (i - 1) to j
                substring = s[i - 1:j]

                # Check for duplicates in the substring
                if not test_duplicate(substring):
                    # Add valid substring to the list
                    substrings.append(substring)
                else:
                    # Stop further extension if duplicates are found
                    toggle_duplicate = True
                    break

            # Skip further checks from this starting point if duplicates were encountered
            if toggle_duplicate:
                continue

        # Sort substrings by length in descending order and get the length of the longest one
        result = len(sorted(substrings, key=len, reverse=True)[0])
        return result
