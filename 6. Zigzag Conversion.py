class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a given string `s` into a zigzag pattern on a specified number 
        of rows and then reads it row by row to form a new string.

        The zigzag pattern follows a pattern where the string moves down the rows
        and then reverses direction to move back up until the entire string is processed.

        Args:
            s (str): The input string to be converted.
            numRows (int): The number of rows to arrange the string in a zigzag pattern.

        Returns:
            str: The resulting string formed by reading the zigzag pattern row-wise.

        Examples:
            Input: s = "PAYPALISHIRING", numRows = 3
            Output: "PAHNAPLSIIGYIR"
            
            Input: s = "PAYPALISHIRING", numRows = 4
            Output: "PINALSIGYAHRPI"
            
            Input: s = "A", numRows = 1
            Output: "A"
        """
        
        # Return the original string if only 1 row is needed or if numRows exceeds string length
        if numRows == 1 or numRows > len(s):
            return s
        
        # Create an empty list for each row to store characters
        rows = [[] for _ in range(numRows)]
        
        # Initialize variables for current row position and direction
        current_line = 0  # Keeps track of the current row
        direction = -1  # Controls the zigzag direction (up or down)

        # Iterate through each character in the string
        for i in range(len(s)):
            # Add the character to the current row
            rows[current_line].append(s[i])
            
            # Change direction when reaching the top or bottom row
            if current_line == 0 or current_line == numRows - 1:
                direction *= -1  # Reverse direction
            
            # Move to the next row in the current direction
            current_line += direction
        
        # Join all characters from each row to form the final result
        result = "".join(["".join(row) for row in rows])
        
        return result
