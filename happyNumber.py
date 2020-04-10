class Solution(object):
    def isHappy(self, n, out):
        """
        task: Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay),
        or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy numbers.



        :type n: int
        :type out: List[]
        :rtype: bool

        Example
        ---------
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
        returns True
        """

        loop = 0
        while (n != 1) and (loop <= 15):
            n_str = str(n)
            out.append(n)
            n = 0
            for num in n_str:
                n += int(num) ** 2
            loop += 1

        if n != 1:
            return False
        else:
            return True




