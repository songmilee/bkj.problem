class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        long_array = []
        short_array = []

        if len(nums1) > len(nums2):
            long_array = nums1
            short_array = nums2
        else:
            long_array = nums2
            short_array = nums1

        cnt_map = {}
        result = []
        for i in short_array:
            cnt = long_array.count(i)
            if i in long_array:
                if cnt_map.get(i) == None : 
                    cnt_map[i] = 1
                    result.append(i)
                elif cnt_map.get(i) < cnt:
                    cnt_map[i] += 1
                    result.append(i)
            
        return result
        

if __name__ == "__main__":
    a = [3, 1, 2]
    b = [1, 1]
    print(Solution().intersect(a, b))