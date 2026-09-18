class Solution(object):
    def findAnagrams(self, s, p):
        
        if len(p) > len(s):
            return []
        
        p_count = [0] * 26
        window_count = [0] * 26
        
        # Frequency of characters in p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        result = []
        left = 0
        
        for right in range(len(s)):
            
            # Add new character
            window_count[ord(s[right]) - ord('a')] += 1
            
            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            # Check if current window is an anagram
            if window_count == p_count:
                result.append(left)
        
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna