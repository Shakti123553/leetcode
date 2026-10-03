class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        first=0
        last=len(nums)-1
        while first<=last:
            mid=(first+last)//2
            if target > nums[mid]:
                first=mid+1
            elif target == nums[mid]:
                return mid
            else:
                last=mid-1
        return first

       
            

                
            

        