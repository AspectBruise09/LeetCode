# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the input string contains a valid sequence of parentheses.

        A string is valid if:
        - Every opening bracket has a corresponding closing bracket of the same type.
        - The brackets are closed in the correct order.

        Args:
        s (str): The string containing only the characters '(', ')', '{', '}', '[' and ']'.

        Returns:
        bool: True if the string is valid, False otherwise.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), where n is the length of the string.
        """
        
        # Stack to store opening parentheses encountered in the string
        stack = []
        
        # Dictionary to map each closing bracket to its corresponding opening bracket
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if the stack is not empty, 
                # otherwise use a dummy value ('#') to indicate the stack is empty
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                if mapping[char] != top_element:
                    # If it doesn't match, the string is invalid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched and closed
        # If the stack is not empty, some opening brackets were never closed
        return not stack
