"""
LeetCode Problem 136: Single Number

Problem Statement:
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2, 2, 1]
Output: 1

Example 2:
Input: nums = [4, 1, 2, 1, 2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.

Approach:
- The XOR bitwise operation allows us to solve this problem with a linear time complexity (O(n)) and constant space complexity (O(1)).
- Using XOR properties:
  - `a ^ a = 0`
  - `a ^ 0 = a`
- XORing all elements in the array cancels out the pairs and leaves the single number.

"""

class Solution:
    def singleNumber(self, nums):
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

# Example usage:
if __name__ == "__main__":
    param_1 = [2, 2, 1]  # Example input
    solution = Solution()
    result = solution.singleNumber(param_1)
    print(result)  # Output: 1