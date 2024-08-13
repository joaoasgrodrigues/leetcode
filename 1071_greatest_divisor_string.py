class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
        Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.        
        """
        largest, smaller = (str1, str2) if len(str1) > len(str2) else (str2, str1)

        for index in reversed(range(1, len(smaller) + 1)):
            # extract possible sequence
            sequence = smaller[:index]

            # get a full sequence with the same size as largest string
            if sequence * (len(largest) // len(sequence)) == largest: 
                
                # get a full sequence with the same size as smaller string
                if sequence * (len(smaller) // len(sequence)) == smaller:
                    return sequence
                
        return ""