class Solution:
    """
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
    """
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        To determine if three values can define the sides of a triangle, check if the sum of any two sides is greater than the third side for all three combinations:
        a + b > c
        a + c > b
        b + c > a
        """
        nums.sort(reverse=True)
        for n in range(len(nums) - 2):
            if nums[n] > nums[n + 1] + nums[n + 2]: continue
            if nums[n + 1] +  nums[n + 2] == nums[n]: continue
            return sum(nums[n:n+3])
        return 0