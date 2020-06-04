class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        binary = "{0:b}".format(N)        

        cnt = 0
        max_cnt = 0
        for i in binary:
            if i == '1':
                max_cnt = max(cnt + 1, max_cnt)
                cnt = 1
            else:
                cnt += 1
        
        return max_cnt -1

if __name__ == "__main__":
    print(Solution().binaryGap(6))