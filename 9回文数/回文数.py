class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x>=0 and int(str(x)[::-1])==x

'''
进阶
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0：return False
        res,temp=0,x
        while temp:
            res = res*10 + temp%10
            temp//=10
        return res == x
'''