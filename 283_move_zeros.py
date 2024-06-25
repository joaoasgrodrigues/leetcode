class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            zeros = Counter(nums)[0]
            n = 0 
            while True:
                if nums[n] == 0:
                    del nums[n]
                    nums.append(0)
                    zeros -= 1
                    if zeros == 0:
                        break
                else:
                    n += 1