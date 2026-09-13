class Solution(object):
    def isSubsequence(self, s, t):
        
        i = 0
        j = 0
        
        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                i += 1
            
            j += 1
        
        return i == len(s)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna