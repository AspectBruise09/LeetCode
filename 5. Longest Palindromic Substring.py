class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds and returns the longest palindromic substring within the given string.

        Args:
            s (str): Input string to search for palindromic substrings.

        Returns:
            str: The longest palindromic substring found in the input string.
        """

        def test_palindrome(value: str) -> bool:
            """
            Checks if a given string is a palindrome.

            Args:
                value (str): The string to be checked.

            Returns:
                bool: True if the string is a palindrome, False otherwise.
            """
            # Compare the string with its reverse to check for palindrome
            return value == value[::-1]

        # List to store all palindromic substrings
        substrings = []

        # Generate all possible substrings by iterating over start and end indices
        for i in range(1, len(s) + 1):
            for j in range(i, len(s) + 1):
                # Extract substring from index (i-1) to j
                candidate = s[i - 1:j]
                
                # Check if the extracted substring is a palindrome
                if test_palindrome(candidate):
                    # Add the palindrome to the list of substrings
                    substrings.append(candidate)

        # Sort substrings by length in descending order and select the longest one
        result = sorted(substrings, key=len, reverse=True)[0]

        # Return the longest palindromic substring
        return result
