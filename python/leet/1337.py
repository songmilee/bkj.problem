class Solution(object):
    def kWeakestRows(self, mat, k):
        # mat : List[List[int]]
        # k : int
        # rtype : List[int]

        idx = 0
        soldier_cnt = []
        for i in mat:
            soldier_cnt.append([idx, sum(i)])
            idx = idx + 1
        
        soldier_cnt.sort(key=lambda a: [a[1], a[0]])
        
        result = []
        for i in range(k):
            result.append(soldier_cnt[i][0])
        
        return result

if __name__ == "__main__":
    mat = [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]]
    result = Solution().kWeakestRows(mat, 2)
    print(result)