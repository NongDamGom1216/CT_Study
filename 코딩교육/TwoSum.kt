// Leetcode

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        
        for (i: Int in 0 until nums.size) {
            for (j: Int in i + 1 until nums.size) {
                if (nums[i] + nums[j] == target) {
                    return intArrayOf(i, j)
                }
            }
        }
        throw IllegalArgumentException("No solution")
    }
}