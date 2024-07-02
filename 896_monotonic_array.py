class Solution:
    """
    An array is monotonic if it is either monotone increasing or monotone decreasing.
    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
    Given an integer array nums, return true if the given array is monotonic, or false otherwise.
    """
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_temp = sorted(nums)
        if nums_temp == nums: return True 
        if nums_temp[::-1] == nums: return True
        return False