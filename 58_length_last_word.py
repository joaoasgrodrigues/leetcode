class Solution:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring  consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        for n in s[::-1].split(' '):
            if n != '': return len(n)
    
        # counter = 0
        # for n in s[::-1]:
        #     if n == ' ':
        #         if counter > 0: return counter 
        #         else: continue
        #     else:
        #         counter += 1
        # return counter