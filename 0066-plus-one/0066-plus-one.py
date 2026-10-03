class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=0
        for i in digits:
            num=(num*10)+i
        list1 = list(map(int, str(num + 1)))
        return list1



        