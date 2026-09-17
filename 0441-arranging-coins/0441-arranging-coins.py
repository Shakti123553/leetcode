class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=n
        total=0
        for i in range(1,(count//2)+2):
            count-=i
            if count < 0:
                break
            total+=1
        return total