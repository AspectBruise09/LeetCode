# 9. Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check whether an integer x is a palindrome. A palindrome is a number that reads the same forward and backward.

        Args:
            x (int): The integer to be checked.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False
        
        # Convert x to a string and compare digits from the start and end
        for i in range(1, len(str(x)) // 2 + 1):
            # If the digits at positions i-1 and -i don't match, return False
            if str(x)[i - 1] != str(x)[-i]:
                return False
        
        # If all digits match, return True
        return True
