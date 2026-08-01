class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
    
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float("inf")
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            # If character count matches countT requirement, increment 'have'
            if char in countT and window[char] == countT[char]:
                have += 1
                
            # Shrink window from left as long as it remains valid
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                    
                # Pop left character
                left_char = s[l]
                window[left_char] -= 1
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""