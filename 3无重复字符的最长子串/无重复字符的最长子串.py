'''
red:整形，用于返回，储存当前最长的子串长度。
start：整形，用于保存当前子串的开始下标。
cache：字典，用于保存每个字母的最近下标。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,res,cache=0,0,{}
        for idx,c in enumerate(s):
            if c in cache and cache[c]>=start:
                start = cache[c]+1
                cache[c]=idx
            else:
                cache[c] = idx
                cur = idx-start+1
                res=max(res,cur)
        return res
