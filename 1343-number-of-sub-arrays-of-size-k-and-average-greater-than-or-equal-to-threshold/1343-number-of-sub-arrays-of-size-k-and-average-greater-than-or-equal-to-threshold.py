class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):

        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= k * threshold:
            count += 1

        for i in range(k, len(arr)):

            window_sum -= arr[i-k]
            window_sum += arr[i]

            if window_sum >= k * threshold:
                count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna