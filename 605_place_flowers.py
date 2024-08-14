class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.  
        """
        flowers = flowerbed.count(1)
        
        # only one place for flower
        if flowerbed == [0]:
            if n <= 1:
                return True
            return False
        
        if flowerbed == [1]:
            if n == 0:
                return True
            return False

        # start [0 0 ...]
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1

        # end   [... 0 0]
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                
        if flowerbed.count(1) - flowers >= n:
            return True
        
        return False