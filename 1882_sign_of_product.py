class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for n in nums:
            if n == 0: return 0
            if n < 0: negatives += 1
        if negatives % 2 != 0: return -1
        return 1
                

        # Solution without performing operation
        # if 0 in nums: return 0
        # if sum(1 for n in nums if n < 0) % 2 != 0: return -1
        # return 1

        # Solution that performs the operation
        # product = reduce(operator.mul, nums)     # slower
        # product = reduce(lambda a, b: a * b, nums)
        # if product > 0:
        #     return 1
        # elif product < 0:
        #     return -1
        # else:
        #     return 0