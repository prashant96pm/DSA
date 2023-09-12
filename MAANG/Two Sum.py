''''
--Two Sum--

Given an array A and an integer target, find the indices of the two numbers in the array whose sum is equal to the given target.'''


class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        """
        Finds the indices of the two numbers in the array whose sum is equal to the given target.

        Args:
            A: The array of integers.
            target: The target sum.

        Returns:
            A list of two integers, the indices of the two numbers whose sum is equal to the target.
        """

        nums_map = {}
        for i, num in enumerate(A):
            nums_map[num] = i

        for i, num in enumerate(A):
            complement = target - num
            if complement in nums_map and nums_map[complement] != i:
                return [i, nums_map[complement]]

        return []
