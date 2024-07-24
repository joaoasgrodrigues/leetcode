class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        zero_rows = set()
        zero_columns = set()

        # identify zeroes
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zero_columns.add(c)
                    zero_rows.add(r)
        
        # change rows and columns to zeros
        for r in range(rows):
            if r in zero_rows:
                matrix[r] = [0] * columns
            for c in zero_columns:
                matrix[r][c] = 0
