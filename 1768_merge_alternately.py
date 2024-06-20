class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_alternate = ""
        for n in range(max(len(word1), len(word2))):
            if word1:
                merge_alternate += word1[0]
            if word2:
                merge_alternate += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]

        return merge_alternate