''''
--Largest Contiguous Sum--

A subarray is a part of an array including one or more contiguous/adjacent elements.

Example
Array: [1, 2, 3, 4, 5]
Subarrays:
[1]
[2]
[3]
[4]
[5]
[1, 2]
[2, 3]
[3, 4]
[4, 5]
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
[1, 2, 3, 4]
[2, 3, 4, 5]
[1, 2, 3, 4, 5]
If we find the sum of the elements of any subarray then that sum will be known as a contiguous sum.''''


class Solution:
    def largestContiguousSum(self, arr: List[int]) -> int:
        """
        Finds the largest contiguous sum in the given array.

        Args:
            arr: The array to find the largest contiguous sum in.

        Returns:
            The largest contiguous sum in the array.
        """
        max_ending_here = 0
        max_so_far = -float("inf")
        for i in range(len(arr)):
            max_ending_here = max(max_ending_here + arr[i], arr[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
