# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        result = True

        dest_list = [x[2] for x in trips]
        max_dest = max(dest_list)

        path_in_cap = [0] * (max_dest + 1)

        for i in trips:
            for j in range(i[1], i[2]):
                path_in_cap[j] += i[0]

                if(path_in_cap[j] > capacity):
                    result = False
                    return result
        
        return result


if __name__ == "__main__":
    s = Solution()
    
    trips = [[2,1,5],[3,3,7]]
    capacity = 4

    print(s.carPooling(trips, capacity))