class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
    
        size = len(arr)
        j = 0
        for i in range(size):
            if j >= size: break

            if arr[j] == 0:
                arr.insert(j + 1, 0)
                j = j + 2
                arr.pop()
            else:
                j = j + 1

        
        print(arr)


if __name__ == "__main__":
    arr = [1,0,2,3,0,4,5,0]
    Solution().duplicateZeros(arr)