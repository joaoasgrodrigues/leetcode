class Solution:
    """
    A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false."""
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()                                              # faster in-line
        progression = arr[1] - arr[0]
        for index in range(1, len(arr[:-1])):                   # less readable but faster
            if arr[index + 1] - arr[index] != progression:
                return False 
                
        return True 
    
        # arr = sorted(arr)
        # progression = arr[1] - arr[0]
        # for index, number in enumerate(arr[:-1]):
        #     if arr[index + 1] - number != progression: 
        #         return False 
        # return True