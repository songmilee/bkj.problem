class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_one = 0
        max_cnt = 0

        for i in nums:
            if i == 1:
                cnt_one = cnt_one + 1
            else:
                max_cnt = max(max_cnt, cnt_one)
                cnt_one = 0

        max_cnt = max(max_cnt, cnt_one)
        
        return max_cnt

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]

    result = Solution().findMaxConsecutiveOnes(nums)
    print(result)