from collections import Counter


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

    def twoSum(self, nums, target):
        dic = dict()
        for index, fig in enumerate(nums):
            if target - fig in dic:
                return dic[target - fig], index
            dic[fig] = index

    def searchInsert(self, nums, target):
        if target in nums:
            return (nums.index(target))
        else:
            nums.append(target)
            nums.sort()
            return (nums.index(target))

    def plusOne(self, digits):
        ans = 0
        digits = digits[::-1]
        ans = digits[0] + 1
        for i in range(len(digits)):
            if i != 0:
                ans = ans + digits[i] * (10 ** i)

        digits = str(ans)
        x = list(digits[::1])
        return (x)

    def singleNumber(self,nums):
        dic = dict()
        numset = set(nums)
        for i in numset:
            dic[i] = 0
            print(dic)
        for i in nums:
            dic[i] += 1
        for i in numset:
            if dic[i] == 1:
                return (i)



    # def search(self, nums, target):

# ...........................................................
# ss = Solution()

# .........................data..............................
nums = [-1,0,3,5,9,12]
target = 9
# .........................main..............................
for i in range(len(nums)) :
    if nums[i] == target :
        print(i)



