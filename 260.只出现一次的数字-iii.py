#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x ^= i
        x1 = 0
        x2 = 0
        spare = x & -x
        for i in nums:
            if i & spare:
                x1 ^= i
            else:
                x2 ^= i

        return [x1,x2]
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     dic = {}
    #     ret = []
    #     for item in nums:
    #         v = dic.setdefault(item,1)
    #         if v:
    #             dic[item] = v+1
    #     for key,val in dic.items():
            
    #         if val==2:
    #             ret.append(key)
    #     return ret
            
            
# @lc code=end

