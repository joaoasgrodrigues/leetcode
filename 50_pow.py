class Solution:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    """
    def myPow(self, x: float, n: int) -> float:
        pow = 1
        if  n == 0: return 1

        if n < 0:
            x = 1 / x
            n = -n
            
        # Exponentiation by squaring
        # a^2n = (a^2)^n
        while n > 0:

            if n % 2 != 0:
                pow *= x
          
            n = n // 2
            # n = n >> 1
            x *= x
            print(n)

        
        return pow