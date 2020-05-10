class Solution:
    def twoSum(self, nums, target):
        result = {}

        for i, num in enumerate(nums):
            another_val = target - num
            if another_val not in result:
                result[num] = i
            else:
                return [result[another_val], i]


if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([3, 3], 6)
    print(result)