class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i = 0
        cnt = 0

        while cnt < size :            
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1
            cnt += 1


                


if __name__ == "__main__":
    nums = [0,0,1]
    Solution().moveZeroes(nums)

    print(nums)