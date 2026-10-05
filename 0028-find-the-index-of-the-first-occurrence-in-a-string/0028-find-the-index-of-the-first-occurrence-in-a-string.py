class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sto=""
        for i in range(len(haystack) - len(needle) + 1):
            for j in range (len(needle)):
                if needle[j] == haystack[i+j]:
                    sto += needle[j]
                    if sto == needle:
                        return i
                    
                else:
                    break
            sto=""
        
        return -1



                

            

                        

                
            
                
            

        