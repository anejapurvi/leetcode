class Solution(object):
    def mySqrt(self, x):

        if x < 2:
            return x

        low = 1
        high = x // 2

        while low <= high:

            mid = (low + high) // 2

            if mid * mid <= x:
                low = mid + 1
            else:
                high = mid - 1

        return high

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna