class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in a given string.
        
        A word is defined as a maximal substring consisting of non-space characters only.
        Trailing spaces are ignored before computation starts.

        Parameters:
            s (str): The input string containing words and possibly spaces.

        Returns:
            int: The length of the last word in the string.
        """
        length = 0  # Initialize length counter for the last word

        # Iterate over the string in reverse, after stripping trailing spaces
        for i in s.rstrip()[::-1]:
            if i == " ":
                # Stop if a space is encountered after starting the count
                break
            else:
                length += 1  # Count each character in the last word

        result = length  # Store final result
        return result
