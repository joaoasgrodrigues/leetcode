class Solution:
    def average(self, salary: List[int]) -> float:
        """
        You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

        Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
        """
        # sort heavier
        # return sum(sorted(salary)[1:-1]) / (len(salary) - 2)
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)
         