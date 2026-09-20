class Solution(object):
    def findMaxLength(self, nums):

        prefix = {0: -1}
        current_sum = 0
        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum in prefix:
                length = i - prefix[current_sum]
                max_length = max(max_length, length)

            else:
                prefix[current_sum] = i

        return max_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna