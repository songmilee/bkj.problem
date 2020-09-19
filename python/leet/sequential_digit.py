# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
# 10 <= low <= high <= 10^9

class Solution(object):

    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        low_len = len(str(low))
        high_len = len(str(high))

        ans = []

        for i in range(low_len, high_len + 1):            
            for j in range(1, 9):
                seq_val = 0
                plus_val = j
                for k in range(i - 1, -1, -1):
                    seq_val = seq_val + pow(10, k) * plus_val
                    plus_val = plus_val + 1

                if seq_val > high: break
                if seq_val >= low and self.isSequentialDigit(seq_val):
                    ans.append(seq_val)
        
        
        return ans

    def isSequentialDigit(self, num):
        result = True

        str_num = str(num)
        size = len(str_num)

        for i in range(1, size):
            prev_num = int(str_num[i - 1])
            cur_num = int(str_num[i])

            if cur_num - prev_num != 1:
                result = False
                break
            
        return result
      
              

if __name__ == "__main__":
    s = Solution()

    low = 1000
    high = 13000

    print(s.sequentialDigits(low, high))