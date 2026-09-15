class Solution(object):
    def firstBadVersion(self, n):

        low = 1
        high = n 

        while low < high:
             mid = (low + high)//2

             if isBadVersion(mid):
                high = mid 

             else:
                low = mid + 1
        
        return low

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna