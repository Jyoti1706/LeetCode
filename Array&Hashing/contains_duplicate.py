'''
https://leetcode.com/problems/contains-duplicate/
'''

class Solution:
    def containsDuplicate(self, nums):
        arr = set()
        for num in nums:
            if num in arr:
                return True
            else:
                arr.add(num)
        return False


nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))