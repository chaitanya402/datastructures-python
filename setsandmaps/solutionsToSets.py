from typing import List
"""
list comprehension :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


is equivalent for 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

"""

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

        """
        
        [] -> stack , que 
        [].pop() --> stack 
        [].pop(1) --> que
        list() 
        set() //hash set 
        {} //hash map 
        linked list // class Node cur , next 
        doubly linked list // class Node cur , next , prev
        
        Big O for all
        map, set , 
        linked list , 
        doubly linked list 
        array 
        
        trees - important
        graph - important - dijkstra algo 
        heaps - study 
        
        
        
        
        """

        for idx, i in enumerate(nums):
            if i not in space:
                space[i] = idx
            else:
                if (abs(idx - space[i]) <= k):
                    return True
                else:
                    space[i] = idx

        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}

        for i in strs:
            sort = "".join(sorted(list(i)))
            if sort not in strDict:
                strDict[sort] = [i]
            else:
                strDict[sort].append(i)
        print(strDict)
        res = []
        for i in strDict:
            res.append(strDict[i])
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = 9

        # rows
        for r in range(N):
            row = [c for c in board[r] if c != '.']
            if len(row) != len(set(row)): return False

        # columns
        for c in range(N):
            col = [board[r][c] for r in range(N) if board[r][c] != '.']
            if len(col) != len(set(col)): return False

            # blocks

        def helper(R, C):
            l = set()
            for r in range(R, R + 3):
                for c in range(C, C + 3):
                    if board[r][c] == '.': continue
                    if board[r][c] not in l:
                        l.add(board[r][c])
                    else:
                        return False
            return True

        for r in range(0, N, 3):
            for c in range(0, N, 3):
                if helper(r, c):
                    continue
                else:
                    return False
        return True
sol = Solution()

sol.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])