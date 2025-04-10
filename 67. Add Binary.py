class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.

        Args:
            a (str): A binary string representing the first operand.
            b (str): A binary string representing the second operand.

        Returns:
            str: A binary string representing the sum of a and b.
        """

        # Ensure both binary strings are of equal length by padding the shorter one with leading zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        bin_sum = ""  # Initialize the resulting binary sum
        carry = 0     # Initialize carry to handle overflow at each bit addition

        # Iterate from the least significant bit (rightmost) to the most significant (leftmost)
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])  # Convert character to integer (0 or 1)
            bit_b = int(b[i])

            # Calculate the total sum of the two bits and the carry
            total = bit_a + bit_b + carry

            # Append the binary digit of total % 2 (either '0' or '1') to the left of the result
            bin_sum = str(total % 2) + bin_sum

            # Update the carry (1 if total >= 2, else 0)
            carry = total // 2

        # If there's a carry remaining after the final iteration, add it to the front
        if carry:
            bin_sum = "1" + bin_sum

        result = bin_sum
        return result
