class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        res=0
        while x>0:
            dig=x%10
            res=res*10+dig
            x//=10
        if res>2**31-1 or res<-2**31:
            return 0
        return res*sign