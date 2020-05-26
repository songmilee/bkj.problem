class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #range -2^31 ~ 2^31 - 1

        MAX_VAL = pow(2, 31) - 1
        MIN_VAL = -pow(2, 31)

        is_under_zero = False
        if x < 0 : is_under_zero = True

        target = str(abs(x))[::-1]

        result = int(target)
        if is_under_zero: result = -result

        if result >= MAX_VAL : return 0
        elif result <= MIN_VAL : return 0

        return result



if __name__ == "__main__":
    print(Solution().reverse(120))