class Solution(object):
    def splitArray(self, nums, k):

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:

                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

            if subarrays <= k:
                right = mid
            else:
                left = mid + 1

        return left

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna