class Solution(object):
    
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        product = 1

        
        for i in range(n):
            answer[i] = product
            product *= nums[i]

        product = 1

     
        for i in range(n - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna