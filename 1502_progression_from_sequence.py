class Solution:
    """
    A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false."""
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        progression = arr[1] - arr[0]
        for index, number in enumerate(arr[:-1]):
            if arr[index + 1] - number != progression: 
                return False 
        return True