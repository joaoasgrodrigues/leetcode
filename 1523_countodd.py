class Solution:
    """
    Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
    """
    # alternative SLOW
    # return len([1 for n in range(low, high + 1) if n & 1 == 1])

    # alternative SLOW
    # counter = 0
    # for n in range(low, high + 1):
    #     if n % 2 != 0:
    #         counter += 1
    #     # even with bitwise operation
    #     # if n & 1 == 1:
    #     #     counter += 1
    # return counter

    # with math thinking
    def countOdds(self, low: int, high: int) -> int:
        half = (high - low) // 2
        if low & 1 == 1 or high & 1 == 1:
            return half + 1
        return half