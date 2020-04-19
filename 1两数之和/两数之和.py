'''
暴力穷举法
'''
from typing import  List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return  None



'''
利用一个容器cache

from typing import  List
class Solution:
    def twoSum(self,nums:List[int],target: int)->List[int]:
        cache={}
        for idx,num in enumerate(nums):
            cur = target-num
            if num in cache:
                return [cache[num],idx]
            cache[cur] = idx
        return None
'''


