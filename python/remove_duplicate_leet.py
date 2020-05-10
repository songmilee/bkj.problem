class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0

        prev = 0
        for i in range(len(nums)):
            if nums[i] != nums[prev]:
                nums[prev + 1] = nums[i]
                prev += 1

        return prev + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))