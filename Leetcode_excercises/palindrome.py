class Solution:
    def palindrome(self, nums: int) -> bool:
        text = str(nums)
        if text == text[::-1] :
            return True
        else :
            return False
            
result= Solution().palindrome(1223)
print(result)