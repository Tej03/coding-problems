# Solution 1
n = int(input())
nums = list(map(int, input().split()))[:n]
k = int(input())
sum = 0
for i in range(k):  #since the value of k=4, we will add the first ele from the subarray (of length 4) to the sum
    sum += nums[i]
maxSum = sum   # at present, the value of maxSum is equal to sum value (sum = 1 & maxSum = 1)

i = k    # for next k values
j = 0     
while i < len(nums):
    sum -= nums[j] # removing value from the front (subtracting) in order to slide through the list
    sum += nums[i] # adding new element to the sum to compare the maxSum 
    maxSum = max(maxSum, sum)
    i += 1
    j += 1
print(maxSum/k) # maximum average 


# Solution 2
# def findMaxAverage(self, nums: List[int], k: int) -> float:
#         # Calculate the sum of the first window
#         current_sum = sum(nums[:k])
#         max_sum = current_sum
        
#         # Slide the window over the array
#         for i in range(k, len(nums)):
#             current_sum += nums[i] - nums[i - k]
#             max_sum = max(max_sum, current_sum)
        
#         # Return the maximum average
#         return max_sum / k


# Solution 3
# def findMaxAverage(self, nums: List[int], k: int) -> float:
#         m = sum(nums[:k])
#         ans = m
#         for i in range(k, len(nums)):
#             m += nums[i]-nums[i-k]
#             if ans < m:
#                 ans = m
#         return ans/k