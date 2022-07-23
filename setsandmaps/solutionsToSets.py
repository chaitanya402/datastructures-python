from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums = set()
        solution = set()

        for i in nums1:
            if i not in nums: nums.add(i)

        for i in nums2:
            if i in nums:
                if i not in solution: solution.add(i)

        return solution

    def isHappy(self, n: int) -> bool:
        visit = set()

        while (n not in visit):
            visit.add(n)

            mod, rem, sum = 0, n, 0
            while (rem > 0):
                mod = rem % 10
                sum = sum + (mod * mod)
                rem = rem // 10
                print(rem, mod, sum)
            print(sum)
            if sum == 1: return True
            n = sum

        return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        results = {}

        for idx, i in enumerate(nums):
            # if i <= target :
            lookout = target - i

            if lookout in results:
                return [idx, results[lookout][i]]

            results[i] = {lookout: idx}

        return []