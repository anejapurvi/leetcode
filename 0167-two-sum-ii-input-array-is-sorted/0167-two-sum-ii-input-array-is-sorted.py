class Solution(object):
    def twoSum(self, numbers, target):
        
        L = 0
        R = len(numbers) - 1
        
        while L < R:
            
            total = numbers[L] + numbers[R]
            
            if total < target:
                L += 1
            
            elif total > target:
                R -= 1
            
            else:
                return [L + 1, R + 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna