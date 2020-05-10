class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(int(size/2)):
            target = size - i - 1

            temp = s[i]
            s[i] = s[target]
            s[target] = temp

if __name__ == "__main__":
    Solution().reverseString(list("hello"))