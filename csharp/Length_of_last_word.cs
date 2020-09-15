//https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/
using System.Linq;

namespace csharp
{
    class Solution
    {
        public int LengthOfLastWord(string s) 
        {
            if(s.Length == 0) return 0;

            int result = 0;
            
            string[] splitWord = s.Split(" ");
            var size = splitWord.Length;

            for(var i = size - 1; i >= 0; i--)
            {
                result = splitWord[i].Length;
                if(result != 0) break;

                result = 0;
            }

            return result;        
        }
    }
}