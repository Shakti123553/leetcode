class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num=nums
        temp1=nums[0]
        
        k=1
        
        for i in range(0,len(num)):
            temp2=num[i]
            if temp1 != temp2:
                nums[k]=num[i]
                k+=1
                temp1 = temp2
            else :
                temp1 = temp2
                continue
        return k

        