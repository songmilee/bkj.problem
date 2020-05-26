import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target = list("balloon")
        word_cnt = collections.Counter(text)
        print(word_cnt)

        cnt = 0
        is_run = True
        while is_run:
            for word in target:
                if word_cnt[word] != 0:
                    word_cnt[word] -= 1
                else:
                    is_run = False
                    break

            cnt += 1

        return cnt-1

if __name__ == "__main__":
    s = Solution()
    result = s.maxNumberOfBalloons("loonbalxballpoon")
    print(result)
