'''
本质上是求矩形面积。可以用双指针来约束矩形
用res来表示面积，不断更新取最大值
l，r表示两个指针，应该移动较短的指针来寻求最优解
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res,l,r = 0,0,len(height)-1
        while True:
            if l>r:
                break
            res = max(res,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res