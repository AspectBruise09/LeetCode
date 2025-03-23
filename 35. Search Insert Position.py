class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Determines the index at which the target should be inserted into the sorted list `nums`.
        
        Args:
            nums (list[int]): A sorted list of integers.
            target (int): The target value to search for or insert.
        
        Returns:
            int: The index of `target` if it is present, otherwise the index where it 
                 should be inserted to maintain the sorted order.
        """
        
        # Check if the target is already present in the list
        if target in nums:
            return nums.index(target)
        
        # Iterate through the reversed list to find the correct insertion point
        for idx, elem in enumerate(reversed(nums)):
            # If the target is greater than the current element, determine the insert position
            if target > elem:
                return len(nums) - idx
        
        # If the target is smaller than all elements, insert at the beginning
        return 0
