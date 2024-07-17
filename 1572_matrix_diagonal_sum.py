class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Given a square matrix mat, return the sum of the matrix diagonals.
        Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
        """
        counter = 0

        # odd rows counts only the center element, sets row to zero   
        if len(mat) % 2 == 1:
            counter += mat[len(mat) // 2][len(mat[0]) // 2]
            mat[len(mat) // 2] = [0] * len(mat)

        # from left and right extract diagonal elements
        index = 0
        for row in mat:
            counter += row[index] + row[-index - 1]
            index += 1
        
        return counter