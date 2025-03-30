class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to its Roman numeral representation.

        Args:
        num (int): The integer to be converted to a Roman numeral.

        Returns:
        str: The Roman numeral representation of the input integer.
        """
        
        # Mapping of integer values to their corresponding Roman numerals
        roman_map = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        roman_str = ""  # Initialize an empty string to build the Roman numeral result
        
        # Loop through each value-symbol pair in the Roman numeral mapping
        for value, symbol in roman_map:
            # Keep subtracting the value from num while it's greater than or equal to the current value
            while num >= value:
                roman_str += symbol  # Append the Roman numeral symbol to the result string
                num -= value  # Decrease num by the value

        result = roman_str  # Assign the final Roman numeral string to result
        return result  # Return the result string
