# LeetCode: 1. Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given a list of integers `nums` and an integer `target`, 
        return the indices of the two numbers such that they add up to `target`.
        
        Args:
        nums (list[int]): A list of integers.
        target (int): The target sum to find.
        
        Returns:
        list[int]: A list containing the indices of the two numbers that add up to `target`.
        """
        # Iterate through each element in the list `nums`
        for first_idx, first_elem in enumerate(nums):
            # Iterate through the remaining elements after the current element
            for second_idx, second_elem in enumerate(nums[first_idx + 1:], start=first_idx + 1):
                # If the sum of the two elements equals the target, return their indices
                if first_elem + second_elem == target:
                    return [first_idx, second_idx]
