class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Given a string of digits (from '2' to '9'), return all possible letter combinations
        that the number could represent, based on the phone number keypad mapping.

        Args:
            digits (str): A string containing digits from '2' to '9' (inclusive), each digit 
                          representing a set of characters as per a traditional phone keypad.

        Returns:
            list[str]: A list of all possible letter combinations that the input digits can represent.

        Example:
            letterCombinations("23") -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        """
        
        # If the input string is empty, return an empty list
        if not digits:
            return []

        # Mapping of digits to corresponding letters on a phone keypad
        mapping = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        # Initialize the result with an empty string (to help build combinations)
        result = [""]

        # Iterate over each digit in the input string
        for i in str(digits):
            # Convert the character digit into an integer to map to letters
            num = int(i)
            
            # Get the corresponding letters for the current digit
            letters = mapping[num]

            # Temporary list to hold the updated combinations
            temp = []

            # Combine each prefix in result with each letter for the current digit
            for prefix in result:
                for letter in letters:
                    temp.append(prefix + letter)

            # Update result to the new list of combinations
            result = temp

        # Return the final list of letter combinations
        return result
