class Solution(object):
    def maxArea(self, height):
        
        L = 0
        R = len(height) - 1
        
        max_area = 0
        
        while L < R:
            
            area = (R - L) * min(height[L], height[R])
            
            max_area = max(max_area, area)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna