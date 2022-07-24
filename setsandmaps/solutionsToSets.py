from typing import List, Optional

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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        nodes = {}
        output = []

        def dfs(node):
            if (not node): return ''
            key = f'{node.val},{dfs(node.left)},{dfs(node.right)}'
            if (key in nodes):
                nodes[key] = nodes[key] + 1
            else:
                nodes[key] = 1

            if nodes[key] == 2:
                print(key, nodes[key])
                output.append(node)

            return key

        dfs(root)
        return output

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        count = 0
        for stone in stones :
            if stone in jewel : count = count + 1
        return count

    def lengthOfLongestSubstring(self, s: str) -> int:

        existingchar = set()
        lengths = {}
        string = []
        if (not s): return 0
        if len(s) == 1: return 1

        for char in s:
            if (char not in existingchar):
                existingchar.add(char)
                string.append(char)
            else:
                while (char in string):
                    popValue = string.pop(0)
                    existingchar.remove(popValue)

                existingchar.add(char)
                string.append(char)
            lengths[len(string)] = ''.join(string)

        more = -1
        for key in lengths:
            if more == -1:
                more = key
            elif more < key:
                more = key
            else:
                pass
        if more == -1:
            return 0
        else:
            return more

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

            sums = {}
            for i in nums1:
                for j in nums2:
                    print(i, j)
                    if i + j not in sums:
                        sums[i + j] = 1
                    else:
                        sums[i + j] = sums[i + j] + 1
            count = 0
            for i in nums3:
                for j in nums4:
                    if 0 - (i + j) in sums: count = count + sums[0 - (i + j)]

            return count

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = {}
        order = []
        for i in nums:
            if i not in frequencyCount:
                frequencyCount[i] = 1
            else:
                frequencyCount[i] = frequencyCount[i] + 1

        frequencyCount = sorted(frequencyCount, key=lambda x: frequencyCount[x], reverse=True)
        return frequencyCount[:k]
sol = Solution()

sol.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])