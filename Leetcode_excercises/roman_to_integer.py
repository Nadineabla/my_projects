class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_number = 0
        n = len(s)
        for i in range(n):
            current_value = roman_map[s[i]]
            if i+1 < n and current_value < roman_map[s[i+1]]:
                total_number -= current_value
            else:
                total_number += current_value

        return total_number
        
        
s = Solution().romanToInt('IX')
print(f'the integer is {s}')  