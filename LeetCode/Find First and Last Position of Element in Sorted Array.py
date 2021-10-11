"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

# Solution
#Time complexity is O(log(n))......as bisect module itself uses the binary search algorithm
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect.bisect_left(nums,target)
        r=bisect.bisect_right(nums,target)
        if l<r:
            return([l,r-1])
        else:
            return([-1,-1])    
