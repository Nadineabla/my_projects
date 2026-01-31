from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for word in strs :
            for i in range(len(word)):
                if word[i] != strs[0][i]:
                    return word[:i]
        
        return strs[0]

s = Solution().longestCommonPrefix(["flower","flow","flight"])
print(s)
