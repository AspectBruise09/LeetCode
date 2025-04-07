class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Given a non-empty array of digits representing a non-negative integer, 
        increment the integer by one and return the resulting array of digits.
        
        The digits are stored such that the most significant digit is at the head of the list,
        and each element in the list represents a single digit of the number.

        Args:
            digits (list[int]): The list of digits representing the number to increment.

        Returns:
            list[int]: The list of digits after incrementing the number by one.
        """
        
        # Initialize result as a reference to the input digits list
        result = digits
        
        # Traverse the digits from the least significant (rightmost) to the most significant (leftmost)
        for i in range(len(result) - 1, -1, -1):  # Start from the last digit
            # If the current digit is less than 9, simply increment it by 1 and stop
            if result[i] < 9:
                result[i] += 1  # Increment the digit
                break  # No need to continue, as we don't have a carry-over anymore
            
            # If the current digit is 9, set it to 0 (carry over) and move to the next left digit
            result[i] = 0
        
        # If the leftmost digit is 0 after processing, we have a carry over that affects the most significant digit
        if result[0] == 0:
            result = [1] + result  # Insert 1 at the start to handle the carry over (e.g., 999 -> 1000)
        
        # Return the final result after incrementing
        return result
