using System;
//https://leetcode.com/problems/maximum-subarray/
namespace csharp 
{
    public class SubArray
    {
        public int MaxSubArray(int[] nums) {
            var result = -2147483648;

            var size = nums.Length;
            
            int[] dp = new int[size];
            dp[0] = nums[0];
            result = Math.Max(dp[0], result);

            if(size == 1) return dp[0];

            for(var i = 1; i < size; i++)
            {
                dp[i] = Math.Max(dp[i-1] + nums[i], nums[i]);
                result = Math.Max(dp[i], result);
            }

            return result;
        }
    }
}