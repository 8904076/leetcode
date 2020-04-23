'''
字符串方法
class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        x=int('-'+strx[1:][::-1]) if x<0 else int (strx[::-1])
        return 0 if x < -2**31 or x > 2**31-1 else x
'''
'''
数学方法
'''
class Solution:
    def reverse(self, x: int) -> int:
        flag=-1 if x<0 else 1
        x= abs(x)
        res = 0
        while x:
            res = res*10 + x%10
            x//=10
        res *= flag
        return 0 if res <-2**31 or res >2**31-1 else res 
