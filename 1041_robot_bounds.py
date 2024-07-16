class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """ 
        On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

        The north direction is the positive direction of the y-axis.
        The south direction is the negative direction of the y-axis.
        The east direction is the positive direction of the x-axis.
        The west direction is the negative direction of the x-axis.
        The robot can receive one of three instructions:

        "G": go straight 1 unit.
        "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
        "R": turn 90 degrees to the right (i.e., clockwise direction).
        The robot performs the instructions given in order, and repeats them forever.

        Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
        """

        # does not move
        g = instructions.count("G")
        if g == 0: return True

        # stays in same place
        instructions = instructions.replace("LR", "")
        instructions = instructions.replace("RL", "")

        l = instructions.count("L")
        r = instructions.count("R")
        # does not turn
        if r == 0 and l == 0: return False
        
        angle = abs(l - r)
        # faces the same direction than the start direction
        if angle == 0 or angle % 4 == 0:

            # magic intuition, second half different than the first so not same position
            if instructions[:len(instructions) // 2] != instructions[len(instructions) // 2:]:
                return False
        
        return True