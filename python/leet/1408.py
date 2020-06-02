class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        size = len(words)
        result = set()

        for i in range(0, size - 1):
            for j in range(i + 1, size):
                if words[i] in words[j]:
                    result.add(words[i])                    
                if words[j] in words[i]:
                    result.add(words[j])
        
        return list(result)


if __name__ == "__main__":
    input = ["leetcode","et","code"]
    print(Solution().stringMatching(input))