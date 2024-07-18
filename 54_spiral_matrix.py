class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 
        Given an m x n matrix, return all elements of the matrix in spiral order.
        """
        side = 0
        # 0 top
        # 1 right
        # 2 down
        # 3 left

        spiral_order = []
        total_elements = len(matrix[0]) * len(matrix)
        while len(spiral_order) < total_elements:
            if side == 0:
                spiral_order += matrix[0]
                del matrix[0]
            if side == 1:
                spiral_order += [row[-1] for row in matrix]
                for row in matrix:
                    del row[-1]
            if side == 2:
                spiral_order += matrix[-1][::-1]
                del matrix[-1]
            if side == 3:
                spiral_order += [row[0] for row in matrix][::-1]
                for row in matrix:
                    del row[0]
            side += 1
            if side == 4: side = 0
        return spiral_order