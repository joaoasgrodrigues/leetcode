# not mine
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        for (x, y) in coordinates[2:]:
            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
                return False
        return True     
    

class Solution:
    """
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = None
        for n in range(len(coordinates) - 1):
            y = coordinates[n + 1][1] - coordinates[n][1]
            x = coordinates[n + 1][0] - coordinates[n][0]

            if x == 0:
                new_slope = float("inf")
            else:
                new_slope = y / x

            if slope is None: 
                slope = new_slope
                continue

            if slope != new_slope: return False
        
        return True