class Solution(object):
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            total = 0
            count = 1

            for weight in weights:
                if total + weight > mid:
                    count += 1
                    total = weight
                else:
                    total += weight

            if count <= days:
                right = mid
            else:
                left = mid + 1

        return left
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna