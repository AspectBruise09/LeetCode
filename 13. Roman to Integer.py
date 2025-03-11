# LeetCode: 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Args:
            s (str): A string representing a Roman numeral.

        Returns:
            int: The integer equivalent of the Roman numeral.
        """

        # Step 1: Convert Roman numerals to their integer values
        first = []
        for i in s:
            if i == "I":
                first.append(1)
            elif i == "V":
                first.append(5)
            elif i == "X":
                first.append(10)
            elif i == "L":
                first.append(50)
            elif i == "C":
                first.append(100)
            elif i == "D":
                first.append(500)
            else:
                first.append(1000)

        # Step 2: Process values to handle subtractive notation
        second = []  # Stores numbers that do not require subtraction
        third = []   # Stores pairs where subtraction is needed
        idx = 0
        while idx < len(first):
            # If the current value is less than the next one, it's a subtractive case
            if not (idx < len(first) - 1 and first[idx] < first[idx + 1]):
                second.append(first[idx])  # Add the value directly
                idx += 1
            else:
                third.append([first[idx], first[idx + 1]])  # Store the subtractive pair
                idx += 2  # Skip the next value as it's already processed

        # Step 3: Calculate the final result
        result = sum(second)  # Sum of non-subtractive values
        for i in third:
            result += i[-1] - i[0]  # Subtract smaller value from larger one

        return result
