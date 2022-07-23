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

    def isIsomorphic(self, s: str, t: str) -> bool:
        result = {}
        uniqueValues = set()

        for idx, i in enumerate(s):
            if i not in result:
                if t[idx] in uniqueValues: return False
                result[i] = t[idx]
                uniqueValues.add(t[idx])
            else:
                if result[i] != t[idx]: return False

        print(result)
        return True

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        resultList = {}
        common = {}
        result = [-1]

        for idx, i in enumerate(list1):
            resultList[i] = idx

        for idx, i in enumerate(list2):
            if i in resultList:
                common[i] = resultList[i] + idx

        prevValue = -1
        for key in common:
            if (prevValue == -1):
                result = [key]
            else:
                if (prevValue > common[key]):
                    result = []
                    result.append(key)
                elif (prevValue == common[key]):
                    result.append(key)
                else:
                    pass
            prevValue = common[key]
        return result

    def firstUniqChar(self, s: str) -> int:
        result = {}
        unique = set()

        for idx, i in enumerate(s):
            if i not in result:
                result[i] = idx
                unique.add(i)
            else:
                if i in unique: unique.remove(i)

        for i in result:
            if i in unique: return result[i]

        return -1

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        space = {}

        for idx, i in enumerate(nums):
            if i not in space:
                space[i] = idx
            else:
                if (abs(idx - space[i]) <= k):
                    return True
                else:
                    space[i] = idx

        return False