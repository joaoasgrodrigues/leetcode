class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
        You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

        An integer x.
        Record a new score of x.

        '+'.
        Record a new score that is the sum of the previous two scores.

        'D'.
        Record a new score that is the double of the previous score.

        'C'.
        Invalidate the previous score, removing it from the record.

        Return the sum of all the scores on the record after applying all the operations.
        The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
        """
        score = []
        for op in range(len(operations)):
            instruction = operations[op]
            if instruction == 'C':
                del score[-1]
            elif instruction == 'D':
                score.append(2 * score[-1])
            elif instruction == '+':
                score.append(score[-1] + score[-2])
            elif instruction.isnumeric() or instruction[0] == '-':
                score.append(int(instruction))
        return sum(score)