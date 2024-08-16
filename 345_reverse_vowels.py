class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and return it.
        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
        """
        new_string = list(s)
        vowels = [c for c in s if c in "aeiouAEIOU"]
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                new_string[i] = vowels[-1]
                del vowels[-1]
        return ''.join(new_string)