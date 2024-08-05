class Solution:
    """ 
    At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

    Note that you do not have any change in hand at first.

    Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for n in bills:
            if n == 5:
                fives += 1
                continue
            if n == 10:
                tens += 1
                if fives >= 1:
                    fives -= 1
                    continue
            if n == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                    continue
                if fives >= 3:
                    fives -= 3
                    continue
            return False 
        return True
    
        # change = []
        # for n in bills:
        #     change.append(n)
        #     if n == 5: 
        #         continue
        #     elif n == 10:
        #         if 5 in change:
        #             change.remove(5)
        #             continue
        #     elif n == 20:
        #         if change.count(5) == 3:
        #             change.remove(5)
        #             change.remove(5)
        #             change.remove(5)
        #             continue
        #         elif change.count(5) == 1 and change.count(10) == 1:
        #             change.remove(5)
        #             change.remove(10)
        #             continue
        #     return False
        # return True 